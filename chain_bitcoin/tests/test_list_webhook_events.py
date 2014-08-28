from __future__ import absolute_import

import sure
from .. import Chain, NoApiKeyId, NoApiKeySecret, AddressTransactionEvent, \
    list_webhook_events
from .mock_http_adapter import *


def test_list_webhook_events():
    list_webhook_events(
        webhook_id, api_key_id=api_key_id, api_key_secret=api_key_secret,
        http_adapter=http_adapter) \
        .should.equal(events)


def test_list_webhook_events_using_class():
    Chain(api_key_id=api_key_id, api_key_secret=api_key_secret,
          http_adapter=http_adapter) \
        .list_webhook_events(webhook_id).should.equal(events)


def test_list_webhook_events_without_api_key_id():
    (lambda: list_webhook_events(webhook_id, http_adapter=no_http())) \
        .should.throw(NoApiKeyId)


def test_list_webhook_events_without_api_key_secret():
    (lambda: list_webhook_events(webhook_id, api_key_id=api_key_id,
                                 http_adapter=no_http())) \
        .should.throw(NoApiKeySecret)


api_key_id = 'DEMO-4a5e1e4'

api_key_secret = 'DEMO-f8aef80',

webhook_id = 'FFA21991-5669-4728-8C83-74DEC4C93A4A'

url = 'https://api.chain.com/v1/webhooks/' \
      'FFA21991-5669-4728-8C83-74DEC4C93A4A/events'

response_body = """
[
  {
    "id": "29CDE78E-7BFA-4401-BC0A-3071C88A86F0",
    "webhook_id": "FFA21991-5669-4728-8C83-74DEC4C93A4A",
    "event": "address-transaction",
    "block_chain": "bitcoin",
    "address": "1A34...",
    "confirmations": 1
  },
  {
    "id": "S2K459FK-8G3N-1936-J29C-K7G3V9D77FG1",
    "webhook_id": "FFA21991-5669-4728-8C83-74DEC4C93A4A",
    "event": "address-transaction",
    "block_chain": "bitcoin",
    "address": "1H6D...",
    "confirmations": 5
  }
]
"""

events = [
    AddressTransactionEvent(
        id='29CDE78E-7BFA-4401-BC0A-3071C88A86F0',
        webhook_id=webhook_id,
        block_chain='bitcoin',
        address='1A34...',
        confirmations=1,
    ),
    AddressTransactionEvent(
        id='S2K459FK-8G3N-1936-J29C-K7G3V9D77FG1',
        webhook_id=webhook_id,
        block_chain='bitcoin',
        address='1H6D...',
        confirmations=5,
    ),
]

http_adapter = mock_get(url, response_body)
