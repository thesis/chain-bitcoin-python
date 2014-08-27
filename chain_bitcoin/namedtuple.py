from __future__ import absolute_import

__all__ = ('namedtuple', 'namedtuple_to_dict', 'dict_field_map')

import collections
import functools
import json
import types

from .exceptions import *
from .func_util import set_function_defaults


def namedtuple(name, args=None, field_map=None):
    """
    A class constructor similar to ``collections.namedtuple``.

    Arguments:

        args: list of strings

        field_map: (string, a) -> Maybe (string, b)
        Modifies the behavior of ``from_dict``.

    Differences from ``collections.namedtuple``:

        All parameters to ``__new__`` have a default value of ``None``.

        ``_replace`` is aliased as ``replace`` because it shouldn't be
        considered a private method.

        There is a class method ``from_dict`` which converts a ``dict``
        to an instance of the ``namedtuple`` class.

        ``args`` must be a list of strings.
    """

    tuple_type = collections.namedtuple(name, list(args or []))

    set_function_defaults(tuple_type.__new__, [None] * len(args))

    tuple_type.replace = tuple_type._replace

    def from_dict(cls, x):
        return namedtuple_from_dict(cls, field_map, x)
    tuple_type.from_dict = classmethod(from_dict)

    return tuple_type


def namedtuple_from_dict(tuple_type, field_map, x):

    from . import models

    def transform_item(item):
        (k, v) = item
        return field_map(k, v)

    if field_map is not None:
        x = dict(filter(None, map(transform_item, x.items())))

    try:
        return tuple_type(**x)
    except TypeError:
        raise ChainError("{name} doesn't fit the data {data}".format(
            name=tuple_type.__name__, data=json.dumps(x)))


def dict_field_map(x):
    def f(k, v):
        return (k, x[k](v)) if k in x else (k, v)
    return f


def namedtuple_to_dict(tup):
    return dict((s, getattr(tup, s)) for s in tup._fields)
