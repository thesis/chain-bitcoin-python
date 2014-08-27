from __future__ import absolute_import

__all__ = (
    'set_function_defaults', 'argspec_drop_right', 'argspec_append_left'
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
