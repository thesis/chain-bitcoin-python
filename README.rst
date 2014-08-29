chain-bitcoin-python
====================

Integration library for the Chain.com API.

https://pypi.python.org/pypi/chain_bitcoin/

.. pypi - Everything below this line goes into the description for PyPI.


Setup
-----

Either import ``chain_bitcoin``

.. code:: python

    import chain_bitcoin

    address_info = chain_bitcoin.get_address(
        some_address_hash, api_key_id=some_api_key_id)

or configure a ``Chain`` object

.. code:: python

    from chain_bitcoin import Chain

    chain = Chain(api_key_id=some_api_key_id)
    address_info = chain.get_address(some_address_hash)

Function examples
-----------------

.. code:: python

    from chain_bitcoin import Chain

    chain = Chain(api_key_id='...', api_key_secret='...')

    chain.get_address('17x23dNjXJLzGMev6R63uyRhMWP1VHawKc')

    chain.get_addresses(['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb',
                         '1EX1E9n3bPA1zGKDV5iHY2MnM7n5tDfnfH'])

    chain.get_address_transactions('17x23dNjXJLzGMev6R63uyRhMWP1VHawKc')

    chain.get_addresses_transactions(['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb',
                                      '1EX1E9n3bPA1zGKDV5iHY2MnM7n5tDfnfH'])

    chain.get_address_unspents('17x23dNjXJLzGMev6R63uyRhMWP1VHawKc')

    chain.get_addresses_unspents(['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb',
                                  '1EX1E9n3bPA1zGKDV5iHY2MnM7n5tDfnfH'])

    chain.get_address_op_returns('1Bj5UVzWQ84iBCUiy5eQ1NEfWfJ4a3yKG1')

    chain.get_transaction(
        '0f40015ddbb8a05e26bbacfb70b6074daa1990b813ba9bc70b7ac5b0b6ee2c45')

    chain.get_transaction_op_return(
        '4a7d62a4a5cc912605c46c6a6ef6c4af451255a453e6cbf2b1022766c331f803')

    chain.get_block_by_hash(
        '00000000000000009cc33fe219537756a68ee5433d593034b6dc200b34aa35fa')

    chain.get_block_by_height(308920)

    chain.get_latest_block()

    chain.get_block_op_returns_by_hash(
        '00000000000000009cc33fe219537756a68ee5433d593034b6dc200b34aa35fa')

    chain.get_block_op_returns_by_height(308920)

    chain.create_webhook(
        webhook_id='test_webhook',
        webhook_url='https://example.com/chain')

    chain.list_webhooks()

    chain.update_webhook(
        webhook_id='test_webhook',
        webhook_url='https://example.com/chain2')

    chain.create_address_transaction_event(
        webhook_id='test_webhook',
        address='17x23dNjXJLzGMev6R63uyRhMWP1VHawKc',
        confirmations=2)

    chain.list_webhook_events('test_webhook')

    chain.delete_address_transaction_event(
        webhook_id='test_webhook',
        address='17x23dNjXJLzGMev6R63uyRhMWP1VHawKc')

    chain.delete_webhook('test_webhook')

Webhook-parsing example
-----------------------

.. code:: python

    from chain_bitcoin import WebhookEvent
    import json

    message = WebhookEvent.Message.from_dict(json.loads(request.body))

Changes
-------


0.4__
~~~~~
__ https://github.com/cardforcoin/chain-bitcoin-python/milestones/0.4

Type of time attributes: string -> ``datetime`` `(#2)
<https://github.com/cardforcoin/chain-bitcoin-python/issues/2>`_

Type of bitcoin amount attributes: ``int`` -> ``Btc`` `(#3)
<https://github.com/cardforcoin/chain-bitcoin-python/issues/3>`_

0.3
~~~

Initial release

< 0.3
~~~~~

Defunct
