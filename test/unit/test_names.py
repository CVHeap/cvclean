'''
Tests that ensure company and human names are removed.
'''
# CV Heap
import cvclean.filters.names


# Test document with fake names
NAME_DOCUMENT = '''FRED FLINSTONE

While working at Rubble Industries, I was responsible for making sure boulders
were never dropped on any noggins. Fortunately, the only time that ever
happened was when Barney stopped over and tickled Dino, the dinosaur.'''


class TestNames:
    '''Tests against a filtered document loaded with various names.'''
    result = None

    def setup_method(self):
        '''Send document through filters.'''
        self.result = cvclean.filters.names.apply(NAME_DOCUMENT).lower()

    def test_non_names(self):
        '''Check for words that should have remained.'''
        assert 'dinosaur' in self.result
        assert 'noggins' in self.result
        assert 'boulders' in self.result

    def test_self_reference(self):
        '''Check for self-referential words that should have remained.'''
        assert ', i ' in self.result

    def test_no_person(self):
        '''Check for names that should have been removed.'''
        assert 'fred' not in self.result
        assert 'flinstone' not in self.result
        assert 'barney' not in self.result
        assert 'dino,' not in self.result

    def test_company_is_left_for_the_entities_filter(self):
        '''Check that an organization is not this filter's business.'''
        assert 'rubble industries' in self.result
