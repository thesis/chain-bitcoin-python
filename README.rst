chain-bitcoin-python
====================

Integration library for the Chain.com API.

.. pypi - Everything below this line goes into the description for PyPI.


Usage
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
