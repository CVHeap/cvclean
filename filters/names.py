'''
CV Clean: Filter for Names
'''
import functools
import re
from nameparser import HumanName
from presidio_analyzer import AnalyzerEngine


# Redaction token already claimed by an earlier filter
TOKEN = re.compile(
    r'\[(?:pii|employer\d+|altorg\d+|location\d+|school\d+|product\d+'
    r'|date-[a-z0-9]+|datespan\d+mo-[a-z0-9]+)\]')


@functools.lru_cache(maxsize=1)
def _analyzer():
    '''
    Build the analyzer once, on first use.
    '''
    return AnalyzerEngine()


def _subject(blob):
    '''
    Remove the subject's name, read from the document's first line.
    '''
    line = blob.split('\n', 1)[0]
    full = line.lstrip('#').strip()
    if not full:
        return blob
    name = HumanName(full)
    parts = {name.title, name.first, name.middle, name.last, name.suffix}
    blob = blob.replace(full, '[pii]')
    for part in sorted(filter(None, parts), key=len, reverse=True):
        blob = re.sub(rf'\b{re.escape(part)}\b', '[pii]', blob)
    return blob


def _competencies(blob):
    '''
    Return the extent of the Technical Competencies section.
    '''
    match = re.search(r'^## Technical Competencies$', blob, re.MULTILINE)
    if not match:
        return None
    following = re.search(r'^## ', blob[match.end():], re.MULTILINE)
    end = match.end() + following.start() if following else len(blob)
    return match.start(), end


def _others(blob):
    '''
    Remove every other person the engine finds.
    '''
    occupied = [match.span() for match in TOKEN.finditer(blob)]
    competencies = _competencies(blob)
    if competencies:
        occupied.append(competencies)
    found = _analyzer().analyze(text=blob, language='en',
                                entities=['PERSON'])
    for result in sorted(found, key=lambda result: result.start,
                         reverse=True):
        if any(result.start < stop and result.end > begin
               for begin, stop in occupied):
            continue
        blob = blob[:result.start] + '[pii]' + blob[result.end:]
    return blob


def apply(blob):
    '''
    Remove the subject's name and every other person's name.
    '''
    return _others(_subject(blob))
