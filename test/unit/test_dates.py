'''
Tests that ensure dates collapse to a span length and a decay hint.
'''
import datetime

# CV Heap
import cvclean.filters.dates


# Date all decay hints are measured against
REFERENCE = datetime.date(2027, 1, 1)

# Test document with dates in the formats a CV carries
DATE_DOCUMENT = '''## Professional Experience

*Senior Systems Engineer* · Remote · October 2024 – Present

*Linux Desktop Engineer* · Remote · May 2022 - May 2024

*Systems Engineer* · Remote · July 2020 — August 2021

*Senior DevOps Engineer* · Hybrid · July 2015 to June 2020

*Application Developer* · On-Site · 03/2015 – 2015-06

## Certifications

| **SSCE** (SaltStack Certified Engineer) | Mar 2015 |

Obtained Developer status in 2009 after maintaining packages.

Boundary dates: February 2022, January 2022, February 2017, January 2017.

Presented at Presentations about CIS Level 2 and TLS 1.2.
'''


class TestDates:
    '''Tests against a filtered document carrying dates and ranges.'''
    result = None

    def setup_method(self):
        '''Send document through filters.'''
        self.result = cvclean.filters.dates.apply(DATE_DOCUMENT, REFERENCE)

    def test_open_range_ends_at_the_reference_month(self):
        '''Check that 'Present' resolves and the final month counts.'''
        assert '· [datespan28mo-under5yr]' in self.result

    def test_span_length_counts_both_endpoints(self):
        '''Check that a range reports an inclusive month count.'''
        assert '[datespan25mo-under5yr]' in self.result
        assert '[datespan14mo-over5yr]' in self.result
        assert '[datespan60mo-over5yr]' in self.result

    def test_every_separator_delimits_a_range(self):
        '''Check that hyphen, dashes and 'to' all yield one span.'''
        assert '2022 - May' not in self.result
        assert '2020 — August' not in self.result
        assert '2015 to June' not in self.result

    def test_numeric_months_resolve(self):
        '''Check that a slashed and a dashed date make one range.'''
        assert '[datespan4mo-over10yr]' in self.result

    def test_abbreviated_month_resolves(self):
        '''Check that a three-letter month is read as a date.'''
        assert '| [date-over10yr] |' in self.result

    def test_year_without_month_reads_as_december(self):
        '''Check that a bare year is dated to the end of that year.'''
        assert 'status in [date-over10yr] after' in self.result

    def test_decay_steps_at_sixty_and_one_hundred_twenty_months(self):
        '''Check both decay boundaries from either side.'''
        assert ('Boundary dates: [date-under5yr], '
                '[date-over5yr], [date-over5yr], '
                '[date-over10yr].') in self.result

    def test_date_like_words_survive(self):
        '''Check that words resembling a date are not redacted.'''
        assert 'Presented at Presentations' in self.result
        assert 'CIS Level 2' in self.result
        assert 'TLS 1.2' in self.result

    def test_headings_survive(self):
        '''Check that this filter touches nothing but dates.'''
        assert '## Professional Experience' in self.result
        assert '**SSCE** (SaltStack Certified Engineer)' in self.result
