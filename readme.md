# Makeuppy

A simple asynchronous wrapper for [MakeUp](http://makeup-api.herokuapp.com/) api

Base: http://makeup-api.herokuapp.com/api/v1/products.json
Session: aiohttp.ClientSession

# The parameters according to the API:
Parameter | Data Type | Description
--- | --- | ---
product_type | _string_ | The type of makeup being searched for (ie. lipstick, eyeliner). See list of product types below. Will return a list of all products of this type
product_category | _string_ | Sub-category for each makeup-type. (ie. lip gloss is a category of lipstick). See product types below. If a category exists it will be under 'By Category'. Will return a list of all products of this category
product_tags | _string_ | list separated by commas
brand | _string_ | Brand of the product. Will return all products for each brand


# Usage example:
        import asyncio
        from aio_makeup import MakeUp

        async def main():
            async with MakeUp() as make_up:
                blush_powder = await make_up._get(endpoint='blush', extension='powder')
                vegan = await make_up.tags(product_tags='vegan', product_type='bronzer', product_category='powder')
                
        asyncio.run(main())