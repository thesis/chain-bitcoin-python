from __future__ import absolute_import

import sure
from .. import Chain, NoApiKeyId, OpReturn, get_transaction_op_return
from .mock_http_adapter import *


def test_get_transaction_op_return():
    get_transaction_op_return(transaction_hash, api_key_id=api_key_id,
                              http_adapter=http_adapter) \
        .should.equal(op_return)


def test_get_transaction_op_return_using_class():
    Chain(api_key_id=api_key_id, http_adapter=http_adapter) \
        .get_transaction_op_return(transaction_hash).should.equal(op_return)


def test_get_transaction_op_return_without_api_key_id():
    (lambda: get_transaction_op_return(transaction_hash, http_adapter=no_http())) \
        .should.throw(NoApiKeyId)


transaction_hash = '4a7d62a4a5cc912605c46c6a6ef6c4af451255a453e6cbf2b1022766c331f803'

api_key_id = 'DEMO-4a5e1e4'

url = 'https://api.chain.com/v1/bitcoin/transactions/' \
      '4a7d62a4a5cc912605c46c6a6ef6c4af451255a453e6cbf2b1022766c331f803' \
      '/op-return?api-key-id=DEMO-4a5e1e4'

response_body = """
{
  "transaction_hash": "4a7d62a4a5cc912605c46c6a6ef6c4af451255a453e6cbf2b1022766c331f803",
  "hex": "436861696e2e636f6d202d2054686520426c6f636b20436861696e20415049",
  "text": "Chain.com - The Block Chain API",
  "receiver_addresses": [
    "1Bj5UVzWQ84iBCUiy5eQ1NEfWfJ4a3yKG1"
  ],
  "sender_addresses": [
    "1Bj5UVzWQ84iBCUiy5eQ1NEfWfJ4a3yKG1"
  ]
}
"""

op_return = OpReturn(
    transaction_hash='4a7d62a4a5cc912605c46c6a6ef6c4af451255a453e6cbf2b1022766c331f803',
    hex='436861696e2e636f6d202d2054686520426c6f636b20436861696e20415049',
    text='Chain.com - The Block Chain API',
    receiver_addresses=['1Bj5UVzWQ84iBCUiy5eQ1NEfWfJ4a3yKG1'],
    sender_addresses=['1Bj5UVzWQ84iBCUiy5eQ1NEfWfJ4a3yKG1'],
)

http_adapter = mock_get(url, response_body)
