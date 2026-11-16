Sanitization Rules
==================

**Overview:**

1. Any PII/PHI
2. Mask dates and date ranges (<5yr, >10yr)
3. Company names (employed vs. named)
4. Non-employment organizations (redacted throughout localized section)
5. Reduce all numbers to two significant digits

Tokens
------

Replace every occurrence of what a token stands for, including inside a
bracketed aside, a list of names, or a longer name built around it. A single
occurrence left in place identifies the token everywhere it is used.

Every redaction is replaced with a bracketed token:

- ``[pii]`` - anything under rule 1 with no token of its own
- ``[employerN]`` - an organization the subject worked with (for or at)
- ``[altorgN]`` - an organization named without having been worked for
- ``[locationN]`` - a city, region or country
- ``[schoolN]`` - an educational institution
- ``[productN]`` - a product or service belonging to an employer
- ``[date-<decay>]`` - a single date
- ``[datespanNNmo-<decay>]`` - a date range

``N`` is assigned in order of first appearance. One entity holds one token
throughout the document, and no two entities share a token.

``decay`` is one of ``under5yr``, ``over5yr`` or ``over10yr``, measured from
the most recent date provided. This is further defined by **Rule 2**.

Rule Definitions
----------------

**Rule 1, removed** - PII/PHI covers the subject's name, contact details,
profile links, addresses and record identifiers, and also:

- a sentence in which the subject describes their own health, addiction,
  recovery or disability
- the title of a presentation or publication by the subject, which identifies
  its author
- the name of an internal team, department or program the subject belonged
  to, which places them inside an employer's structure
- a product or service belonging to an employer
- a ranking phrase ("the nation's largest") attached to an organization

**Rule 1, kept** - context that carries no identity:

- job titles and seniority
- certification and credential names
- standards, regulations and benchmarks
- third-party technologies, tools and vendors the subject used
- a counterpart group described by what it does rather than by name
- the name of a team the subject worked with rather than belonged to
- a superlative describing the subject's own role or work

**Rule 2** - a date keeps a decay hint, measured against the reference date the
document is sanitized on:

- ``under5yr`` - ended less than 60 months before the reference date
- ``over5yr`` - ended 60 to 119 months before
- ``over10yr`` - ended 120 months or more before
- ``NN`` - the length of a range in months, counting both the first month and
  the last
- an open range ends at the reference month, and that month counts
- a year given without a month is read as that year's December

**Rule 3** - an organization the subject worked for or at is employed, and
takes ``[employerN]``; one that is only named takes ``[altorgN]``:

- a staffing agency and the client it placed the subject with are both employed
- a brand, parent company, conference, volunteer organization or open source
  project is named
- a third-party organization is named where the subject held a role in it or
  collaborated with it
- a third-party name that appears only as a tool, product or platform the
  subject used is not an organization reference, and stays
- one name can denote two entities, such as a parent and a brand, and each
  keeps its own token, deliberately not linked to the other

**Rule 4** - a non-employment organization is redacted throughout its localized
section, the section that documents or names it, and left alone elsewhere,
where it reads as a technology or a tool:

- the name, its short form, and any run of its distinctive words are all
  redacted there
- a heading that names the organization is redacted whole, less any trailing
  phrase the section body defines in a sentence of its own
- in body text only the name and runs of its distinctive words match, so an
  adjacent word naming an industry, technology or legal form (``Linux``,
  ``web server``, ``repositories``) stays
- matching is case-sensitive, so a lowercase descriptor is never absorbed

**Rule 5** - every number keeps two significant digits, preserving separators
and decimal width:

- the month count inside a date token is generated metadata, and is not reduced
- includes version strings
