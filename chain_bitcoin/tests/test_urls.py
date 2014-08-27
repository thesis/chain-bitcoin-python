from __future__ import absolute_import

import sure
from ..urls import *


def test_make_query_string():
    make_query_string([('ghi', None), ('jkl', 42)]).should.equal('jkl=42')


def test_make_url():
    make_url('https://localhost',
             ['abc', 'def'],
             [('ghi', None), ('jkl', 42)]) \
        .should.equal('https://localhost/abc/def?jkl=42')


def test_make_url_with_bad_character():
    (lambda: make_url('https://localhost', ['abc', '../secrets'])) \
        .should.throw(ValueError)
