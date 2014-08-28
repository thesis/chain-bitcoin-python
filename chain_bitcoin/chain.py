from __future__ import absolute_import

__all__ = ('Chain',)

import inspect
import textwrap

from . import endpoints
from .config import *
from .exceptions import *
from .func_util import *
from .models import *
from .namedtuple import *


class Chain(object):

    def __init__(self, config=default_config, **kw):
        """
        Keyword arguments: Any arguments of ``Config``.
        """
        self.config = config.replace(**kw)

    def configure(self, **kw):
        """
        Keyword arguments: Any arguments of ``Config``.

        Returns a new ``Chain``.
        """
        return Chain(self.config, **kw)

    @property
    def requests(self):
        """
        Returns a ``requests.Session``.
        """
        return config_to_requests(self.config)


# Copy functions from the ``endpoints`` module onto the ``Chain`` class.
for name in endpoints.__all__:
    f = getattr(endpoints, name)
    argspec = inspect.getargspec(f)

    # Remove the ``config`` param
    argspec = argspec_drop_right(1, argspec)

    # Add a ``self`` param
    argspec = argspec_append_left(['self'], argspec)

    code = textwrap.dedent("""
        def _{name}{argspec}:
            return endpoints.{name}({args}config=self.config, **kw)
        Chain.{name} = _{name}
    """).format(
        argspec=inspect.formatargspec(*argspec),
        args=''.join(map('{0}, '.format, argspec.args[1:])),
        name=name,
    )
    exec(code, globals())
