'''
Ensure full document with all filters applied winds up fully redacted.
'''
import pytest

# CV Heap
import cvclean


def read(document):
    '''Return entire file from test data.'''
    with open(f'test/data/{document}', 'r') as fh:
        return fh.read().strip()


@pytest.mark.parametrize('original, expected', [
    ('bearimy_janice.md', 'bearimy_clean.md'),
    ('bearimy_jeremy.md', 'bearimy_clean.md'),
])
def test_whole_files(original, expected):
    '''Compare filtered document againts expected result'''
    assert cvclean.apply_filters(read(original)) == read(expected)
