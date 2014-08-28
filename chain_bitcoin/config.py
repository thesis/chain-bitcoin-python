from __future__ import absolute_import

__all__ = ('Config', 'ca_cert', 'default_block_chain', 'default_config',
           'config_to_requests', 'require_api_key_id', 'require_api_key_secret')

import os
import requests
import requests.auth

from .exceptions import *
from .namedtuple import namedtuple


class Config(namedtuple('Config', (
    'api_key_id', 'api_key_secret', 'block_chain', 'verify', 'http_adapter'
))):
    """
    Arguments:

        api_key_id: string

        api_key_secret: string

        block_chain: string - The name of the block chain.
        For example: bitcoin or testnet3.
        https://chain.com/docs/v1/curl/#block-chains

        verify - One of:
        - A CA_BUNDLE path for SSL cert verification,
        - ``True`` to verify using the system CA_BUNDLE
        - ``False`` to skip SSL cert verification.
        The default is verification with Chain's CA cert.

        http_adapter: ``requests.adapters.HTTPAdapter``
        The HTTP adapter used to make HTTP requests.
        (This parameter mostly exists for testing.)
    """


ca_cert = os.path.join(os.path.dirname(__file__), 'chain.pem')

default_block_chain = 'bitcoin'

default_config = Config(verify=ca_cert, block_chain=default_block_chain)


def config_to_requests(config):

    session = requests.Session()
    session.verify = config.verify

    if config.api_key_id is not None:

        if config.api_key_secret is not None:
            session.auth = requests.auth.HTTPBasicAuth(
                config.api_key_id, config.api_key_secret)

        else:
            session.params.update({'api-key-id': config.api_key_id})

    if config.http_adapter is not None:
        session.mount('http://', config.http_adapter)
        session.mount('https://', config.http_adapter)

    return session


def require_api_key_id(config):
    if config.api_key_id is None:
        raise NoApiKeyId


def require_api_key_secret(config):
    require_api_key_id(config)
    if config.api_key_secret is None:
        raise NoApiKeySecret
