from __future__ import absolute_import

import sure
from .. import Chain, NoApiKeyId, NoApiKeySecret, AddressTransactionEvent, \
    create_address_transaction_event
from .mock_http_adapter import *


def test_create_address_transaction_event():
    create_address_transaction_event(
        webhook_id, address, confirmations=1, api_key_id=api_key_id,
        api_key_secret=api_key_secret, http_adapter=http_adapter) \
        .should.equal(event)


def test_create_address_transaction_event_using_class():
    Chain(api_key_id=api_key_id, api_key_secret=api_key_secret,
          http_adapter=http_adapter) \
        .create_address_transaction_event(
            webhook_id, address, confirmations=1) \
        .should.equal(event)


def test_create_address_transaction_event_without_api_key_id():
    (lambda: create_address_transaction_event(
        webhook_id, address, confirmations=1, http_adapter=no_http())) \
        .should.throw(NoApiKeyId)


def test_create_address_transaction_event_without_api_key_secret():
    (lambda: create_address_transaction_event(
        webhook_id, address, confirmations=1, api_key_id=api_key_id,
        http_adapter=no_http())) \
        .should.throw(NoApiKeySecret)


api_key_id = 'DEMO-4a5e1e4'

api_key_secret = 'DEMO-f8aef80',

webhook_id = 'FFA21991-5669-4728-8C83-74DEC4C93A4A'

address = '1...'

url = 'https://api.chain.com/v1/webhooks/' \
      'FFA21991-5669-4728-8C83-74DEC4C93A4A/events'

request_json = """
{
  "event": "address-transaction",
  "block_chain": "bitcoin",
  "address": "1...",
  "confirmations": 1
}
"""

response_body = """
{
  "id": "29CDE78E-7BFA-4401-BC0A-3071C88A86F0",
  "webhook_id": "FFA21991-5669-4728-8C83-74DEC4C93A4A",
  "event": "address-transaction",
  "block_chain": "bitcoin",
  "address": "1...",
  "confirmations": 1
}
"""

event = AddressTransactionEvent(
    id='29CDE78E-7BFA-4401-BC0A-3071C88A86F0',
    webhook_id='FFA21991-5669-4728-8C83-74DEC4C93A4A',
    block_chain='bitcoin',
    address='1...',
    confirmations=1,
)

http_adapter = mock_post_json(url, request_json, response_body)
