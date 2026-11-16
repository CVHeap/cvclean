'''
CV Clean: Filter for Organizations
'''
import re


# Redaction token already claimed by an earlier filter
TOKEN = re.compile(
    r'\[(?:pii|employer\d+|altorg\d+|location\d+|school\d+|product\d+'
    r'|date-[a-z0-9]+|datespan\d+mo-[a-z0-9]+)\]')

# Experience or education heading: name, city, state and optional agency
PLACEMENT = re.compile(
    r'(?P<name>.+), (?P<city>[^,]+), (?P<state>[A-Z]{2})'
    r'(?: — via (?P<agency>.+))?$')

# Presentation heading: title, venue
PRESENTATION = re.compile(r'(?P<title>.+), (?P<venue>[^,]+)$')

# A run of capitalized words making up a name
NAME = r'[A-Z][\w-]*(?: [A-Z][\w-]*)*'

# Sister company named inside an employer's section
SISTER = re.compile(rf'(?P<name>{NAME}), a sister company')

# Product and its acronym named inside an employer's section
PRODUCT = re.compile(
    rf'development of (?P<name>{NAME}) \((?P<acronym>[A-Z]+)\)')

# Collaborator named in any section, unless a team follows
WORKED_WITH = re.compile(rf'Worked with (?P<name>{NAME})')
SERVED_ON = re.compile(
    rf'^- Served as .*\bon (?P<name>{NAME})\s*$', re.MULTILINE)


def _sections(blob):
    '''
    Walk the headings, returning each with its extent and parent.
    '''
    headings = []
    offset = 0
    for line in blob.split('\n'):
        match = re.match(r'^(#{2,4}) (.*)$', line)
        if match:
            headings.append({
                'level': len(match.group(1)),
                'title': match.group(2),
                'start': offset,
                'body': offset + len(line),
            })
        offset += len(line) + 1
    for index, heading in enumerate(headings):
        heading['end'] = len(blob)
        for later in headings[index + 1:]:
            if later['level'] <= heading['level']:
                heading['end'] = later['start']
                break
        heading['parent'] = next(
            (earlier['title'] for earlier in reversed(headings[:index])
             if earlier['level'] == 2), None)
    return headings


def _overlaps(occupied, start, end):
    '''
    Check whether a span is already claimed or tokenized.
    '''
    return any(start < stop and end > begin for begin, stop in occupied)


def _claim(occupied, claims, start, end, kind, key):
    '''
    Accept a span that overlaps nothing claimed before it.
    '''
    if _overlaps(occupied, start, end):
        return
    claims.append({'start': start, 'end': end, 'kind': kind, 'key': key})
    occupied.append((start, end))


def _claim_all(blob, occupied, claims, name, kind, key, start=0, end=None):
    '''
    Accept every occurrence of a name within a span of the document.
    '''
    pattern = re.compile(rf'\b{re.escape(name)}\b')
    end = len(blob) if end is None else end
    for match in pattern.finditer(blob, start, end):
        _claim(occupied, claims, match.start(), match.end(), kind, key)


def _sentence_openings(blob, start, end):
    '''
    Return the opening words of every sentence in a section body.
    '''
    openings = []
    for line in blob[start:end].split('\n'):
        line = line.lstrip('- ').lstrip('*\'"')
        for sentence in re.split(r'(?<=\.) ', line):
            openings.append(sentence.lstrip('*\'"'))
    return openings


def _opens_with(openings, phrase):
    '''
    Check whether a body sentence opens with a phrase, allowing 'The'.
    '''
    for opening in openings:
        if opening.startswith('The '):
            opening = opening[4:]
        if opening == phrase or opening.startswith(phrase + ' ') \
                or opening.startswith(phrase + '('):
            return True
    return False


def _analyze_heading(blob, heading):
    '''
    Read an organization's heading against the sentences its body opens
    with, returning the kept tail, the short form and the distinctive
    words.
    '''
    words = heading['title'].split()
    openings = _sentence_openings(blob, heading['body'], heading['end'])
    tail = 0
    for count in range(len(words) - 1, 0, -1):
        if _opens_with(openings, ' '.join(words[-count:])):
            tail = count
            break
    short = ''
    for count in range(len(words) - tail, 0, -1):
        candidate = ' '.join(words[:count])
        if _opens_with(openings, candidate):
            short = candidate
            break
    distinctive = short.split() if short else words
    return tail, short, distinctive


