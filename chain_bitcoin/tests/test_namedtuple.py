from __future__ import absolute_import

import sure
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
    Foo.from_dict({'a': 1, 'b': 2, 'c': 3}).should.equal(Foo(1, 2))


def test_from_dict_with_subclass():
    class Foo(namedtuple('Foo', ('a', 'b'))):
        pass
    Foo.from_dict({'a': 1, 'b': 2}).should.equal(Foo(1, 2))


def test_transform_item():
    alter_dict = transform_item('b', lambda x: x + 1)
    Foo = namedtuple('Foo', ('a', 'b'), alter_dict=alter_dict)
    Foo.from_dict({'a': 1, 'b': 2}).should.equal(Foo(1, 3))


def test_remove_item():
    alter_dict = remove_item('b')
    Foo = namedtuple('Foo', ('a', 'b'), alter_dict=alter_dict)
    Foo.from_dict({'a': 1, 'b': 2}).should.equal(Foo(1, None))
