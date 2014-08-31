from __future__ import absolute_import

import inspect
import sure
from ..func_util import *


def test_set_function_defaults():
    def f(a, b='x', c='x', d='x'):
        return (a, b, c, d)
    set_function_defaults(f, ('c', 'd'))
    (lambda: f(1)).should.throw(Exception)
    f(1, 2).should.equal((1, 2, 'c', 'd'))


def test_argspec_drop_right():

    def f(a, b, c=None):
        pass

    def g(a):
        pass

    argspec_drop_right(2, inspect.getargspec(f)) \
        .should.equal(inspect.getargspec(g))


def test_argspec_append_left():

    def f(a, b=None):
        pass

    def g(x, y, a, b=None):
        pass

    argspec_append_left(['x', 'y'], inspect.getargspec(f)) \
        .should.equal(inspect.getargspec(g))


def test_if_not_none():
    f = if_not_none(lambda x: x * 2 + 1)
    f(7).should.equal(15)
    f(0).should.equal(1)
    f(None).should.equal(None)
