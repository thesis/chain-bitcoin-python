import ast
import inspect
import pexpect.replwrap
import re
import textwrap


def test():

    from chain_bitcoin import Chain

    chain = Chain(
        api_key_id='',
        api_key_secret='')

    chain.get_address('17x23dNjXJLzGMev6R63uyRhMWP1VHawKc')

    chain.get_addresses(['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb',
                         '1EX1E9n3bPA1zGKDV5iHY2MnM7n5tDfnfH'])

    chain.get_address_transactions('17x23dNjXJLzGMev6R63uyRhMWP1VHawKc')[:2]

    chain.get_addresses_transactions(['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb',
                                      '1EX1E9n3bPA1zGKDV5iHY2MnM7n5tDfnfH'])[:2]

    chain.get_address_unspents('17x23dNjXJLzGMev6R63uyRhMWP1VHawKc')

    chain.get_addresses_unspents(['1K4nPxBMy6sv7jssTvDLJWk1ADHBZEoUVb',
                                  '1EX1E9n3bPA1zGKDV5iHY2MnM7n5tDfnfH'])[:2]

    chain.get_address_op_returns('1Bj5UVzWQ84iBCUiy5eQ1NEfWfJ4a3yKG1')[:2]

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


def commands(f):
    lines, _ = inspect.getsourcelines(f)
    lines = lines[1:]
    source = textwrap.dedent(''.join(lines))
    lines = source.split('\n')
    nodes = list(ast.iter_child_nodes(ast.parse(source)))
    line_starts = [node.lineno - 1 for node in nodes]
    line_ranges = zip(line_starts, line_starts[1:] + [len(lines)])
    return ('\n'.join(lines[a:b]).strip() for (a, b) in line_ranges)


def repl_commands(commands):
    repl = pexpect.replwrap.python()
    for command in commands:
        print('>>> {}\n'.format(re.sub('\n', '\n... ', command)))
        print(repl.run_command(command))


def main():
    repl_commands(commands(test))


if __name__ == '__main__':
    main()
