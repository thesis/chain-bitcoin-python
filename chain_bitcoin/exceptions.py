from __future__ import absolute_import

__all__ = ('ChainError', 'NoApiKeyId', 'NoApiKeySecret')


class ChainError(BaseException):
    pass


class NoApiKeyId(ChainError):
    pass


class NoApiKeySecret(ChainError):
    pass
