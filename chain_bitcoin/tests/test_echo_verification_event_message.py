from __future__ import absolute_import

import json
import sure
from .. import WebhookEvent, EchoVerificationEvent


def test_address_transaction_callback():
    WebhookEvent.Message.from_dict(json.loads(request_body)) \
        .should.equal(message)


request_body = """
{
   "event": "echo-verification"
}
"""

message = EchoVerificationEvent.Message()
