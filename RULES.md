Sanitization Rules
==================

**Overview:**

1. Remove anything that identifies the subject (PII/PHI)
2. Remove anything that reveals a protected class, while keeping the work
3. Tokenize organizations, people and products, and remove places
4. Collapse dates into durations and decay hints
5. Remove version numbers, then reduce every other number to two significant
   digits

The goal is text that shows what the subject did without showing who they are.
A capitalized word or phrase inside a sentence that is not on the product
list and is not a name already known from the headings is treated as a name,
and replaced with ``[pii]``. ``[pii]`` is the same in every journal and
carries no gender or origin, so a wrong guess costs a word of evidence rather
than adding a bias. How much evidence this removes is measured by the
evidence-loss test in the scorecard spec.

Input
-----

- A document can arrive with LF or CRLF line endings. Both give the same
  output. The checksum is verified on the raw bytes first, and line endings
  are normalized after that.
- Section names are matched without regard to case or trailing whitespace, so
  a renamed or reformatted section is still found.
- The reference date for every decay hint is the submission date, passed in
  with the document. The same document always gives the same output.

Tokens
------

Every redaction is replaced with a bracketed token:

- ``[pii]`` - anything under rule 1 with no token of its own
- ``[person-<id>]`` - a person other than the subject, such as a manager or
  client
- ``[employer-<id>]`` - an organization the subject worked with (for or at)
- ``[altorg-<id>]`` - an organization named without having been worked for
- ``[school-<id>]`` - an educational institution
- ``[product-<id>]`` - a product or service belonging to an employer
- ``[date-<decay>]`` - a single date
- ``[datespanNNmo-<decay>]`` - a date range

``<id>`` is four characters from ``[a-z0-9]``, drawn at random with the
document's checksum as the seed. The ids carry no order, so they do not show
how many entities came before, and the same document always gets the same
ids, so tests stay repeatable. One entity holds one id throughout the
document, and no two entities share an id; a draw that repeats an id is drawn
again. The ids mean nothing outside the document they came from. Replace every
occurrence of what a token stands for, including inside a bracketed aside, a
list of names, or a longer name built around it. A single occurrence left in
place identifies the token everywhere it is used.

``decay`` is one of ``under5yr``, ``over5yr`` or ``over10yr``. Decay hints stay
in the cleaned text. The scorecard strips them as the first step of splitting
spans, so the smallest-unit prompts (one span, one bucket) never see them,
while the position-level questions that come later can use them.

Rule Definitions
----------------

**Rule 1, removed** - anything that identifies the subject:

- the subject's name, contact details, profile links, addresses and record
  identifiers, such as certification or license numbers
- email addresses, phone numbers with or without a country code, and bare
  URLs or domains, as well as Markdown links
- locations, such as a city, region or country, in a heading or in the text
- job titles and seniority words such as "Senior" or "Lead". The search filter
  handles titles, and the level comes from what the text says was done
- the name of an internal team, department or program the subject belonged
  to, which places them inside an employer's structure
- a ranking or news phrase that points at one organization, such as "the
  nation's largest" or "a cyberattack that made national news"
- a detail distinctive enough to find the subject on its own, such as a unique
  role in a public project

**Rule 1, replaced with a label** - details that are also evidence:

- the title of a presentation or publication by the subject is replaced with
  a fixed label taken from the section it sits in, ``a conference talk`` or
  ``a publication``. The label shows that the work exists and keeps nothing
  from the title, and no model writes it

**Rule 1, kept** - context that carries no identity:

- certification and credential names, without their identifiers
- standards, regulations and benchmarks
- third-party technologies, tools and vendors the subject used. These are
  matched against a maintained product list first, so a tool name such as
  Jenkins or Kafka is never taken for a person or an organization
- a counterpart group described by what it does rather than by name
- the name of a team the subject worked with rather than belonged to
- a superlative describing the subject's own role or work

**Rule 2** - protected classes are removed, and the text must not allow them
to be inferred. They include:

- age
- health, addiction, recovery and disability
- religion
- parental status
- sex and gender
- race, ethnicity and national origin

Wording that points at one of them is removed too:

- stated ages and year counts, such as "20 years of experience"
- types of leave, pronouns and affinity groups
- phrases such as "native speaker"

A language itself is a skill and is kept.

When the class is part of the work itself, the work stays and only the
affiliation goes. Volunteer work at a recovery center keeps what the subject
did, such as "peer support" or "community outreach", while the description of
the organization and any wording that ties the subject to the condition are
removed. A sentence in which the subject describes their own protected detail
is removed whole.

**Rule 3** - an organization the subject worked for or at is employed, and
takes ``[employer-<id>]``; one that is only named takes ``[altorg-<id>]``:

- a staffing agency and the client it placed the subject with are both
  employed. Which placement belongs to which agency is resolved before dates
  are replaced, from "via" qualifiers in the headings and from overlapping
  date ranges, and the result is kept as a nesting relationship
- a brand, parent company, conference, volunteer organization or open source
  project is named
- a third-party organization is named where the subject held a role in it or
  collaborated with it
- a third-party name that appears only as a tool, product or platform the
  subject used is not an organization reference, and stays
- one name can denote two entities, such as a parent and a brand, and each
  keeps its own token, deliberately not linked to the other

A non-employment organization is redacted throughout its localized section,
the section that documents or names it, and left alone elsewhere, where it
reads as a technology or a tool:

- the name, its short form, and any run of its distinctive words are all
  redacted there
- a heading that names the organization is redacted whole, less any trailing
  phrase the section body defines in a sentence of its own
- in body text only the name and runs of its distinctive words match, so an
  adjacent word naming an industry, technology or legal form (``Linux``,
  ``web server``, ``repositories``) stays
- matching is case-sensitive, so a lowercase descriptor is never absorbed

**Rule 4** - dates become durations and decay hints, measured against the
submission date:

- ``under5yr`` - ended less than 60 months before the reference date
- ``over5yr`` - ended 60 to 119 months before
- ``over10yr`` - ended 120 months or more before
- ``NN`` - the length of a range in months, counting both the first month and
  the last
- an open range ends at the reference month, and that month counts
- a year given without a month is read as that year's December
- a four-digit number is a date only when it is part of a range, follows a
  month name, or sits in an entry heading. Elsewhere it is a number, so
  "managed 2000 servers" stays a count
- degrees keep their duration but no decay hint, because the years since
  graduation are a direct stand-in for age

**Rule 5** - numbers:

- version numbers are handled first, by their own filter, and removed:
  "Python 3.11" becomes "Python". A version dates the work, and the oldest one
  in a journal points at when the career started
- every other number keeps two significant digits, preserving separators and
  decimal width
- the month count inside a date token is generated metadata, and is not
  reduced
