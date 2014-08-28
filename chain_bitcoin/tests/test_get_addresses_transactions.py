from __future__ import absolute_import

import sure
from .. import Chain, NoApiKeyId, Transaction, get_addresses_transactions
from .mock_http_adapter import *


def test_get_addresses_transactions():
    get_addresses_transactions(address_ids, limit=2, api_key_id=api_key_id,
                               http_adapter=http_adapter) \
        .should.equal(transactions)


def test_get_addresses_transactions_using_class():
    Chain(api_key_id=api_key_id, http_adapter=http_adapter) \
        .get_addresses_transactions(address_ids, limit=2) \
        .should.equal(transactions)


def test_get_addresses_transactions_without_api_key_id():
    (lambda: get_addresses_transactions(address_ids, limit=2,
                                        http_adapter=no_http())) \
        .should.throw(NoApiKeyId)


address_ids = ['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb',
                  '1EX1E9n3bPA1zGKDV5iHY2MnM7n5tDfnfH']

api_key_id = 'DEMO-4a5e1e4'

url = 'https://api.chain.com/v1/bitcoin/addresses/' \
      '1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb,' \
      '1EX1E9n3bPA1zGKDV5iHY2MnM7n5tDfnfH' \
      '/transactions?limit=2&api-key-id=DEMO-4a5e1e4'

response_body = """
[
    {
        "hash": "0bf0de38c26195919179f42d475beb7a6b15258c38b57236afdd60a07eddd2cc",
        "block_hash": "00000000000000001ea5471a4edc67380f114c6cad06bfd59ac6508f90e8b252",
        "block_height": 303404,
        "block_time": "2014-05-30T23:54:55Z",
        "confirmations": 8758,
        "inputs": [
            {
                "transaction_hash": "0bf0de38c26195919179f42d475beb7a6b15258c38b57236afdd60a07eddd2cc",
                "output_hash": "b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf",
                "output_index": 0,
                "value": 300000,
                "addresses": [
                    "3L7dKYQGNoZub928CJ8NC2WfrM8U8GGBjr"
                ],
                "script_signature": "0 3046022100de7b67b96a6855fbc81c1a4b45d98ba6fef27ddda8739c5a3e7c70039685f7db0221008972607445195847631d902f594db6d712c315e0d49a2bee98125af8e1fefb5701 304402200cc13d8859247bff4ab4bc70964955fa4dbcd1a0dff0a84896be7d9a7757516202206e2c6c0aec6527ccf30305ad6e242c973aad011e9ccc18a0b75fd7be6c9b675301 5221032071a66eaed3dbe31a982dc337108b28bcffbf88d8cac8975194e184abdb36662102134541ec8f3dc2d382646bad199526a64080a66d27d2e156906bdb822774283921020431faa475c966c752e6cf97dfbb2c68c98b0013ca5c76b860263438850c2ba053ae"
            }
        ],
        "outputs": [
            {
                "transaction_hash": "0bf0de38c26195919179f42d475beb7a6b15258c38b57236afdd60a07eddd2cc",
                "output_index": 0,
                "value": 290000,
                "addresses": [
                    "1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb"
                ],
                "script": "OP_DUP OP_HASH160 c629680b8d13ca7a4b7d196360186d05658da6db OP_EQUALVERIFY OP_CHECKSIG",
                "script_hex": "76a914c629680b8d13ca7a4b7d196360186d05658da6db88ac",
                "script_type": "pubkeyhash",
                "required_signatures": 1,
                "spent": false
            }
        ],
        "fees": 10000,
        "amount": 290000
    },
    {
        "hash": "b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf",
        "block_hash": "0000000000000000577344f05b6ea721b95fa629e0c3b16cdd929cbdf20f862f",
        "block_height": 303402,
        "block_time": "2014-05-30T23:38:24Z",
        "confirmations": 8760,
        "inputs": [
            {
                "transaction_hash": "b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf",
                "output_hash": "027bd765dc335ecc37a571d4d8b7cd4ab802e1eb50e91b3e7e9c6689861609e7",
                "output_index": 1,
                "value": 252000,
                "addresses": [
                    "1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb"
                ],
                "script_signature": "3045022100c239e879cde489f2a51ceb16e02806340ca90da07c8c8442620229b7a687afbb022020c08b3a32159ae1fee6dc4f1d1a5edb0613299844622721cefb3e0049e4ee0c01 037bd486bb4f0f4ffe9e39f213879fc5b85c00df0194a97da7169589ad9bb3ce84"
            },
            {
                "transaction_hash": "b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf",
                "output_hash": "3ae7d2a0b8d6574d2217f3f9b6a205e564b6e34da772d6182e91e2fdbb6eac35",
                "output_index": 0,
                "value": 90000,
                "addresses": [
                    "1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb"
                ],
                "script_signature": "30450221008eec802d9f07f18cfa5677675e471f1378bbca8f93b3539a3e5395935f9faa1c022030af5f5f95ad927ca132374d6d5701fc09ef8b31150253571fa21548c6435fc201 037bd486bb4f0f4ffe9e39f213879fc5b85c00df0194a97da7169589ad9bb3ce84"
            }
        ],
        "outputs": [
            {
                "transaction_hash": "b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf",
                "output_index": 0,
                "value": 300000,
                "addresses": [
                    "3L7dKYQGNoZub928CJ8NC2WfrM8U8GGBjr"
                ],
                "script": "OP_HASH160 ca19cb72e98b7a94979a3a1c58eb516603158749 OP_EQUAL",
                "script_hex": "a914ca19cb72e98b7a94979a3a1c58eb51660315874987",
                "script_type": "scripthash",
                "required_signatures": 1,
                "spent": true
            },
            {
                "transaction_hash": "b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf",
                "output_index": 1,
                "value": 32000,
                "addresses": [
                    "1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb"
                ],
                "script": "OP_DUP OP_HASH160 c629680b8d13ca7a4b7d196360186d05658da6db OP_EQUALVERIFY OP_CHECKSIG",
                "script_hex": "76a914c629680b8d13ca7a4b7d196360186d05658da6db88ac",
                "script_type": "pubkeyhash",
                "required_signatures": 1,
                "spent": false
            }
        ],
        "fees": 10000,
        "amount": 332000
    }
]
"""

