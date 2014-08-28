from __future__ import absolute_import

__all__ = ('map_list',)

from .exceptions import *


def map_list(f, xs):
    """
    Use ``f`` to transform each element of ``xs`` if ``xs`` is a list.
    Raise ``ChainError`` if ``xs`` is not a list.
    """
    if not isinstance(xs, list):
        raise ChainError('Expected list, got "{0}"'.format(xs))
    return list(map(f, xs))
