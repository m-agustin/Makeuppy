#__init__.py contains the asynchronous MakeUp wrapper

from makeuppy.aio_makeup import MakeUp
from makeuppy.exceptions import APIException, DeprecatedEndpoint

__all__ = ['MakeUp', 'ApiException', 'DeprecatedEndpoint']