def _claim_headings(blob, headings, occupied, claims):
    '''
    Claim what each parent section declares its child headings to be,
    returning the organizations to propagate inside their own section.
    '''
    local = []
    for heading in headings:
        if heading['level'] < 3:
            continue
        start = heading['start'] + len('#' * heading['level']) + 1
        title = heading['title']
        if heading['parent'] == 'Professional Experience':
            if heading['level'] == 4:
                _claim_all(blob, occupied, claims, title, 'employer', title)
                continue
            match = PLACEMENT.match(title)
            location = f"{match.group('city')}, {match.group('state')}"
            for name, kind, key in (
                    (match.group('name'), 'employer', match.group('name')),
                    (location, 'location', location),
                    (match.group('agency'), 'employer',
                     match.group('agency'))):
                if name:
                    _claim_all(blob, occupied, claims, name, kind, key)
        elif heading['parent'] == 'Education' and heading['level'] == 3:
            match = PLACEMENT.match(title)
            location = f"{match.group('city')}, {match.group('state')}"
            _claim_all(blob, occupied, claims,
                       match.group('name'), 'school', match.group('name'))
            _claim_all(blob, occupied, claims, location, 'location',
                       location)
        elif heading['parent'] in ('Volunteer Experience',
                                   'Open Source Contributions'):
            tail, short, distinctive = _analyze_heading(blob, heading)
            kept = len(title.split()) - tail
            name = ' '.join(title.split()[:kept])
            _claim(occupied, claims, start, start + len(name),
                   'altorg', title)
            local.append({
                'key': title,
                'name': name,
                'short': short,
                'distinctive': distinctive,
                'body': heading['body'],
                'end': heading['end'],
            })
        elif heading['parent'] == 'Presentations':
            match = PRESENTATION.match(title)
            _claim(occupied, claims, start,
                   start + len(match.group('title')), 'pii', None)
            venue = match.group('venue')
            offset = start + len(match.group('title')) + 2
            _claim(occupied, claims, offset, offset + len(venue),
                   'altorg', venue)
    return local


def _claim_prose(blob, headings, occupied, claims):
    '''
    Claim prose entities inside each employer's section, by cue.
    '''
    for heading in headings:
        if heading['level'] != 3 \
                or heading['parent'] != 'Professional Experience':
            continue
        body, end = heading['body'], heading['end']
        employer = PLACEMENT.match(heading['title']).group('name')
        words = employer.split()
        for count in range(len(words) - 1, 1, -1):
            phrase = ' '.join(words[:count])
            remainder = re.escape(' ' + ' '.join(words[count:]))
            pattern = re.compile(
                rf'\b{re.escape(phrase)}\b(?!{remainder}\b)')
            matches = list(pattern.finditer(blob, body, end))
            if matches:
                for match in matches:
                    _claim(occupied, claims, match.start(), match.end(),
                           'altorg', phrase)
                break
        first = re.escape(words[0])
        brands = re.compile(
            rf'\b{first}(?:, (?:and )?[A-Z][\w-]*){{2,}}')
        for match in brands.finditer(blob, body, end):
            for brand in match.group(0).split(', '):
                brand = brand.removeprefix('and ')
                _claim_all(blob, occupied, claims, brand, 'altorg',
                           brand, body, end)
        for match in SISTER.finditer(blob, body, end):
            name = match.group('name')
            _claim(occupied, claims, match.start('name'),
                   match.end('name'), 'employer', name)
        for match in PRODUCT.finditer(blob, body, end):
            _claim(occupied, claims, match.start('name'), match.end(),
                   'product', match.group('acronym'))
            _claim_all(blob, occupied, claims, match.group('acronym'),
                       'product', match.group('acronym'), body, end)
        short = re.compile(rf'\b{first}\b(?!\s+[A-Z])')
        for match in short.finditer(blob, body, end):
            _claim(occupied, claims, match.start(), match.end(),
                   'employer', employer)


def _claim_collaborators(blob, occupied, claims):
    '''
    Claim organizations the subject worked with or served on.
    '''
    for match in WORKED_WITH.finditer(blob):
        if re.match(r'teams?\b', blob[match.end():].lstrip()):
            continue
        _claim(occupied, claims, match.start('name'), match.end('name'),
               'altorg', match.group('name'))
    for match in SERVED_ON.finditer(blob):
        _claim(occupied, claims, match.start('name'), match.end('name'),
               'altorg', match.group('name'))


def _claim_local(blob, local, occupied, claims):
    '''
    Claim each named organization's forms inside its own section.
    '''
    for org in local:
        candidates = {org['name'], org['short']}
        words = org['distinctive']
        for begin in range(len(words)):
            for stop in range(begin + 1, len(words) + 1):
                candidates.add(' '.join(words[begin:stop]))
        candidates.discard('')
        pattern = re.compile(
            r'\b(?:' + '|'.join(
                re.escape(candidate) for candidate in sorted(
                    candidates, key=len, reverse=True)) + r')s?\b')
        for match in pattern.finditer(blob, org['body'], org['end']):
            _claim(occupied, claims, match.start(), match.end(),
                   'altorg', org['key'])


def _render(blob, claims):
    '''
    Number each kind in order of first appearance and substitute tokens.
    '''
    numbering = {}
    for claim in sorted(claims, key=lambda claim: claim['start']):
        kind, key = claim['kind'], claim['key']
        if kind != 'pii' and key not in numbering.setdefault(kind, {}):
            numbering[kind][key] = len(numbering[kind]) + 1
    for claim in sorted(claims, key=lambda claim: claim['start'],
                        reverse=True):
        if claim['kind'] == 'pii':
            token = '[pii]'
        else:
            number = numbering[claim['kind']][claim['key']]
            token = f"[{claim['kind']}{number}]"
        blob = blob[:claim['start']] + token + blob[claim['end']:]
    return blob


def apply(blob):
    '''
    Classify, localize and number organizations.
    '''
    headings = _sections(blob)
    occupied = [match.span() for match in TOKEN.finditer(blob)]
    claims = []
    local = _claim_headings(blob, headings, occupied, claims)
    _claim_prose(blob, headings, occupied, claims)
    _claim_collaborators(blob, occupied, claims)
    _claim_local(blob, local, occupied, claims)
    return _render(blob, claims)
