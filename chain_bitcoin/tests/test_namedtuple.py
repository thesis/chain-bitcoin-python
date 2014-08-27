from __future__ import absolute_import

import sure
from ..exceptions import *
from ..namedtuple import *


def test_namedtuple_param_defaults():
    Foo = namedtuple('Foo', ('a', 'b'))
    Foo().should.equal(Foo(None, None))
    Foo().should.equal(Foo(None))
    Foo().should.equal(Foo(b=None))


def test_namedtuple_replace():
    Foo = namedtuple('Foo', ('a', 'b'))
    Foo('x', 'y').replace(b='z').should.equal(Foo('x', 'z'))


def test_from_dict():
    Foo = namedtuple('Foo', ('a', 'b'))
    Foo.from_dict({'a': 1, 'b': 2}).should.equal(Foo(1, 2))


def test_from_dict_with_missing_key():
    Foo = namedtuple('Foo', ('a', 'b'))
    Foo.from_dict({'a': 1}).should.equal(Foo(a=1))


def test_from_dict_with_bad_key():
    Foo = namedtuple('Foo', ('a', 'b'))
    (lambda: Foo.from_dict({'a': 1, 'b': 2, 'c': 3})).should.throw(ChainError)


def test_from_dict_with_subclass():
    class Foo(namedtuple('Foo', ('a', 'b'))):
        pass
    Foo.from_dict({'a': 1, 'b': 2}).should.equal(Foo(1, 2))


def test_dict_field_map():
    field_map = dict_field_map({'b': lambda x: x + 1})
    Foo = namedtuple('Foo', ('a', 'b'), field_map=field_map)
    Foo.from_dict({'a': 1, 'b': 2}).should.equal(Foo(1, 3))


def test_key_transforming_field_map():
    def field_map(k, v):
        return (k[0], v)
    Foo = namedtuple('Foo', ('a', 'b'), field_map=field_map)
    Foo.from_dict({'apple': 1, 'banana': 2}).should.equal(Foo(1, 2))


def test_filtering_field_map():
    def field_map(k, v):
        if k in ('a', 'b'):
            return (k, v)
    Foo = namedtuple('Foo', ('a', 'b'), field_map=field_map)
    Foo.from_dict({'a': 1, 'b': 2, 'c': 3}).should.equal(Foo(1, 2))
