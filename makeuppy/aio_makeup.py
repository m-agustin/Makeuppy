#aio_makeup.py contains the MakeUp class, an asynchronous wrapper


import json
from typing import Optional, Dict, Union, Any, TypeVar

import aiohttp
import simplejson

from makeuppy import exceptions
from makeuppy import utils

MakeUpT = TypeVar('MakeUpT', bound='MakeUp')
#Binds type variable to MakeUp to be used in type hints, so linting can flag possible type problems.


class MakeUp:
#Asynchronous wrapper for the public api: http://makeup-api.herokuapp.com/
    def __init__(self, selected_base: Optional[str] = None, session: Optional[aiohttp.ClientSession] = None,) -> None:
    #selected_base defaults to the public API URL
        self.base = (utils.base_url if selected_base is None else selected_base.rstrip('/'))
        self.id_url = (utils.url_id if selected_base is None else selected_base.rstrip('/'))
        self.id_url2 = (utils.url_id2 if selected_base is None else selected_base.rstrip('/'))
        self.session = session
    
    async def __aenter__(self: MakeUpT) -> MakeUpT:
        return self
    
    async def __aexit__(self, *excinfo: Any) -> None:
        await self.close()

    async def close(self) -> None:
        #Closes session
        if self.session is not None:
            await self.session.close()
    
    async def _get_session(self) -> aiohttp.ClientSession:
        if self.session is None:
            self.session = aiohttp.ClientSession()
        return self.session
    
    async def _wrap_response(self, response: aiohttp.ClientResponse, url: str, **kwargs: Union[int, Optional[str]],) -> Dict[str, Any]:
        json_response: Dict[str, Any] = {}
        #Response will be in json
        #Checked and added to add_makeup_metadata
        try:
            json_response = await response.json()
            if not isinstance(json_response, dict):
                json_response = {'data': json_response}
        except (json.decoder.JSONDecodeError, simplejson.JSONDecodeError):
            json_response = {'error': await response.text()}
        if response.status >= 400:
            raise APIException(response.status, json_response, **kwargs)
        return utils.add_makeup_metadata(response, json_response, url)
    
    async def _request(self, url: str, **kwargs: Union[int, Optional[str]]) -> Dict[str, Any]:
    #Makes a request to the API given the url and wraps the response
        session = await self._get_session()
        response = await session.get(url)
        return await self._wrap_response(response, url, **kwargs)

    async def _get(self, endpoint: str, extension: Optional[str] = None) -> Dict[str, Any]:
    #Gets the response from API given the endpoint: blush, bronzer, eyebrow, 
    # eyeliner, eyeshawdow, foundation, lipliner, lipstick, mascara, or nailpolish
    #ex: blush_powder = await make_up._get(endpoint='blush', extension='powder')
        url = utils.get_main_url(self.base, endpoint, extension)
        return await self._request(url, endpoint=endpoint, extension=extension)

    async def product_id(self, id: int) -> Dict[str, Any]:
    #ex: blush_id = await make_up.product_id(1035)
        url = utils.get_product_id_url(self.id_url, id, self.id_url2)
        return await self._request(url, id=id)
        
    async def tags(self, product_tags: str, product_type: Optional[str], product_category: Optional[str]) -> Dict[str, Any]:
    #ex: vegan = await make_up.tags(product_tags='vegan', product_type='bronzer', product_category='powder')
        url = utils.get_tags_url(self.base, product_tags, product_type, product_category)
        return await self._request(url, product_tags=product_tags, product_type=product_type, product_category=product_category)

    async def brand(self, brand: str, product_type: Optional[str], product_category: Optional[str]) -> Dict[str, Any]:
    #ex: benefit = await make_up.brand('benefit', None, None)
        url = utils.get_brand_url(self.base, brand, product_type, product_category)
        return await self._request(url, brand=brand, product_type=product_type, product_category=product_category)
    
