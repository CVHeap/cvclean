'''
CV Clean

Copyright: 2026, CV Heap LLC.
See LICENSE.txt for details.
'''
import importlib


# All supported and enabled filters, in the order they are applied
ALL_FILTERS = [
    'names',
]


def apply_filters(blob):
    '''
    Return a text object with all filters applied.
    '''
    for filter_name in ALL_FILTERS:
        fltr = importlib.import_module(f'cvclean.filters.{filter_name}')
        blob = fltr.apply(blob)
    return blob
