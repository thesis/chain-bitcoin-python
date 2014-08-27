from __future__ import absolute_import

__all__ = ('make_url', 'make_query_string')

try:
    from urllib.parse import urlencode  # python 3
except ImportError:
    from urllib import urlencode  # python 2

import re

path_component_regex = re.compile(r'^[0-9a-z_\-,]+$', re.I)


def make_url(base, path_components, query_params=None):

    for c in path_components:
        if not path_component_regex.match(c):
            raise ValueError('Invalid character in "{0}"'.format(c))

    return '?'.join(filter(None, [
        '/'.join([base] + path_components),
        make_query_string(query_params),
    ]))


def make_query_string(query_params):
    query_params = filter(lambda p: p[1] is not None, query_params or [])
    return '&'.join(map(url_encode_tuple, query_params))


def url_encode_tuple(tup):
    return urlencode(dict([tup]))
