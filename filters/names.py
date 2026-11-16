'''
CV Clean: Filter for Names
'''


def apply(blob):
    '''
    Remove people and company names.
    '''
    return blob.lower().replace('fred flinstone', '').replace(
            'dino,', ',').replace('barney', '').replace(
                    'rubble industries', '')
