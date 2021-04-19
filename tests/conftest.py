import asyncio
import json
import sys

import pytest
import simplejson


@pytest.fixture
def aio_response_mock(use_json_decoder=True):
    class ResponseMock:
        def __init__(self):
            self.status = 404
    #simulate a failed request
        async def json(self):
            if use_json_decoder:
                raise json.decoder.JSONDecodeError('Failed', '', 0)
            raise simplejson.JSONDecodeError('Failed', '', 0)

        async def text(self):
            """Request not valid"""
            return """<html>
                <head><title>404 Error</title></head>
                <body>
                <center><h1>Not Found</h1></center>
                </body>
                </html>
            """
    return ResponseMock()


@pytest.fixture
def aio_response_non_dict_mock():
    class ResponseMock:
        def __init__(self):
            self.status = 200
            self.headers = {'Content-Type': 'application/json'}

        async def json(self):
            return ['blush', 'lipstick']

    return ResponseMock()