#Testing for aio_makeup.py
import pytest
import vcr

from makeuppy.aio_makeup import MakeUp
from makeuppy.exceptions import APIException, DeprecatedEndpoint
from makeuppy import utils


pytestmark = pytest.mark.asyncio


@pytest.fixture
def make_up():
    return MakeUp()


async def test_construct_using_async_with():
    async with MakeUp() as temp_makeup:
        assert isinstance(temp_makeup, MakeUp)


async def test_strip_base_url():
    async with MakeUp('http://localhost:8000') as temp_makeup:
        assert temp_makeup.base == 'http://localhost:8000'

    async with MakeUp('http://localhost:8000') as temp_makeup_2:
        assert temp_makeup_2.base == 'http://localhost:8000'


@pytest.mark.vcr('tests/vcr_cassettes/wrap-response.yaml')
async def test_wrap_response(make_up):
    product_info = await make_up._get('lipstick')
    lipstick_url = utils.get_main_url(utils.base_url, 'lipstick', None)
    
    assert isinstance(product_info, dict)
    assert 'makeup_url' in product_info
    assert 'headers' in product_info
    assert isinstance(product_info['headers'], dict)
    assert lipstick_url == product_info['makeup_url']
    await make_up.close()


async def test_wrap_non_dict_response(make_up, aio_response_non_dict_mock):
    wrapped_response = await make_up._wrap_response(aio_response_non_dict_mock, '')

    assert isinstance(wrapped_response, dict)
    assert 'data' in wrapped_response
    assert wrapped_response['data'] == await aio_response_non_dict_mock.json()
    await make_up.close()


#product_id tests
@vcr.use_cassette("tests/vcr_cassettes/id-success.yaml")
async def test_id_success(id_keys, make_up):
    product_id_info = await make_up.product_id(1035)

    assert isinstance(product_id_info, dict)
    assert id_keys.issubset(product_id_info.keys())
    await make_up.close()

@vcr.use_cassette("tests/vcr_cassettes/id-failure.yaml")
async def test_id_failure(make_up):
    with pytest.raises(APIException):
        await make_up.product_id(-1)
    await make_up.close()


#_get req tests
@vcr.use_cassette("tests/vcr_cassettes/product-success.yaml")
async def test_product_success(product_keys, make_up):
    product_info = await make_up._get('lipstick')

    assert isinstance(product_info, dict)
    assert product_keys.issubset(product_info.keys())
    await make_up.close()

@vcr.use_cassette("tests/vcr_cassettes/product-failure.yaml")
async def test_product_failure(make_up):
    with pytest.raises(DeprecatedEndpoint):
        await make_up._get('Err')
    await make_up.close()


#tags tests
@vcr.use_cassette("tests/vcr_cassettes/tags-success.yaml")
async def test_tags_success(tags_keys, make_up):
    tags_info = await make_up.tags('organic', None, None)

    assert isinstance(tags_info, dict)
    assert tags_keys.issubset(tags_info.keys())
    await make_up.close()

@vcr.use_cassette("tests/vcr_cassettes/tags-failure.yaml")
async def test_tags_failure(make_up):
    with pytest.raises(APIException):
        await make_up.tags('Err', None, None)
    await make_up.close()


#brand tests
@vcr.use_cassette("tests/vcr_cassettes/brand-success.yaml")
async def test_brand_success(brand_keys, make_up):
    brand_info = await make_up.brand('benefit', None, None)

    assert isinstance(brand_info, dict)
    assert brand_keys.issubset(brand_info.keys())
    await make_up.close()

@vcr.use_cassette("tests/vcr_cassettes/brand-failure.yaml")
async def test_brand_failure(make_up):
    with pytest.raises(APIException):
        await make_up.brand('Err', None, None)
    await make_up.close()