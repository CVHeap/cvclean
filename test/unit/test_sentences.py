'''
Tests that ensure phrases carrying identity are removed and plain ones stay.
'''
# CV Heap
import cvclean.filters.sentences


# Test document with identifying phrases beside descriptive ones
SENTENCE_DOCUMENT = '''## Professional Experience

I was the only Linux Administrator in the nation's largest provider.

I was hired as a Site Reliability Engineer on the Database Operations team.

Support was handed off to internal IT teams for ongoing maintenance.

## Volunteer Experience

- Mentored individuals in recovery, walking them through sobriety
- Presented my personal story about addiction and recovery

## Open Source Contributions

I was voted into the Ubuntu Community Membership team.

- Contributed content and reviews for the Ubuntu News and Website teams
- Joined "ftpteam", reviewing packages to ensure standards are maintained
- Assisted in development of infrastructure for Local Community teams
- I participated in various teams across the project
'''


class TestSentences:
    '''Tests against a filtered document of contextual phrases.'''
    result = None

    def setup_method(self):
        '''Send document through filters.'''
        self.result = cvclean.filters.sentences.apply(SENTENCE_DOCUMENT)

    def test_ranking_phrase_is_removed(self):
        '''Check that a ranking leaves its article behind.'''
        assert 'in the [redacted-pii] provider.' in self.result
        assert "nation's largest" not in self.result

    def test_internal_team_is_removed(self):
        '''Check that a team the subject belonged to is a name.'''
        assert 'on the [redacted-pii] team.' in self.result
        assert 'Database Operations' not in self.result

    def test_membership_programme_absorbs_the_project_name(self):
        '''Check that the longest phrase wins at a shared start.'''
        assert 'into the [redacted-pii] team.' in self.result
        assert 'Ubuntu Community Membership' not in self.result

    def test_team_names_leave_the_project_name(self):
        '''Check that a span not starting at the project keeps it.'''
        assert 'for the Ubuntu [redacted-pii] teams' in self.result

    def test_first_person_health_bullet_is_removed_whole(self):
        '''Check that an account of addiction leaves no remnant.'''
        assert '- [redacted-pii]\n' in self.result
        assert 'addiction' not in self.result

    def test_membership_language_alone_is_not_enough(self):
        '''Check that a public team survives a joining verb.'''
        assert 'Joined "ftpteam"' in self.result

    def test_title_case_alone_is_not_enough(self):
        '''Check that a public community structure survives.'''
        assert 'Local Community teams' in self.result

    def test_groups_described_by_what_they_do_survive(self):
        '''Check that an unnamed counterpart group remains.'''
        assert 'internal IT teams' in self.result
        assert 'various teams across the project' in self.result

    def test_superlative_about_the_subject_survives(self):
        '''Check that the subject's own seniority remains.'''
        assert 'the only Linux Administrator' in self.result

    def test_unrelated_bullet_survives(self):
        '''Check that mentoring is not treated as a health account.'''
        assert '- Mentored individuals in recovery' in self.result
