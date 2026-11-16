'''
CV Clean: Filter for Contacts
'''
import re
import phonenumbers


# Inline Markdown link, label and target together
LINK = re.compile(r'\[[^\]]*\]\([^)]*\)')

# Email address, matched by shape rather than deliverability
EMAIL = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')


def apply(blob):
    '''
    Remove contact details, profile links and record identifiers.
    '''
    blob = LINK.sub('[pii]', blob)
    blob = EMAIL.sub('[pii]', blob)
    matches = phonenumbers.PhoneNumberMatcher(blob, None)
    for match in reversed(list(matches)):
        blob = blob[:match.start] + '[pii]' + blob[match.end:]
    return blob
