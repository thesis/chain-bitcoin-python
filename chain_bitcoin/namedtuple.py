from __future__ import absolute_import

__all__ = (
    'namedtuple', 'namedtuple_to_dict', 'transform_item', 'remove_item'
)

import logging
logger = logging.getLogger('chain_bitcoin')

import collections
import functools
import json
import types

from .exceptions import *
from .func_util import set_function_defaults


def namedtuple(name, args=None, alter_dict=None):
    """
    A class constructor similar to ``collections.namedtuple``.

    Arguments:

        args: list of strings

        alter_dict: map from dict to dict
        Modifies the behavior of ``from_dict``.

    Differences from ``collections.namedtuple``:

        All parameters to ``__new__`` have a default value of ``None``.

        ``_replace`` is aliased as ``replace`` because it shouldn't be
        considered a private method.

        There is a class method ``from_dict`` which converts a ``dict``
        to an instance of the ``namedtuple`` class.

        ``args`` must be a list of strings.
    """

    args = list(args or [])

    tuple_type = collections.namedtuple(name, args)

    set_function_defaults(tuple_type.__new__, [None] * len(args))

    tuple_type.replace = tuple_type._replace

    def from_dict(cls, x):
        return namedtuple_from_dict(cls, alter_dict(x) if alter_dict else x)
    tuple_type.from_dict = classmethod(from_dict)

    return tuple_type


def namedtuple_from_dict(tuple_type, x):

    # Remove keys that aren't fields, and log a warning.
    bad_keys = list(k for k in x if k not in tuple_type._fields)
    if len(bad_keys) != 0:
        logger.warning('Keys not applicable to {name}: {keys}\n{x}'.format(
            name=tuple_type.__name__,
            keys=', '.join(bad_keys),
            x=str(x),
        ))
        x = dict((k, x[k]) for k in x if k not in bad_keys)

    return tuple_type(**x)


def transform_item(k, f):
    def t(x):
        x = dict(x)
        if k in x:
            x[k] = f(x[k])
        return x
    return t


def remove_item(k):
    def t(x):
        if k in x:
            x = dict(x)
            del x[k]
        return x
    return t


def namedtuple_to_dict(tup):
    return dict((s, getattr(tup, s)) for s in tup._fields)
