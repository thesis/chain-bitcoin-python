from __future__ import absolute_import

__all__ = ('MockHttpAdapter', 'mock_one_request', 'mock_get', 'mock_put_json',
           'mock_post_json', 'mock_delete', 'no_http')

import json
from requests import Response

from ..namedtuple import namedtuple

default_encoding = 'utf-8'


def create_response(**kw):
    r = Response()
    r._content = b''
    r.status = 200
    for k, v in kw.items():
        setattr(r, k, v)
    return r


class MockHttpAdapter(object):

    def __init__(self, f):
        self._f = f

    def send(self, request, *args, **kw):
        return self._f(request)

    def close(self, *args, **kw):
        pass


def no_http():

    def f(request):
        return create_response(
            status=404,
            _content=json.dumps({
                'error': 'There are no HTTP requests mocked.',
                'url': request.url,
            }).encode(encoding),
            encoding=encoding,
        )

    return MockHttpAdapter(f)


def mock_one_request(url=None, method=None, request_json=None,
                     response_body='', encoding=default_encoding):

    def f(request):

        if method is not None and request.method != method:
            return create_response(
                status=404,
                _content=json.dumps({
                    'wrong method': request.method
                }).encode(encoding),
                encoding=encoding,
            )

        if url is not None and request.url != url:
            return create_response(
                status=404,
                _content=json.dumps({
                    'url not mocked': request.url
                }).encode(encoding),
                encoding=encoding,
            )

        if (
            (request_json is not None) and
            (not json_equivalent(request.body, request_json))
        ):
            return create_response(
                status=404,
                _content=json.dumps({
                    'wrong request body': request.body.decode(encoding)
                }).encode(encoding),
                encoding=encoding,
            )

        return create_response(
            _content=response_body.encode(encoding),
            encoding=encoding,
        )

    return MockHttpAdapter(f)


def mock_get(url, response_body, encoding=default_encoding):
    return mock_one_request(
        url=url, method='GET', response_body=response_body, encoding=encoding)


def mock_put_json(url, request_json, response_body, encoding=default_encoding):
    return mock_one_request(
        url=url, method='PUT', request_json=request_json,
        response_body=response_body, encoding=encoding)


def mock_post_json(url, request_json, response_body, encoding=default_encoding):
    return mock_one_request(
        url=url, method='POST', request_json=request_json,
        response_body=response_body, encoding=encoding)


def mock_delete(url, response_body, encoding=default_encoding):
    return mock_one_request(url=url, method='DELETE',
                            response_body=response_body, encoding=encoding)


def json_equivalent(x, y):
    return json.loads(x) == json.loads(y)
