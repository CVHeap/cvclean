'''
Ensure full document with all filters applied winds up fully redacted.
'''
import datetime
import functools
import pytest

# CV Heap
import cvclean
import cvclean.filters.dates


# Date all decay hints are measured against
REFERENCE = datetime.date(2027, 1, 1)


def read(document):
    '''Return entire file from test data.'''
    with open(f'test/data/{document}', 'r') as fh:
        return fh.read().strip()


@pytest.mark.parametrize('original, expected', [
    ('bearimy_janice.md', 'bearimy_clean.md'),
    ('bearimy_jeremy.md', 'bearimy_clean.md'),
])
def test_whole_files(monkeypatch, original, expected):
    '''Compare filtered document againts expected result'''
    monkeypatch.setattr(cvclean.filters.dates, 'apply', functools.partial(
        cvclean.filters.dates.apply, reference=REFERENCE))
    assert cvclean.apply_filters(read(original)) == read(expected)
