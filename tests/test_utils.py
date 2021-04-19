# Testing for utils.py

from makeuppy import utils
import pytest


def test_get_product_id_url():
    assert(
        utils.get_product_id_url(utils.url_id, 1035, utils.url_id2, '/')
        == 'http://makeup-api.herokuapp.com/api/v1/products/1035.json'
    )


def test_get_main_url():
    assert(
        utils.get_main_url(utils.base_url, 'blush', None)
        == 'http://makeup-api.herokuapp.com/api/v1/products.json?product_type=blush'
    )


def test_get_main_url_with_extension():
    assert(
        utils.get_main_url(utils.base_url, 'blush', 'powder')
        == 'http://makeup-api.herokuapp.com/api/v1/products.json?product_type=blush&product_category=powder'
    )


def test_get_tags_url():
    assert(
        utils.get_tags_url(utils.base_url, 'natural', None, None)
        == 'http://makeup-api.herokuapp.com/api/v1/products.json?product_tags=natural'
    )


def test_get_tags_url_with_product_type():
    assert(
        utils.get_tags_url(utils.base_url, 'natural', 'blush', None)
        == 'http://makeup-api.herokuapp.com/api/v1/products.json?product_tags=natural&product_type=blush'
    )


def test_get_tags_url_with_product_category():
    assert(
        utils.get_tags_url(
            utils.base_url, 'natural', None, 'powder')
        == 'http://makeup-api.herokuapp.com/api/v1/products.json?product_tags=natural&product_category=powder'
    )


def test_get_tags_url_with_product_type_and_product_category():
    assert(
        utils.get_tags_url(
            utils.base_url, 'natural', 'blush', 'powder')
        == 'http://makeup-api.herokuapp.com/api/v1/products.json?product_tags=natural&product_type=blush&product_category=powder'
    )


def test_get_brand_url():
    assert(
        utils.get_brand_url(
            utils.base_url, 'benefit', None, None)
        == 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=benefit'
    )


def test_get_brand_url_with_product_type():
    assert(
        utils.get_brand_url(
            utils.base_url, 'benefit', 'blush', None)
        == 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=benefit&product_type=blush'
    )


def test_get_brand_url_with_product_category():
    assert(
        utils.get_brand_url(
            utils.base_url, 'benefit', None, 'powder')
        == 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=benefit&product_category=powder'
    )


def test_get_brand_url_with_product_type_and_product_category():
    assert(
        utils.get_brand_url(
            utils.base_url, 'benefit', 'blush', 'powder')
        == 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=benefit&product_type=blush&product_category=powder'
    )