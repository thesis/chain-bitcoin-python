from __future__ import absolute_import

import json
import sure
from .. import WebhookEvent, AddressTransactionEvent, Transaction


def test_address_transaction_callback():
    WebhookEvent.Message.from_dict(json.loads(request_body)) \
        .should.equal(message)


request_body = """
{
  "transaction": {
    "confirmations": 0,
    "hash": "aa89c35ffa2873076980471b4a149f38880bc376898643fec1fd776c2572f1ef",
    "block_height": null,
    "block_hash": null,
    "block_time": null,
    "inputs": [
      {
        "script_signature": "3045022100ebb4f5348c5fbefcdd5c562a853081dd557f36e8099a4f9a46fb00530f2d57e0022016e5dbf4ff2bc8bf085e712e63e1f3a361e941e07f2be28f1ae9bbab1a8e924e01 042dd53bd3c7a7be60688997cde684ca3e05cb5259e9fd165ce1cf3efcbe9b488997792727a5695a959596bed426be559a325bba0b9bda07701dd1dbf69e094bc9",
        "addresses": [
          "mvqaxopu9Uef2qjXSV3fGrp6DcEYnCoYWK"
        ],
        "value": 47080000,
        "output_index": 0,
        "output_hash": "fbaf72cd6fca1a93e969e4ddcd0bc4af2d5a34494800c69fe73af74c333a18c9",
        "transaction_hash": "aa89c35ffa2873076980471b4a149f38880bc376898643fec1fd776c2572f1ef"
      }
    ],
    "outputs": [
      {
        "spent": false,
        "required_signatures": 1,
        "script_type": "pubkeyhash",
        "script": "OP_DUP OP_HASH160 a80ffbadbbf94998c278b06b25d6db68b573d3de OP_EQUALVERIFY OP_CHECKSIG",
        "addresses": [
          "mvqaxopu9Uef2qjXSV3fGrp6DcEYnCoYWK"
        ],
        "value": 47070000,
        "output_index": 0,
        "transaction_hash": "aa89c35ffa2873076980471b4a149f38880bc376898643fec1fd776c2572f1ef"
      }
    ],
    "amount": 47070000,
    "fees": 10000
  },
  "block_chain": "testnet3",
  "event": "address-transaction",
  "address": "mvqaxopu9Uef2qjXSV3fGrp6DcEYnCoYWK"
}
"""

message = AddressTransactionEvent.Message(
    transaction=Transaction(
        confirmations=0,
        hash='aa89c35ffa2873076980471b4a149f38880bc376898643fec1fd776c2572f1ef',
        block_height=None,
        block_hash=None,
        block_time=None,
        inputs=[
            Transaction.Input(
                script_signature='3045022100ebb4f5348c5fbefcdd5c562a853081dd557f36e8099a4f9a46fb00530f2d57e0022016e5dbf4ff2bc8bf085e712e63e1f3a361e941e07f2be28f1ae9bbab1a8e924e01 042dd53bd3c7a7be60688997cde684ca3e05cb5259e9fd165ce1cf3efcbe9b488997792727a5695a959596bed426be559a325bba0b9bda07701dd1dbf69e094bc9',
                addresses=['mvqaxopu9Uef2qjXSV3fGrp6DcEYnCoYWK'],
                value=47080000,
                output_index=0,
                output_hash='fbaf72cd6fca1a93e969e4ddcd0bc4af2d5a34494800c69fe73af74c333a18c9',
                transaction_hash='aa89c35ffa2873076980471b4a149f38880bc376898643fec1fd776c2572f1ef',
            )
        ],
        outputs=[
            Transaction.Output(
                spent=False,
                required_signatures=1,
                script_type='pubkeyhash',
                script='OP_DUP OP_HASH160 a80ffbadbbf94998c278b06b25d6db68b573d3de OP_EQUALVERIFY OP_CHECKSIG',
                addresses=['mvqaxopu9Uef2qjXSV3fGrp6DcEYnCoYWK'],
                value=47070000,
                output_index=0,
                transaction_hash='aa89c35ffa2873076980471b4a149f38880bc376898643fec1fd776c2572f1ef'
            )
        ],
        amount=47070000,
        fees=10000,
    ),
    block_chain='testnet3',
    address='mvqaxopu9Uef2qjXSV3fGrp6DcEYnCoYWK',
)
