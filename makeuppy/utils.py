#Utility methods used for MakeUp

from typing import Optional, Dict, Union, Any

import requests
import aiohttp


base_url = 'http://makeup-api.herokuapp.com/api/v1/products.json'
url_id = 'http://makeup-api.herokuapp.com/api/v1/products'
url_id2 = '.json'

def add_makeup_metadata(response: Union[requests.Response, aiohttp.ClientResponse], response_dict: Dict[str, Any], url: str,) -> Dict[str, Any]:
    response_dict['make_up'] = url
    if isinstance(response, aiohttp.ClientResponse):
        response_dict['headers'] = dict(response.headers)
    else:
        response_dict['headers'] = dict(response.headers)
    return response_dict


def get_product_id_url(url_id: str, id: int, url_id2: str, delimiter: str = '/') -> str:
    url = f'{url_id}{delimiter}{id}{url_id2}'
    return url


def get_main_url(base_url: str, endpoint: str, extension: Optional[str]) -> str:
    url = f'{base_url}?product_type={endpoint}'
    if extension is not None:
        url += f'&product_category={extension}'
    return url
#creates the URL for the product endpoint with or without extension
#endpoint: product_type
#extension: product_category


def get_tags_url(base_url: str, product_tags: str, product_type: Optional[str], product_category: Optional[str]):
    url = f'{base_url}?product_tags={product_tags}'
    product_tags.replace(' ', '+')
    if product_type is not None:
        url += f'&product_type={product_type}'
    if product_category is not None:
        url += f'&product_category={product_category}'
    return url
#spaces in product_tags will be replaces with '+', according to the API
#multiple tags can be inserted, just separate each one with a comma','


def get_brand_url(base_url: str, brand: str, product_type: Optional[str], product_category: Optional[str]):
    url = f'{base_url}?brand={brand}'
    brand.replace(' ', '+')
    if product_type is not None:
        url += f'&product_type={product_type}'
    if product_category is not None:
        url += f'&product_category={product_category}'
    return url
#spaces in brand will be replaces with '+', according to the API
#multiple brands can be inserted, just separate each one with a comma','