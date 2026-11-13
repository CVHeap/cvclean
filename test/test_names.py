'''
Tests that ensure company and human names are removed.
'''
import cvclean


# Test document with fake names
NAME_DOCUMENT = '''
skeleton document with
the names Fred Flinstone and
also Rubble Industries.'''


class TestNames:
    '''Tests against a filtered document loaded with various names.'''
    result = None

    def setup_method(self):
        '''Send document through filters.'''
        self.result = cvclean.apply_filters(NAME_DOCUMENT)

    def test_no_person(self):
        '''Spot check some names that should have been removed.'''
        assert 'Wilma' not in self.result
