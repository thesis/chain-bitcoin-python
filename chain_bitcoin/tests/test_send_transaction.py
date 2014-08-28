from __future__ import absolute_import

import sure
from .. import Chain, NoApiKeyId, NoApiKeySecret, SendTransactionResult, \
    send_transaction
from .mock_http_adapter import *


def test_send_transaction():
    send_transaction(hex, api_key_id=api_key_id, api_key_secret=api_key_secret,
                     http_adapter=http_adapter) \
        .should.equal(result)


def test_send_transaction_using_class():
    Chain(api_key_id=api_key_id, api_key_secret=api_key_secret,
          http_adapter=http_adapter) \
        .send_transaction(hex).should.equal(result)


def test_send_transaction_without_api_key_id():
    (lambda: send_transaction(hex=hex, http_adapter=no_http())) \
        .should.throw(NoApiKeyId)


def test_send_transaction_without_api_key_secret():
    (lambda: send_transaction(hex=hex, api_key_id=api_key_id,
                              http_adapter=no_http())) \
        .should.throw(NoApiKeySecret)


hex = '0100000001ec...'

api_key_id = 'DEMO-4a5e1e4'

api_key_secret = 'DEMO-f8aef80',

url = 'https://api.chain.com/v1/bitcoin/transactions'

request_json = """
{
  "hex": "0100000001ec..."
}
"""

response_body = """
{
  "hash": "1Jdbaiv..."
}
"""

result = SendTransactionResult(
    hash='1Jdbaiv...'
)

http_adapter = mock_put_json(url, request_json, response_body)
