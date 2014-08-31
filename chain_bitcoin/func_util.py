from __future__ import absolute_import

__all__ = (
    'set_function_defaults', 'argspec_drop_right', 'argspec_append_left',
    'if_not_none'
)

from inspect import ArgSpec


def set_function_defaults(f, defaults):
    if hasattr(f, '__defaults__'):  # python 3
        f.__defaults__ = tuple(defaults) or None
    elif hasattr(f, 'func_defaults'):  # python 2
        f.func_defaults = tuple(defaults) or None
    else:
        raise Exception('???')


def argspec_drop_right(n, argspec):
    return argspec._replace(args=argspec.args[:-n],
                            defaults=argspec.defaults[:-n] or None)


def argspec_append_left(new_args, argspec):
    return argspec._replace(args=(new_args + argspec.args))


def compose(*fs):
    """
    compose(a, b, c)(x) = a(b(c(x)))
    """
    def g(x):
        for f in reversed(fs):
            x = f(x)
        return x

    return g


def if_not_none(f):
    return lambda x: None if x is None else f(x)
