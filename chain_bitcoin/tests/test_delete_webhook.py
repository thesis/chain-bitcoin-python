from __future__ import absolute_import

import sure
from .. import Chain, NoApiKeyId, NoApiKeySecret, Webhook, delete_webhook
from .mock_http_adapter import *


def test_delete_webhook():
    delete_webhook(webhook_id, api_key_id=api_key_id,
                   api_key_secret=api_key_secret, http_adapter=http_adapter) \
        .should.equal(webhook)


def test_delete_webhook_using_class():
    Chain(api_key_id=api_key_id, api_key_secret=api_key_secret,
          http_adapter=http_adapter) \
        .delete_webhook(webhook_id=webhook_id).should.equal(webhook)


def test_delete_webhook_without_api_key_id():
    (lambda: delete_webhook(webhook_id=webhook_id, http_adapter=no_http())) \
        .should.throw(NoApiKeyId)


def test_delete_webhook_without_api_key_secret():
    (lambda: delete_webhook(webhook_id=webhook_id, api_key_id=api_key_id,
                            http_adapter=no_http())) \
        .should.throw(NoApiKeySecret)


api_key_id = 'DEMO-4a5e1e4'

api_key_secret = 'DEMO-f8aef80',

webhook_id = 'FFA21991-5669-4728-8C83-74DEC4C93A4A'

url = 'https://api.chain.com/v1/webhooks/FFA21991-5669-4728-8C83-74DEC4C93A4A'

response_body = """
{
  "id": "FFA21991-5669-4728-8C83-74DEC4C93A4A",
  "url": "https://username:password@your-server-url.com"
}
"""

webhook = Webhook(
    id=webhook_id,
    url='https://username:password@your-server-url.com',
)

http_adapter = mock_delete(url, response_body)
