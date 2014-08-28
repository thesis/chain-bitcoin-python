"""
These functions all accept, as additional keyword arguments, any arguments
of ``Config``.
"""

from __future__ import absolute_import

__all__ = []

import functools
import json

from . import urls
from .config import *
from .exceptions import *
from .map_list import *
from .models import *

base_url = 'https://api.chain.com'

make_url = functools.partial(urls.make_url, base_url)

json_header = {'content-type': 'application/json'}


def json_args(x):
    return dict(data=json.dumps(x), headers=json_header)


def parse_response_data(response):
    x = response.json()
    if 'error' in x:
        raise ChainError(x['error'])
    return x


def endpoint(f):
    __all__.append(f.__name__)
    return f


@endpoint
def get_address(address, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-address

    Arguments:

        address: string
        A Bitcoin address.

    Return: ``Address``
    """
    config = config.replace(**kw)
    require_api_key_id(config)
    requests = config_to_requests(config)
    url = make_url(['v1', config.block_chain, 'addresses', address])
    response_data = parse_response_data(requests.get(url))
    return Address.from_dict(response_data)


@endpoint
def get_addresses(addresses, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-address

    Arguments:

        addresses: list of string
        A set of Bitcoin addresses.

    Return: list of ``Address``
    """
    config = config.replace(**kw)
    require_api_key_id(config)
    requests = config_to_requests(config)
    url = make_url(
        ['v1', config.block_chain, 'addresses', ','.join(addresses)]
    )
    response_data = parse_response_data(requests.get(url))
    return map_list(Address.from_dict, response_data)


@endpoint
def get_address_transactions(address, limit=None, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-address-transactions

    Arguments:

        address: string
        A Bitcoin address.

        limit: number
        The max number of transactions to return, starting with most recent.

    Return: list of ``Transaction``
    """
    config = config.replace(**kw)
    require_api_key_id(config)
    requests = config_to_requests(config)
    url = make_url(
        ['v1', config.block_chain, 'addresses', address, 'transactions'],
        [('limit', limit)]
    )
    response_data = parse_response_data(requests.get(url))
    return map_list(Transaction.from_dict, response_data)


@endpoint
def get_addresses_transactions(addresses, limit=None, config=default_config,
                               **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-address-transactions

    Arguments:

        addresses: list of string
        A set of Bitcoin addresses.

        limit: number
        The max number of transactions to return, starting with most recent.

    Return: list of ``Transaction``
    """
    config = config.replace(**kw)
    require_api_key_id(config)
    requests = config_to_requests(config)
    url = make_url(
        ['v1', config.block_chain, 'addresses', ','.join(addresses),
         'transactions'],
        [('limit', limit)]
    )
    response_data = parse_response_data(requests.get(url))
    return map_list(Transaction.from_dict, response_data)


@endpoint
def get_address_unspents(address, limit=None, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-address-unspents

    Arguments:

        address: string
        A Bitcoin address.

        limit: number
        The max number of transactions to return, starting with most recent.

    Return: list of ``Output``
    """
    config = config.replace(**kw)
    require_api_key_id(config)
    requests = config_to_requests(config)
    url = make_url(
        ['v1', config.block_chain, 'addresses', address, 'unspents'],
        [('limit', limit)]
    )
    response_data = parse_response_data(requests.get(url))
    return map_list(Output.from_dict, response_data)


@endpoint
def get_addresses_unspents(addresses, limit=None, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-address-unspents

        addresses: list of string
        A set of Bitcoin addresses.

        limit: number
        The max number of transactions to return, starting with most recent.

    Return: list of ``Output``
    """
    config = config.replace(**kw)
    require_api_key_id(config)
    requests = config_to_requests(config)
    url = make_url(
        ['v1', config.block_chain, 'addresses', ','.join(addresses),
         'unspents'],
        [('limit', limit)]
    )
    response_data = parse_response_data(requests.get(url))
    return map_list(Output.from_dict, response_data)


@endpoint
def get_address_op_returns(address, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-address-op-returns

    Arguments:

        address: string
        A Bitcoin address.

    Return: list of ``OpReturn``
    """
    config = config.replace(**kw)
    require_api_key_id(config)
    requests = config_to_requests(config)
    url = make_url(
        ['v1', config.block_chain, 'addresses', address, 'op-returns']
    )
    response_data = parse_response_data(requests.get(url))
    return map_list(OpReturn.from_dict, response_data)


@endpoint
def get_transaction(transaction_hash, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-transaction

    Arguments:

        hash: string
        A transaction hash.

    Return: ``Transaction``
    """
    config = config.replace(**kw)
    require_api_key_id(config)
    requests = config_to_requests(config)
    url = make_url(['v1', config.block_chain, 'transactions', transaction_hash])
    response_data = parse_response_data(requests.get(url))
    return Transaction.from_dict(response_data)


@endpoint
def get_transaction_op_return(transaction_hash, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-transaction-op-return

    Arguments:

        hash: string
        A transaction hash.

    Return: ``OpReturn``
    """
    config = config.replace(**kw)
    require_api_key_id(config)
    requests = config_to_requests(config)
    url = make_url(['v1', config.block_chain, 'transactions', transaction_hash,
                    'op-return'])
    response_data = parse_response_data(requests.get(url))
    return OpReturn.from_dict(response_data)


@endpoint
def send_transaction(hex, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-transaction-send

    Arguments:

        hex: string
        A hex representation of the signed transaction.

    Return: ``SendTransactionResult``
    """
    config = config.replace(**kw)
    require_api_key_secret(config)
    requests = config_to_requests(config)
    url = make_url(['v1', config.block_chain, 'transactions'])
    request_data = {'hex': hex}
    response = requests.put(url, **json_args(request_data))
    response_data = parse_response_data(response)
    return SendTransactionResult.from_dict(response_data)


def _get_block(x, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-block

    Return: ``Block``
    """
    config = config.replace(**kw)
    require_api_key_id(config)
    requests = config_to_requests(config)
    url = make_url(['v1', config.block_chain, 'blocks', x])
    response_data = parse_response_data(requests.get(url))
    return Block.from_dict(response_data)


@endpoint
def get_block_by_hash(block_hash, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-block

    Arguments:

        hash: string
        A block hash.

    Return: ``Block``
    """
    return _get_block(block_hash, config, **kw)


@endpoint
def get_block_by_height(height, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-block

    Arguments:

        height: integer
        A block height.

    Return: ``Block``
    """
    return _get_block(str(height), config, **kw)


@endpoint
def get_latest_block(config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-block

    Return: ``Block``
    """
    return _get_block('latest', config, **kw)


def _get_block_op_returns(x, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-block-op-returns

    Return: ``OpReturn``
    """
    config = config.replace(**kw)
    require_api_key_id(config)
    requests = config_to_requests(config)
    url = make_url(['v1', config.block_chain, 'blocks', x, 'op-returns'])
    response_data = parse_response_data(requests.get(url))
    return map_list(OpReturn.from_dict, response_data)


@endpoint
def get_block_op_returns_by_hash(block_hash, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-block-op-returns

    Arguments:

        hash: string
        A block hash.

    Return: ``OpReturn``
    """
    return _get_block_op_returns(block_hash, config, **kw)


@endpoint
def get_block_op_returns_by_height(height, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#bitcoin-block-op-returns

    Arguments:

        height: integer
        A block height.

    Return: ``OpReturn``
    """
    return _get_block_op_returns(str(height), config, **kw)


@endpoint
def create_webhook(webhook_url, webhook_id=None, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#webhooks-create

    Arguments:

        webhook_url: string
        The URL of the server that will receive the Webhook POST requests.

        webhook_id: string
        A user-generated id for the Webhook. If you do not provide an id,
        one will be automatically generated by the API.

    Return: ``Webhook``
    """
    config = config.replace(**kw)
    require_api_key_secret(config)
    requests = config_to_requests(config)
    url = make_url(['v1', 'webhooks'])
    request_data = {'id': webhook_id, 'url': webhook_url}
    response = requests.post(url, **json_args(request_data))
    response_data = parse_response_data(response)
    return Webhook.from_dict(response_data)


@endpoint
def list_webhooks(config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#webhooks-list

    Return: list of ``Webhook``
    """
    config = config.replace(**kw)
    require_api_key_secret(config)
    requests = config_to_requests(config)
    url = make_url(['v1', 'webhooks'])
    response_data = parse_response_data(requests.get(url))
    return map_list(Webhook.from_dict, response_data)


@endpoint
def update_webhook(webhook_url, webhook_id, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#webhooks-update

    Arguments:

        webhook_url: string
        The new server URL that will receive the Webhook POST requests.

        webhook_id: string
        The unique id of the Webhook.

    Return: ``Webhook``
    """
    config = config.replace(**kw)
    require_api_key_secret(config)
    requests = config_to_requests(config)
    url = make_url(['v1', 'webhooks', webhook_id])
    request_data = {'url': webhook_url}
    response = requests.put(url, **json_args(request_data))
    response_data = parse_response_data(response)
    return Webhook.from_dict(response_data)


@endpoint
def delete_webhook(webhook_id, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#webhooks-delete

    Arguments:

        id: string
        The unique id of the Webhook.

    Return: ``Webhook``
    """
    config = config.replace(**kw)
    require_api_key_secret(config)
    requests = config_to_requests(config)
    url = make_url(['v1', 'webhooks', webhook_id])
    response = requests.delete(url)
    response_data = parse_response_data(response)
    return Webhook.from_dict(response_data)


@endpoint
def create_address_transaction_event(webhook_id, address, confirmations=None,
                                     config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#webhooks-event-create

    Arguments:

        webhook_id: string - The unique id of the associated Webhook.

        address: string - The address that will be used to match Webhook
        Events.

        confirmations: number - The number of confirmations that will be
        POSTed to the Webhook for each new transaction.

    Return: ``AddressTransactionEvent``
    """
    config = config.replace(**kw)
    require_api_key_secret(config)
    requests = config_to_requests(config)
    url = make_url(['v1', 'webhooks', webhook_id, 'events'])
    request_data = {
        'event': AddressTransactionEvent.event,
        'block_chain': config.block_chain,
        'address': address,
    }
    if confirmations is not None:
        request_data['confirmations'] = confirmations
    response = requests.post(url, **json_args(request_data))
    response_data = parse_response_data(response)
    return AddressTransactionEvent.from_dict(response_data)


@endpoint
def list_webhook_events(webhook_id, config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#webhooks-event-list

    Arguments:

        webhook_id: string
        The unique id of the associated Webhook.

    Return: list of ``WebhookEvent``
    """
    config = config.replace(**kw)
    require_api_key_secret(config)
    requests = config_to_requests(config)
    url = make_url(['v1', 'webhooks', webhook_id, 'events'])
    response_data = parse_response_data(requests.get(url))
    return map_list(WebhookEvent.from_dict, response_data)


@endpoint
def delete_address_transaction_event(webhook_id, address,
                                     config=default_config, **kw):
    """
    https://chain.com/docs/v1/curl/#webhooks-event-delete

    Arguments:

        webhook_id: string
        The unique id of the associated Webhook.

        address: string
        The address that is used to match Webhook Events.

    Return: ``AddressTransactionEvent``
    """
    config = config.replace(**kw)
    require_api_key_secret(config)
    requests = config_to_requests(config)
    url = make_url(['v1', 'webhooks', webhook_id, 'events',
                    AddressTransactionEvent.event, address])
    response_data = parse_response_data(requests.delete(url))
    return AddressTransactionEvent.from_dict(response_data)
