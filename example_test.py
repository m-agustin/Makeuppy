from pprint import pprint

import asyncio

from makeuppy.aio_makeup import MakeUp


make_up = MakeUp()


async def main():
    async with MakeUp() as make_up:
        blush_powder = await make_up._get(endpoint='blush', extension='powder')
        pprint(blush_powder)

        vegan = await make_up.tags(product_tags='vegan', product_type='bronzer', product_category='powder')
        pprint(vegan)
        
asyncio.run(main())
