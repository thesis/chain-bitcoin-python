from __future__ import absolute_import

__all__ = (
    'Address', 'Transaction', 'Output', 'OpReturn', 'Block', 'Webhook',
    'WebhookEvent', 'EchoVerificationEvent', 'AddressTransactionEvent',
    'SendTransactionResult'
)

from .func_util import compose
from .map_list import *
from .namedtuple import *


class Address(namedtuple('Address', (
    'hash', 'balance', 'received', 'sent', 'unconfirmed_received',
    'unconfirmed_sent', 'unconfirmed_balance'
))):
    """
    https://chain.com/docs/v1/curl/#object-bitcoin-address

    The Address Object contains basic balance details for a Bitcoin address.
    """


class Transaction(namedtuple('Transaction', (
    'hash', 'block_hash', 'block_height', 'block_time', 'inputs', 'outputs',
    'amount', 'fees', 'confirmations', 'chain_received_at', 'propagation_level',
    'double_spend'
), alter_dict=compose(
    transform_item(
        'inputs', lambda v: map_list(Transaction.Input.from_dict, v)),
    transform_item(
        'outputs', lambda v: map_list(Transaction.Output.from_dict, v)),
))):
    """
    https://chain.com/docs/v1/curl/#object-bitcoin-transaction

    The Transaction Object contains details about a Bitcoin transaction,
    including inputs and outputs.
    """

    class Input(namedtuple('Transaction_Input', (
        'transaction_hash', 'output_hash', 'output_index', 'value', 'addresses',
        'script_signature', 'coinbase'
    ))):
        """
        https://chain.com/docs/v1/curl/#object-bitcoin-transaction

        Values of ``Transaction.inputs``.
        """

    class Output(namedtuple('Transaction_Output', (
        'transaction_hash', 'output_index', 'value', 'addresses', 'script',
        'script_hex', 'script_type', 'required_signatures', 'spent',
    ))):
        """
        https://chain.com/docs/v1/curl/#object-bitcoin-transaction

        Values of ``Transaction.outputs``.
        """


class SendTransactionResult(namedtuple('SendTransactionResult', ('hash',))):
    """
    https://chain.com/docs/v1/curl/#bitcoin-transaction-send

    The value returned by the ``send_transaction`` endpoint.

    Arguments:

        hash: string - The newly created transaction hash.
    """


class Output(namedtuple('TransactionOutput', (
    'transaction_hash', 'output_index', 'value', 'addresses', 'script',
    'script_hex', 'script_type', 'required_signatures', 'spent',
    'confirmations'
))):
    """
    https://chain.com/docs/v1/curl/#bitcoin-address-unspents

    The Output Object is a pseudo-object that is extracted from the
    Transaction Object for use when the entire Transaction Object is not
    needed.
    """


class OpReturn(namedtuple('OpReturn', (
    'transaction_hash', 'hex', 'text', 'sender_addresses', 'receiver_addresses'
))):
    """
    https://chain.com/docs/v1/curl/#bitcoin-address-op-returns

    The OP_RETURN Object is a pseudo-object that is extracted from the
    Transaction Object. It is an interpretation of the OP_RETURN script
    within a zero-value output in a Bitcoin transaction. The OP_RETURN can
    be used to include 40 bytes of metadata in a Bitcoin transaction.
    """


class Block(namedtuple('Block', (
    'hash', 'previous_block_hash', 'height', 'confirmations', 'merkle_root',
    'time', 'nonce', 'difficulty', 'transaction_hashes'
))):
    """
    https://chain.com/docs/v1/curl/#object-bitcoin-block

    The Block Object contains details about a Bitcoin block, including all
    transaction hashes.
    """


class Webhook(namedtuple('Webhook', ('id', 'url'))):
    """
    https://chain.com/docs/v1/curl/#object-webhooks

    The Webhook Object contains a server URL that the Chain API uses to
    communicate with your application. You can create one or more Webhook
    Objects, which may each have one or more associated Event Objects.
    """


class WebhookEvent:
    """
    https://chain.com/docs/v1/curl/#object-webhooks-event
    """

    event = None
    """
    https://chain.com/docs/v1/curl/#object-webhooks-event

    The event that will trigger the Webhook's POST request.
    """

    class Message(object):
        """
        https://chain.com/docs/v1/curl/#webhooks-receiving

        The class for data sent to the webhook URL.
        """

        @classmethod
        def from_dict(cls, x):
            x = dict(x)
            event_type = next(t for t in webhook_event_types
                              if t.event == x['event'])
            return event_type.Message.from_dict(x)

    @classmethod
    def from_dict(cls, x):
        x = dict(x)
        event_type = next(t for t in webhook_event_types
                          if t.event == x['event'])
        return event_type.from_dict(x)


echo_verification_event = 'echo-verification'

address_transaction_event = 'address-transaction'


class EchoVerificationEvent(
    namedtuple('EchoVerificationEvent', alter_dict=remove_item('event'))
):
    """
    https://chain.com/docs/v1/curl/#webhooks-setup

    Each time you create a new Webhook, before completing the request, the
    Chain API will make a test request to the Webhook in order to verify
    ownership.

    To pass the verification test, your web server must respond with an exact
    copy of the request body.
    """

    event = echo_verification_event

    class Message(namedtuple(
        'EchoVerificationEvent_Message',
        alter_dict=remove_item('event')
    )):
        pass


class AddressTransactionEvent(
    namedtuple('AddressTransactionEvent', (
        'id', 'webhook_id', 'block_chain', 'address', 'confirmations'
    ), alter_dict=remove_item('event')),
    WebhookEvent,
):
    """
    https://chain.com/docs/v1/curl/#object-webhooks-event

    This event triggers when a new transaction occurs on a specified address.
    The first POST will notify your application of the new, unconfirmed
    transaction. Additional POSTs will notify your application of subsequent
    confirmations for that transction.

    Arguments:

        id: string

        webhook_id: string - The unique id of the associated Webhook.

        block_chain: string - The name of the block chain that the Webhook
        Event is associated with.

        address: string - The address that will be used to match Webhook
        Events.

        confirmations: number - The number of confirmations that will be
        POSTed to the Webhook for each new transaction.
    """

    event = address_transaction_event

    class Message(namedtuple('AddressTransactionEvent_Message', (
        'transaction', 'block_chain', 'address'
    ), alter_dict=compose(
        transform_item('transaction', Transaction.from_dict),
        remove_item('event'),
    ))):
        """
        https://chain.com/docs/v1/curl/#webhooks-receiving

        The data structure that will be POSTed to your server from an
        address-transaction event.
        """

        event = address_transaction_event


webhook_event_types = (
    EchoVerificationEvent,
    AddressTransactionEvent,
)
