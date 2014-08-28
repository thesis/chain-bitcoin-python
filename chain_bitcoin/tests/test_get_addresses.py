from __future__ import absolute_import

import sure
from .. import Chain, NoApiKeyId, Address, get_addresses
from .mock_http_adapter import *


def test_get_addresses():
    get_addresses(address_ids, api_key_id='DEMO-4a5e1e4',
                  http_adapter=http_adapter) \
        .should.equal(addresses)


def test_get_addresses_using_class():
    Chain(api_key_id=api_key_id, http_adapter=http_adapter) \
        .get_addresses(address_ids).should.equal(addresses)


def test_get_addresses_without_api_key_id():
    (lambda: get_addresses(address_ids, http_adapter=no_http())) \
        .should.throw(NoApiKeyId)


address_ids = ['17x23dNjXJLzGMev6R63uyRhMWP1VHawKc',
                  '3WWTV4tw5etd54erhv348ncERVInmervnu']

api_key_id = 'DEMO-4a5e1e4'

url = 'https://api.chain.com/v1/bitcoin/addresses/' \
      '17x23dNjXJLzGMev6R63uyRhMWP1VHawKc,' \
      '3WWTV4tw5etd54erhv348ncERVInmervnu?api-key-id=DEMO-4a5e1e4'

response_body = """
[{
  "hash": "17x23dNjXJLzGMev6R63uyRhMWP1VHawKc",
  "balance": 5000000000,
  "received": 5000000000,
  "sent": 0,
  "unconfirmed_received": 0,
  "unconfirmed_sent": 0,
  "unconfirmed_balance": 0
},{
  "hash": "3WWTV4tw5etd54erhv348ncERVInmervnu",
  "balance": 6700000000,
  "received": 6800000000,
  "sent": 50000000,
  "unconfirmed_received": 42000000,
  "unconfirmed_sent": 311000000,
  "unconfirmed_balance": 12000000
}]
"""

addresses = [
    Address(
        hash='17x23dNjXJLzGMev6R63uyRhMWP1VHawKc',
        balance=5000000000,
        received=5000000000,
        sent=0,
        unconfirmed_received=0,
        unconfirmed_sent=0,
        unconfirmed_balance=0,
    ),
    Address(
        hash='3WWTV4tw5etd54erhv348ncERVInmervnu',
        balance=6700000000,
        received=6800000000,
        sent=50000000,
        unconfirmed_received=42000000,
        unconfirmed_sent=311000000,
        unconfirmed_balance=12000000,
    ),
]

http_adapter = mock_get(url, response_body)
