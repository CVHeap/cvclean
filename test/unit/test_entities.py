'''
Tests that ensure organizations classify, localize and number correctly.
'''
# CV Heap
import cvclean.filters.entities


# Test document with organizations under every kind of parent section
ENTITY_DOCUMENT = '''## Technical Competencies

### Server Administration & DevOps

### Software Development

## Professional Experience

### Volkswagen Group of America, Auburn Hills, MI — via TEKsystems

Through TEKsystems I supported Volkswagen, Audi, and Porsche.

Documentation was presented to the international Volkswagen Group.

### Basis Technologies, Chicago, IL

I was hired on a team improving Big Data infrastructure.

## Education

### Dakota State University, Madison, SD

## Volunteer Experience

### Upper Midwest Great Dane Rescue

Non-profit that rehomes Great Danes in need.

### Avera Oncology Institutional Review Board

Avera Oncology is a regional cancer treatment center.
The Institutional Review Board (IRB) reviews clinical research.

### Tallgrass Recovery

Mentored individuals in recovery, walking them through sobriety.

## Open Source Contributions

### Debian Linux

Debian is a widely-used Linux distribution.
I was granted Debian Developer status after maintaining packages.

### Nginx Web Server

Nginx is a high-performance web server.
I built the Nginx packages for Debian.
'''


class TestEntities:
    '''Tests against a filtered document of organizations.'''
    result = None

    def setup_method(self):
        '''Send document through filters.'''
        self.result = cvclean.filters.entities.apply(ENTITY_DOCUMENT)

    def test_experience_heading_names_an_employer_and_a_location(self):
        '''Check that the parent section decides the kind.'''
        assert ('### [redacted-employer1], [redacted-location1] '
                '— via [redacted-employer2]') in self.result
        assert '### [redacted-employer3], [redacted-location2]' \
            in self.result

    def test_education_heading_names_a_school(self):
        '''Check that an Education org is a school, not an employer.'''
        assert '### [redacted-school1], [redacted-location3]' in self.result

    def test_agency_and_client_are_both_employed(self):
        '''Check that a staffing agency takes an employer token.'''
        assert 'Through [redacted-employer2] I supported' in self.result

    def test_brands_are_only_named(self):
        '''Check that a brand is named rather than employed.'''
        assert ('[redacted-altorg1], [redacted-altorg2], and '
                '[redacted-altorg3].') in self.result

    def test_longest_name_wins_at_a_shared_start(self):
        '''Check that the parent group is its own entity.'''
        assert 'the international [redacted-altorg4]' in self.result

    def test_parent_and_brand_stay_unlinked(self):
        '''Check that a brand never inherits the employer token.'''
        assert 'supported [redacted-employer1]' not in self.result

    def test_heading_tail_without_a_definition_is_consumed(self):
        '''Check that a tail nothing defines joins the token.'''
        assert '### [redacted-altorg8]\n' in self.result
        assert '### [redacted-altorg9]\n' in self.result

    def test_separately_defined_tail_is_kept(self):
        '''Check that a tail with its own defining sentence stays.'''
        assert '### [redacted-altorg6] Institutional Review Board' \
            in self.result

    def test_name_is_redacted_throughout_its_own_section(self):
        '''Check that every mention inside the section is caught.'''
        assert '[redacted-altorg8] is a widely-used' in self.result
        assert 'granted [redacted-altorg8] Developer status' in self.result

    def test_name_survives_outside_its_own_section(self):
        '''Check that elsewhere it reads as a technology.'''
        assert '[redacted-altorg9] packages for Debian.' in self.result

    def test_industry_words_survive_in_body_text(self):
        '''Check that a generic word is not matched on its own.'''
        assert 'Linux distribution' in self.result
        assert 'high-performance web server' in self.result

    def test_plural_of_a_distinctive_run_is_caught(self):
        '''Check that 'Great Danes' takes the organization token.'''
        assert 'rehomes [redacted-altorg5] in need' in self.result

    def test_matching_is_case_sensitive(self):
        '''Check that a lowercase common word survives.'''
        assert 'individuals in recovery' in self.result

    def test_topic_headings_are_untouched(self):
        '''Check that competencies are not mistaken for organizations.'''
        assert '### Server Administration & DevOps' in self.result
        assert '### Software Development' in self.result
