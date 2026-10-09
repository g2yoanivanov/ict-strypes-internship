"""
Formula 1 News scraper implementation.
"""

import os
from itertools import zip_longest
import requests
from bs4 import BeautifulSoup

from exceptions.scraping_exception import ScrapingException

from .scraper import Scraper


class NewsScraper(Scraper):
    """
    Scraper class for F1 news.

    Extracted data:
        Article Title: Headline of the news article
        Article Time: Time elapsed between the article's 
        publication and the moment of data extraction
        Article Link: URL leading to the full article
    """
    URL = 'https://www.motorsport.com/f1/news/'
    DATA_TYPE = [
        'Article Title',
        'Article Time',
        'Article Link'
    ]
    PATH = os.path.join('.', 'data', 'f1_news.{}')

    def scrape(self):
        response = requests.get(self.URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')

        articles = soup.select_one('.ms-grid')

        if articles is None:
            raise ScrapingException('Could not find article section')

        title_tags = articles.select('.ms-item__title')
        link_tags = articles.select('a')
        time_tags = articles.select('.ms-item__date')

        titles = [title.getText() for title in title_tags]
        times = [time.getText().strip() for time in time_tags]

        links = []
        for link in link_tags:
            # Most of the articles are in the MotorSport site (and the link is not full)
            # But there are cases where links redirect you to other sites
            full_link = 'https://www.motorsport.com/' + link['href']

            if link['href'].startswith('http'):
                full_link = link['href']

            links.append(full_link)

        if len(times) > len(titles):
            raise ScrapingException(
                'Mismatched data counts: '
                f'titles: {len(titles)} '
                f'times: {len(times)} '
            )

        if len(titles) == len(links):
            self.stats['records'] = len(titles)

            result = list(zip_longest(titles, times, links, fillvalue='N/A'))
            return result


        raise ScrapingException(
            'Mismatched data counts: '
            f'titles: {len(titles)} '
            f'links: {len(links)} '
        )
