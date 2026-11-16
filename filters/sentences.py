'''
CV Clean: Filter for Sentences
'''
import re


# A named team, department or program, with the article left outside
TEAM = re.compile(
    r'\bthe (?P<name>[A-Z][\w-]*(?:(?: |, (?:and )?| and )[A-Z][\w-]*)*)'
    r' (?P<unit>teams?|department|program)\b')

# A possessive attached to a superlative
RANKING = re.compile(r"\b[\w-]+'s [a-z]+est\b")

# First-person text covering health, addiction, recovery or disability
MY = re.compile(r'\bmy\b')
KEYWORD = re.compile(r'\b(?:health|addiction|recovery|disability)\b')


def _team(match):
    '''
    Redact the name, keeping any word in front of a list of names.
    '''
    name = match.group('name')
    keep = ''
    if ', ' in name or ' and ' in name:
        items = re.split(r', (?:and )?| and ', name)
        first = items[0].split()
        length = len(items[-1].split())
        if len(first) > length:
            keep = ' '.join(first[:-length])
    kept = keep + ' ' if keep else ''
    return f"the {kept}[pii] {match.group('unit')}"


def _health(line):
    '''
    Redact whole any bullet or sentence holding first-person health.
    '''
    prefix = '- ' if line.startswith('- ') else ''
    sentences = re.split(r'(?<=\.) ', line[len(prefix):])
    redacted = [
        '[pii]' if MY.search(sentence) and KEYWORD.search(sentence)
        else sentence
        for sentence in sentences]
    return prefix + ' '.join(redacted)


def apply(blob):
    '''
    Remove phrases carrying identity and leave descriptive ones.
    '''
    blob = TEAM.sub(_team, blob)
    blob = RANKING.sub('[pii]', blob)
    return '\n'.join(_health(line) for line in blob.split('\n'))
