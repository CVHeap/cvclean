'''
Tests that ensure contact details and record identifiers are removed.
'''
# CV Heap
import cvclean.filters.contacts


# Test document with a profile row, contact details and record links
CONTACT_DOCUMENT = '''# Jeremy Bearimy

[lnkd.url/jimminy](https://lnkd.url/jimminy) | [gh.url/jb](https://gh.url/jb)

Phone: +55 555-867-5309 | Email: jeremy.bearimy@emaildomain.tld

## Certifications

| **SSCE** (SaltStack Certified Engineer) | [71C6EC7](https://ssc.url/) |

Further details are available at [personal.url/lab](https://personal.url/lab)

- Read further for accomplishments [Juniper Networks, Suitable Technologies]
- Reviewed RADIUS logs and MySQL schemas for the reporting team
'''


class TestContacts:
    '''Tests against a filtered document carrying contact details.'''
    result = None

    def setup_method(self):
        '''Send document through filters.'''
        self.result = cvclean.filters.contacts.apply(CONTACT_DOCUMENT)

    def test_whole_link_collapses_label_and_target_together(self):
        '''Check that nothing of a link survives its token.'''
        assert '[pii] | [pii]' in self.result
        assert 'lnkd.url' not in self.result
        assert 'https' not in self.result

    def test_separators_survive(self):
        '''Check that the profile row keeps its pipes.'''
        assert self.result.count('|') == 5

    def test_labels_stay_outside_the_token(self):
        '''Check that prose around a contact detail remains.'''
        assert 'Phone: [pii] | Email: [pii]' in self.result

    def test_email_needs_no_valid_top_level_domain(self):
        '''Check that an unverifiable address is still removed.'''
        assert 'emaildomain.tld' not in self.result

    def test_record_identifier_collapses(self):
        '''Check that a verification link goes whole.'''
        assert '71C6EC7' not in self.result

    def test_credential_name_survives(self):
        '''Check that the certification beside a link remains.'''
        assert '**SSCE** (SaltStack Certified Engineer)' in self.result

    def test_bracketed_aside_is_not_a_link(self):
        '''Check that brackets with no target keep their contents.'''
        assert '[Juniper Networks, Suitable Technologies]' in self.result

    def test_prose_is_untouched(self):
        '''Check that technologies resembling records remain.'''
        assert 'RADIUS logs and MySQL schemas' in self.result
