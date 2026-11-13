'''
CV Clean

Copyright: 2026, CV Heap LLC.
See LICENSE.txt for details.
'''
import cvclean.filters


def apply_filters(blob):
    '''
    Return a text object with all filters applied.
    '''
    # Run input blob through every filter
    for filter_name in cvclean.filters.ALL:
        blob = getattr(cvclean.filters, filter_name)(blob)

    # Return final result
    return blob
