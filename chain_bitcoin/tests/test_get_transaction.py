from __future__ import absolute_import

import sure
from .. import Chain, NoApiKeyId, Transaction, get_transaction
from .mock_http_adapter import *


def test_get_transaction():
    get_transaction(transaction_hash, api_key_id=api_key_id,
                    http_adapter=http_adapter) \
        .should.equal(transaction)


def test_get_transaction_using_class():
    Chain(api_key_id=api_key_id, http_adapter=http_adapter) \
        .get_transaction(transaction_hash) \
        .should.equal(transaction)


def test_get_transaction_without_api_key_id():
    (lambda: get_transaction(transaction_hash, http_adapter=no_http())) \
        .should.throw(NoApiKeyId)


transaction_hash = '0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45'

api_key_id = 'DEMO-4a5e1e4'

url = 'https://api.chain.com/v1/bitcoin/transactions/' \
      '0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45' \
      '?api-key-id=DEMO-4a5e1e4'

response_body = """
{
  "hash": "0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45",
  "block_height": 305188,
  "block_hash": "0000000000000000284bc285e23f970189d048ff38c030aa51007e2a8c2af2f0",
  "block_time": "2014-06-11T01:35:09Z",
  "inputs": [
    {
      "transaction_hash": "0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45",
      "output_hash": "066c19f44922480c784ee11845c3e2c0abd346ac5fd1226cbce43229e699acc7",
      "output_index": 202,
      "value": 38340652,
      "addresses": [
          "1FgPk71oB7Bdwzu67nqjKbCi5c1BTMB1en"
      ],
      "script_signature": "30440220205616172b2c170f632b6386224df2ce151b37e8bfe25dc02ae5ff8cb768b1980220662ba1f78e09f352fcbf9a2ee819bea40b5f319a0063e86423ee6fd44f8913c601 04aa6428fec68a1d1ed159143f98ac60d11239af80f4f47f76407641e3d8e932ae17b75edd2456f9b5bc3ae474203646e02347574e29ba348721cc0d12827adfa5"
    },
    {
      "transaction_hash": "0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45",
      "output_hash": "5cfc6475a36a8f9342203c016c3ab0df8da5028cb0ae6a1fe0b513b6a6cfa14a",
      "output_index": 16,
      "value": 52900438,
      "addresses": [
          "18Kp5Fm8ov1xhBsnwAGeVDshGyRgrNqK9T"
      ],
      "script_signature": "3045022100a9108713b2489499d05907b4136f3b8fe80196c215eca6fb519303ede5ca7d6c02205036e810c1a14ff95b7764a33f794f7fbe44824fceb8f6c080c0b00a8930d86c01 043473bd7321eb7b4ca20b7e4c16b2f5ddd3c5ef7ee0d2a3338a5f54a32d13ca4f63cb0b258cf6d7eab061a082c9bf9c59fa1d214090167f4bc79d31f75b9a89fa"
    },
    {
      "transaction_hash": "0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45",
      "output_hash": "afa6f219724bd04e54e02dfcad56d0ebb8df477e7e58a531ff00a6d34a5d0ce2",
      "output_index": 31,
      "value": 100240048,
      "addresses": [
          "18Kp5Fm8ov1xhBsnwAGeVDshGyRgrNqK9T"
      ],
      "script_signature": "3044022050f52ea1c7c311a6894b740e92f4cbd64fe36c5fefa80a36263376acec53cf36022024f8f307e4fa5d0b21fe6578022553846c3b97410df6ca04055c02ee32bb654e01 043473bd7321eb7b4ca20b7e4c16b2f5ddd3c5ef7ee0d2a3338a5f54a32d13ca4f63cb0b258cf6d7eab061a082c9bf9c59fa1d214090167f4bc79d31f75b9a89fa"
    }
  ],
  "outputs": [
    {
      "transaction_hash": "0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45",
      "output_index": 0,
      "value": 167846400,
      "addresses": [
          "18LdfobPPt5cM3TvtRWXXithpNtjMWqHnQ"
      ],
      "script": "OP_DUP OP_HASH160 507f64bdace7fee77fbc7df5c25772faa4605e32 OP_EQUALVERIFY OP_CHECKSIG",
      "script_hex": "76a914507f64bdace7fee77fbc7df5c25772faa4605e3288ac",
      "script_type": "pubkeyhash",
      "required_signatures": 1,
      "spent": true
    },
    {
      "transaction_hash": "0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45",
      "output_index": 1,
      "value": 23634738,
      "addresses": [
          "142V1XwCc72F1FPyF8mwAENiKvhMA1kaHu"
      ],
      "script": "OP_DUP OP_HASH160 21302c992cfafcade4657969bc62ab415a2d2fd2 OP_EQUALVERIFY OP_CHECKSIG",
      "script_hex": "76a91421302c992cfafcade4657969bc62ab415a2d2fd288ac",
      "script_type": "pubkeyhash",
      "required_signatures": 1,
      "spent": true
    }
  ],
  "amount": 191481138,
  "fees": 0,
  "confirmations": 6860
}
"""

