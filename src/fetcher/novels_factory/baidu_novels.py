# -*- coding:utf-8 -*-

import aiohttp
import async_timeout
import asyncio

from src.fetcher.novels_factory.base_novels import BaseNovels
from src.fetcher.functions import get_random_user_agent


class BaiduNovels(BaseNovels):

    def __init__(self):
        super(BaiduNovels, self).__init__()

    async def data_extraction(self, html):
        pass

    async def get_real_url(self, url):
        pass

    async def novels_search(self, novels_name):
        url = self.config.URL_PC
        params = {'wd': novels_name, 'ie': 'utf-8', 'rn': self.config.BAIDU_RN, 'vf_bl': 1}
        headers = {'user-agent': await get_random_user_agent()}
        html = await self.fetch_url(url=url, params=params, headers=headers)
        print(html)


async def start(novels_name):
    return await BaiduNovels.start(novels_name)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start('雪中悍刀行'))
