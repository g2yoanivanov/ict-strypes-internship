from bs4 import BeautifulSoup
import requests
import os

from .scraper import Scraper

from exceptions.scraping_exception import ScrapingException


class NewsScraper(Scraper):
    """
    Scraper class for F1 news.
    """
    URL = 'https://www.motorsport.com/f1/news/'
    DATA_TYPE = [
        'Article Titles',
        'Article Links',
        'Article Times'
    ]
    PATH = os.path.join('.', 'data', 'f1_news.csv')

    def __init__(self):
        super().__init__()

    def scrape(self):
        response = requests.get(self.URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')

        articles = soup.select_one('.ms-grid')

        if articles is None:
            raise ScrapingException('Could not find article section')

        title_tags = articles.select('.ms-item__title')
        link_tags = articles.select('a')
        time_tags = articles.select('.ms-item__date')

        titles = []
        links = []
        times = []

        for title in title_tags:
            titles.append(title.getText())

        for link in link_tags:
            full_link = 'https://www.motorsport.com/' + link['href']
            links.append(full_link)

        for time in time_tags:
            times.append(time.getText().strip())

        if len(titles) == len(links) == len(times):
            self.stats['records'] = len(titles)

            result = list(zip(titles, links, times))
            return result

        else:
            raise ScrapingException(
                'Missmatched data counts: '
                f'titles: {len(titles)} '
                f'links: {len(links)} '
                f'times: {len(times)} '
            )
