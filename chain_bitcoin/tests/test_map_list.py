from __future__ import absolute_import

import sure
from .. import ChainError
from ..map_list import map_list


def test_map_list():
    map_list(lambda x: x + 1, [1, 2, 3]).should.equal([2, 3, 4])


def test_map_list_on_dict():
    (lambda: map_list(lambda x: x + 1, {1: 2})).should.throw(ChainError)


def test_map_list_on_string():
    (lambda: map_list(lambda x: x + 1, '123')).should.throw(ChainError)
