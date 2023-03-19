from typing import List

import asyncio
from bs4 import BeautifulSoup

from main import WebSite


class Baigenews(WebSite):
    source = 'baigenews'

    def __init__(self, base_url: str, news_url: str):
        super().__init__(base_url, news_url)

    async def get_posts_content(self, links: List[str]) -> List[dict]:
        data = []
        for link in links:
            response = await self.get_response(link)
            soup = BeautifulSoup(response, 'html5lib')

            container = soup.find('div', class_='custom-container').find('div', 'detail__text__container__alltext')
            tags = soup.find('div', class_='nl__details').find_all('a', href=True)
            data.append(
                {
                    'id': link[20:],
                    'source': self.source,
                    'created': soup.find('meta', property='article:published_time')['content'],
                    'text': ([p.text.strip() for p in container.find_all('p')]),
                    'url': link,
                    'tags':  [tag.text.replace('#', '').lower() for tag in tags],
                    'comments': ['']
                }
            )
        return data

    async def get_posts(self) -> List[dict]:
        response = await self.get_response(self.news_url)
        soup = BeautifulSoup(response, 'html5lib')

        container = soup.find('div', class_='uk-container list-page-search')
        links = [a['href'] for a in container.find_all('a',
                                                       class_='finded__content__item__link uk-flex',
                                                       href=True)]
        return await self.get_posts_content(links)
