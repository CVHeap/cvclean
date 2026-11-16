'''
Tests that ensure numerals keep only their first two significant digits.
'''
# CV Heap
import cvclean.filters.numbers


# Test document with numerals of varying precision
NUMBER_DOCUMENT = '''## Professional Experience

Supported over 10,007 employees across more than 300 remote facilities.

- Created Ubuntu 20.04 templates used for manual testing
- Led volunteer pack sessions of 10-80 volunteers, rotating teams
- Resolved a 3-node cluster backlog that was 10-year-overdue
- Maintained Route53, OCFS2, Device42, Bind9, NTLMv2 and Jabberd2
- Hardened IPv4/IPv6 endpoints with 2FA over T1 links for B2B clients
- Delivered $800,000 in annual savings across 42 sites

Tenure already reads as [datespan141mo-under5yr] here.
'''


class TestNumbers:
    '''Tests against a filtered document carrying many numerals.'''
    result = None

    def setup_method(self):
        '''Send document through filters.'''
        self.result = cvclean.filters.numbers.apply(NUMBER_DOCUMENT)

    def test_digits_past_the_second_become_zero(self):
        '''Check that a numeral loses its tail but keeps its width.'''
        assert 'over 10,000 employees' in self.result
        assert '10,007' not in self.result

    def test_separators_and_decimal_width_are_preserved(self):
        '''Check that a version string keeps its trailing zeros.'''
        assert 'Ubuntu 20.00 templates' in self.result

    def test_numerals_already_reduced_are_untouched(self):
        '''Check that two significant digits or fewer are left alone.'''
        assert 'more than 300 remote' in self.result
        assert '$800,000 in annual savings' in self.result
        assert 'across 42 sites' in self.result

    def test_ranges_and_compounds_are_untouched(self):
        '''Check that digits joined by hyphens are left alone.'''
        assert '10-80 volunteers' in self.result
        assert '3-node cluster' in self.result
        assert '10-year-overdue' in self.result

    def test_digits_inside_identifiers_are_untouched(self):
        '''Check that product and protocol names keep their digits.'''
        assert 'Route53, OCFS2, Device42, Bind9, NTLMv2 and Jabberd2' \
            in self.result
        assert 'IPv4/IPv6 endpoints with 2FA over T1 links for B2B' \
            in self.result

    def test_generated_metadata_is_untouched(self):
        '''Check that digits inside a redaction token are not reduced.'''
        assert '[datespan141mo-under5yr]' in self.result
