from __future__ import absolute_import

from datetime import datetime
from dateutil.tz import tzoffset
import sure
from .. import Chain, NoApiKeyId, Block, get_latest_block
from .mock_http_adapter import *


def test_get_block_by_height():
    get_latest_block(api_key_id=api_key_id, http_adapter=http_adapter) \
        .should.equal(block)


def test_get_block_by_height_using_class():
    Chain(api_key_id=api_key_id, http_adapter=http_adapter) \
        .get_latest_block().should.equal(block)


def test_get_latest_block_without_api_key_id():
    (lambda: get_latest_block(http_adapter=no_http())).should.throw(NoApiKeyId)


api_key_id = 'DEMO-4a5e1e4'

url = 'https://api.chain.com/v1/bitcoin/blocks/latest?api-key-id=DEMO-4a5e1e4'

response_body = """
{
  "hash": "00000000000000009cc33fe219537756a68ee5433d593034b6dc200b34aa35fa",
  "previous_block_hash": "0000000000000000099884eea8528821fef5953271216d476ad1fc504630d23a",
  "height": 293268,
  "confirmations": 13470,
  "merkle_root": "942ed435c0a43b0113fcba86c75a22b5430977b8403eb5a405a86c8e17f67f0e",
  "time": "2014-03-30T18:40:51Z",
  "nonce": 793426357,
  "difficulty": 5006860589.2054,
  "transaction_hashes": [
    "fb0d50847824a3f15e7184be7def4ccd3fba2deb71f3df6cf63b7ed24073cdc3",
    "8d2ba64cead3cf9506789609c075c070298c3d4035f96909427a3bb7fcc2d56d",
    "564b96b130438c7c9b17207ff68f96b58f077036a014722012d292f8e0a56fcb",
    "..."
  ]
}
"""

block = Block(
    hash='00000000000000009cc33fe219537756a68ee5433d593034b6dc200b34aa35fa',
    previous_block_hash='0000000000000000099884eea8528821fef5953271216d476ad1fc504630d23a',
    height=293268,
    confirmations=13470,
    merkle_root='942ed435c0a43b0113fcba86c75a22b5430977b8403eb5a405a86c8e17f67f0e',
    time=datetime(2014, 3, 30, 18, 40, 51, tzinfo=tzoffset(None, 0)),
    nonce=793426357,
    difficulty=5006860589.2054,
    transaction_hashes=[
        'fb0d50847824a3f15e7184be7def4ccd3fba2deb71f3df6cf63b7ed24073cdc3',
        '8d2ba64cead3cf9506789609c075c070298c3d4035f96909427a3bb7fcc2d56d',
        '564b96b130438c7c9b17207ff68f96b58f077036a014722012d292f8e0a56fcb',
        '...',
    ],
)

http_adapter = mock_get(url, response_body)
