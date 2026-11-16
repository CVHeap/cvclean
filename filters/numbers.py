'''
CV Clean: Filter for Numbers
'''
import re


# Numeral with optional thousands separators and decimal width
NUMERAL = re.compile(r'\d+(?:,\d{3})*(?:\.\d+)?')

# Bracketed redaction token holding generated metadata
TOKEN = re.compile(r'\[[^\]]*\]')


def _reduce(blob, match, protected):
    '''
    Zero every digit past the second significant one, in place.
    '''
    start, end = match.span()
    if any(start < stop and end > begin for begin, stop in protected):
        return match.group(0)
    before = blob[start - 1] if start else ''
    after = blob[end] if end < len(blob) else ''
    if before.isalpha() or before == '-' or after.isalpha() or after == '-':
        return match.group(0)
    significant = 0
    reduced = ''
    for char in match.group(0):
        if char.isdigit():
            if significant == 2:
                char = '0'
            elif char != '0' or significant:
                significant += 1
        reduced += char
    return reduced


def apply(blob):
    '''
    Reduce every numeral to two significant digits.
    '''
    protected = [match.span() for match in TOKEN.finditer(blob)]
    return NUMERAL.sub(lambda match: _reduce(blob, match, protected), blob)
