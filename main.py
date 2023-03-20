from abc import ABC, abstractmethod
import aiohttp
from fake_headers import Headers


class WebSite(ABC):
    headers = Headers(headers=True).generate()

    def __init__(self, base_url: str, news_url: str):
        self.base_url = base_url
        self.news_url = news_url

    async def get_response(self, request_url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(request_url, headers=self.headers) as resp:
                return await resp.text()

    async def send_post(self, request_url: str, data=None):
        if data is None:
            data = {}
        async with aiohttp.ClientSession() as session:
            async with session.post(request_url, data=data) as response:
                try:
                    data = await response.json(encoding='utf-8')
                    return data
                except:
                    return await response.text()

    @abstractmethod
    def get_posts(self):
        ...

    @abstractmethod
    def get_posts_content(self, *args):
        ...

    def get_comments(self, *args):
        ...