transactions = [
    Transaction(
        hash='0bf0de38c26195919179f42d475beb7a6b15258c38b57236afdd60a07eddd2cc',
        block_hash='00000000000000001ea5471a4edc67380f114c6cad06bfd59ac6508f90e8b252',
        block_height=303404,
        block_time='2014-05-30T23:54:55Z',
        confirmations=8758,
        inputs=[
            Transaction.Input(
                transaction_hash='0bf0de38c26195919179f42d475beb7a6b15258c38b57236afdd60a07eddd2cc',
                output_hash='b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf',
                output_index=0,
                value=300000,
                addresses=['3L7dKYQGNoZub928CJ8NC2WfrM8U8GGBjr'],
                script_signature='0 3046022100de7b67b96a6855fbc81c1a4b45d98ba6fef27ddda8739c5a3e7c70039685f7db0221008972607445195847631d902f594db6d712c315e0d49a2bee98125af8e1fefb5701 304402200cc13d8859247bff4ab4bc70964955fa4dbcd1a0dff0a84896be7d9a7757516202206e2c6c0aec6527ccf30305ad6e242c973aad011e9ccc18a0b75fd7be6c9b675301 5221032071a66eaed3dbe31a982dc337108b28bcffbf88d8cac8975194e184abdb36662102134541ec8f3dc2d382646bad199526a64080a66d27d2e156906bdb822774283921020431faa475c966c752e6cf97dfbb2c68c98b0013ca5c76b860263438850c2ba053ae',
            ),
        ],
        outputs=[
            Transaction.Output(
                transaction_hash='0bf0de38c26195919179f42d475beb7a6b15258c38b57236afdd60a07eddd2cc',
                output_index=0,
                value=290000,
                addresses=['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb'],
                script='OP_DUP OP_HASH160 c629680b8d13ca7a4b7d196360186d05658da6db OP_EQUALVERIFY OP_CHECKSIG',
                script_hex='76a914c629680b8d13ca7a4b7d196360186d05658da6db88ac',
                script_type='pubkeyhash',
                required_signatures=1,
                spent=False,
            ),
        ],
        fees=10000,
        amount=290000,
    ),
    Transaction(
        hash='b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf',
        block_hash='0000000000000000577344f05b6ea721b95fa629e0c3b16cdd929cbdf20f862f',
        block_height=303402,
        block_time='2014-05-30T23:38:24Z',
        confirmations=8760,
        inputs=[
            Transaction.Input(
                transaction_hash='b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf',
                output_hash='027bd765dc335ecc37a571d4d8b7cd4ab802e1eb50e91b3e7e9c6689861609e7',
                output_index=1,
                value=252000,
                addresses=['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb'],
                script_signature='3045022100c239e879cde489f2a51ceb16e02806340ca90da07c8c8442620229b7a687afbb022020c08b3a32159ae1fee6dc4f1d1a5edb0613299844622721cefb3e0049e4ee0c01 037bd486bb4f0f4ffe9e39f213879fc5b85c00df0194a97da7169589ad9bb3ce84',
            ),
            Transaction.Input(
                transaction_hash='b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf',
                output_hash='3ae7d2a0b8d6574d2217f3f9b6a205e564b6e34da772d6182e91e2fdbb6eac35',
                output_index=0,
                value=90000,
                addresses=['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb'],
                script_signature='30450221008eec802d9f07f18cfa5677675e471f1378bbca8f93b3539a3e5395935f9faa1c022030af5f5f95ad927ca132374d6d5701fc09ef8b31150253571fa21548c6435fc201 037bd486bb4f0f4ffe9e39f213879fc5b85c00df0194a97da7169589ad9bb3ce84',
            )
        ],
        outputs=[
            Transaction.Output(
                transaction_hash='b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf',
                output_index=0,
                value=300000,
                addresses=['3L7dKYQGNoZub928CJ8NC2WfrM8U8GGBjr'],
                script='OP_HASH160 ca19cb72e98b7a94979a3a1c58eb516603158749 OP_EQUAL',
                script_hex='a914ca19cb72e98b7a94979a3a1c58eb51660315874987',
                script_type='scripthash',
                required_signatures=1,
                spent=True,
            ),
            Transaction.Output(
                transaction_hash='b84a66c46e24fe71f9d8ab29b06df932d77bec2cc0691799fae398a8dc9069bf',
                output_index=1,
                value=32000,
                addresses=['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb'],
                script='OP_DUP OP_HASH160 c629680b8d13ca7a4b7d196360186d05658da6db OP_EQUALVERIFY OP_CHECKSIG',
                script_hex='76a914c629680b8d13ca7a4b7d196360186d05658da6db88ac',
                script_type='pubkeyhash',
                required_signatures=1,
                spent=False,
            )
        ],
        fees=10000,
        amount=332000,
    )
]

http_adapter = mock_get(url, response_body)
