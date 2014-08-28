from __future__ import absolute_import

import sure
from .. import Chain, NoApiKeyId, Address, get_address
from .mock_http_adapter import *


def test_get_address():
    get_address(address_id, api_key_id=api_key_id,
                http_adapter=http_adapter) \
        .should.equal(address)


def test_get_address_using_class():
    Chain(api_key_id=api_key_id, http_adapter=http_adapter) \
        .get_address(address_id) \
        .should.equal(address)


def test_get_address_without_api_key_id():
    (lambda: get_address(address_id, http_adapter=no_http())) \
        .should.throw(NoApiKeyId)


address_id = '17x23dNjXJLzGMev6R63uyRhMWP1VHawKc'

api_key_id = 'DEMO-4a5e1e4'

url = 'https://api.chain.com/v1/bitcoin/addresses/' \
      '17x23dNjXJLzGMev6R63uyRhMWP1VHawKc?api-key-id=DEMO-4a5e1e4'

response_body = """
{
  "hash": "17x23dNjXJLzGMev6R63uyRhMWP1VHawKc",
  "balance": 5000000000,
  "received": 5000000000,
  "sent": 0,
  "unconfirmed_received": 0,
  "unconfirmed_sent": 0,
  "unconfirmed_balance": 0
}
"""

address = Address(
    hash='17x23dNjXJLzGMev6R63uyRhMWP1VHawKc',
    balance=5000000000,
    received=5000000000,
    sent=0,
    unconfirmed_received=0,
    unconfirmed_sent=0,
    unconfirmed_balance=0,
)

http_adapter = mock_get(url, response_body)
