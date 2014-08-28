from __future__ import absolute_import

import sure
from .. import Chain, NoApiKeyId, NoApiKeySecret, AddressTransactionEvent, \
    delete_address_transaction_event
from .mock_http_adapter import *


def test_delete_address_transaction_event():
    delete_address_transaction_event(
        webhook_id, address, api_key_id=api_key_id,
        api_key_secret=api_key_secret, http_adapter=http_adapter) \
        .should.equal(event)


def test_delete_address_transaction_event_using_class():
    Chain(api_key_id=api_key_id, api_key_secret=api_key_secret,
          http_adapter=http_adapter) \
        .delete_address_transaction_event(webhook_id, address) \
        .should.equal(event)


def test_delete_address_transaction_event_without_api_key_id():
    (lambda: delete_address_transaction_event(
        webhook_id, address, http_adapter=no_http())) \
        .should.throw(NoApiKeyId)


def test_delete_address_transaction_event_without_api_key_secret():
    (lambda: delete_address_transaction_event(
        webhook_id, address, api_key_id=api_key_id, http_adapter=no_http())) \
        .should.throw(NoApiKeySecret)


api_key_id = 'DEMO-4a5e1e4'

api_key_secret = 'DEMO-f8aef80',

webhook_id = 'FFA21991-5669-4728-8C83-74DEC4C93A4A'

address = '17x23dNjXJLzGMev6R63uyRhMWP1VHawKc'

url = 'https://api.chain.com/v1/' \
      'webhooks/FFA21991-5669-4728-8C83-74DEC4C93A4A/' \
      'events/address-transaction/17x23dNjXJLzGMev6R63uyRhMWP1VHawKc'

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
    webhook_id=webhook_id,
    block_chain='bitcoin',
    address='1...',
    confirmations=1,
)

http_adapter = mock_delete(url, response_body)
