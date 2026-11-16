'''
CV Clean: Filter for Dates
'''
import datetime
import re
from dateutil import parser


# Month name, in full or abbreviated form
MONTH = (r'Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?'
         r'|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?'
         r'|Nov(?:ember)?|Dec(?:ember)?')

# A date in any format a CV carries, resolved by dateutil where needed
DATE = (rf'(?:{MONTH})\s+\d{{4}}|\d{{1,2}}/\d{{4}}|\d{{4}}-\d{{2}}'
        rf'|(?:19|20)\d{{2}}')

# A date range joined by a dash or 'to', with 'Present' only as its end
RANGE = re.compile(rf'\b({DATE})\s*(?:[-–—]|\bto\b)\s*({DATE}|Present)\b')

# A single date standing alone
SINGLE = re.compile(rf'\b(?:{DATE})\b')


def _month_year(text, reference):
    '''
    Resolve detected date text to its year and month.
    '''
    if text == 'Present':
        return reference.year, reference.month
    if text.isdigit():
        return int(text), 12
    parsed = parser.parse(text)
    return parsed.year, parsed.month


def _decay(year, month, reference):
    '''
    Return the decay hint for an end date against the reference.
    '''
    age = (reference.year - year) * 12 + reference.month - month
    if age < 60:
        return 'under5yr'
    if age < 120:
        return 'over5yr'
    return 'over10yr'


def _range(match, reference):
    '''
    Replace a date range with its span length and decay hint.
    '''
    start_y, start_m = _month_year(match.group(1), reference)
    end_y, end_m = _month_year(match.group(2), reference)
    span = (end_y - start_y) * 12 + (end_m - start_m) + 1
    return f'[datespan{span}mo-{_decay(end_y, end_m, reference)}]'


def _single(match, reference):
    '''
    Replace a single date with its decay hint.
    '''
    year, month = _month_year(match.group(0), reference)
    return f'[date-{_decay(year, month, reference)}]'


def apply(blob, reference=None):
    '''
    Collapse dates and date ranges to a span length and decay hint.
    '''
    reference = reference or datetime.date.today()
    blob = RANGE.sub(lambda match: _range(match, reference), blob)
    return SINGLE.sub(lambda match: _single(match, reference), blob)