transaction = Transaction(
    hash='0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45',
    block_height=305188,
    block_hash='0000000000000000284bc285e23f970189d048ff38c030aa51007e2a8c2af2f0',
    block_time='2014-06-11T01:35:09Z',
    inputs=[
        Transaction.Input(
            transaction_hash='0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45',
            output_hash='066c19f44922480c784ee11845c3e2c0abd346ac5fd1226cbce43229e699acc7',
            output_index=202,
            value=38340652,
            addresses=['1FgPk71oB7Bdwzu67nqjKbCi5c1BTMB1en'],
            script_signature='30440220205616172b2c170f632b6386224df2ce151b37e8bfe25dc02ae5ff8cb768b1980220662ba1f78e09f352fcbf9a2ee819bea40b5f319a0063e86423ee6fd44f8913c601 04aa6428fec68a1d1ed159143f98ac60d11239af80f4f47f76407641e3d8e932ae17b75edd2456f9b5bc3ae474203646e02347574e29ba348721cc0d12827adfa5',
        ),
        Transaction.Input(
            transaction_hash='0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45',
            output_hash='5cfc6475a36a8f9342203c016c3ab0df8da5028cb0ae6a1fe0b513b6a6cfa14a',
            output_index=16,
            value=52900438,
            addresses=['18Kp5Fm8ov1xhBsnwAGeVDshGyRgrNqK9T'],
            script_signature='3045022100a9108713b2489499d05907b4136f3b8fe80196c215eca6fb519303ede5ca7d6c02205036e810c1a14ff95b7764a33f794f7fbe44824fceb8f6c080c0b00a8930d86c01 043473bd7321eb7b4ca20b7e4c16b2f5ddd3c5ef7ee0d2a3338a5f54a32d13ca4f63cb0b258cf6d7eab061a082c9bf9c59fa1d214090167f4bc79d31f75b9a89fa',
        ),
        Transaction.Input(
            transaction_hash='0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45',
            output_hash='afa6f219724bd04e54e02dfcad56d0ebb8df477e7e58a531ff00a6d34a5d0ce2',
            output_index=31,
            value=100240048,
            addresses=['18Kp5Fm8ov1xhBsnwAGeVDshGyRgrNqK9T'],
            script_signature='3044022050f52ea1c7c311a6894b740e92f4cbd64fe36c5fefa80a36263376acec53cf36022024f8f307e4fa5d0b21fe6578022553846c3b97410df6ca04055c02ee32bb654e01 043473bd7321eb7b4ca20b7e4c16b2f5ddd3c5ef7ee0d2a3338a5f54a32d13ca4f63cb0b258cf6d7eab061a082c9bf9c59fa1d214090167f4bc79d31f75b9a89fa',
        ),
    ],
    outputs=[
        Transaction.Output(
            transaction_hash='0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45',
            output_index=0,
            value=167846400,
            addresses=['18LdfobPPt5cM3TvtRWXXithpNtjMWqHnQ'],
            script='OP_DUP OP_HASH160 507f64bdace7fee77fbc7df5c25772faa4605e32 OP_EQUALVERIFY OP_CHECKSIG',
            script_hex='76a914507f64bdace7fee77fbc7df5c25772faa4605e3288ac',
            script_type='pubkeyhash',
            required_signatures=1,
            spent=True,
        ),
        Transaction.Output(
            transaction_hash='0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45',
            output_index=1,
            value=23634738,
            addresses=['142V1XwCc72F1FPyF8mwAENiKvhMA1kaHu'],
            script='OP_DUP OP_HASH160 21302c992cfafcade4657969bc62ab415a2d2fd2 OP_EQUALVERIFY OP_CHECKSIG',
            script_hex='76a91421302c992cfafcade4657969bc62ab415a2d2fd288ac',
            script_type='pubkeyhash',
            required_signatures=1,
            spent=True,
        ),
    ],
    amount=191481138,
    fees=0,
    confirmations=6860,
)

http_adapter = mock_get(url, response_body)
