from __future__ import absolute_import

import sure
from .. import Chain, NoApiKeyId, NoApiKeySecret, Webhook, list_webhooks
from .mock_http_adapter import *


def test_list_webhooks():
    list_webhooks(api_key_id=api_key_id, api_key_secret=api_key_secret,
                  http_adapter=http_adapter) \
        .should.equal(webhooks)


def test_list_webhooks_using_class():
    Chain(api_key_id=api_key_id, api_key_secret=api_key_secret,
          http_adapter=http_adapter) \
        .list_webhooks().should.equal(webhooks)


def test_list_webhooks_without_api_key_id():
    (lambda: list_webhooks(http_adapter=no_http())) \
        .should.throw(NoApiKeyId)


def test_list_webhooks_without_api_key_secret():
    (lambda: list_webhooks(api_key_id=api_key_id, http_adapter=no_http())) \
        .should.throw(NoApiKeySecret)


api_key_id = 'DEMO-4a5e1e4'

api_key_secret = 'DEMO-f8aef80',

url = 'https://api.chain.com/v1/webhooks'

response_body = """
[
  {
    "id": "FFA21991-5669-4728-8C83-74DEC4C93A4A",
    "url": "https://username:password@your-server-url.com/1"
  },
  {
    "id": "HF199S42-9274-0294-7HF4-8H6TQS2D85DM",
    "url": "https://username:password@your-server-url.com/2"
  }
]
"""

webhooks = [
    Webhook(
        id='FFA21991-5669-4728-8C83-74DEC4C93A4A',
        url='https://username:password@your-server-url.com/1',
    ),
    Webhook(
        id='HF199S42-9274-0294-7HF4-8H6TQS2D85DM',
        url='https://username:password@your-server-url.com/2',
    ),
]

http_adapter = mock_get(url, response_body)
