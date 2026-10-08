from bs4 import BeautifulSoup
import requests
import os

from .scraper import Scraper

from exceptions.scraping_exception import ScrapingException


class MerchScraper(Scraper):
    """
    Scraper class for F1 Merch.
    """
    URL = 'https://fanraces.bg/category/formula-1?page={}'
    DATA_TYPE = [
        'Item Name',
        'Item Price',
        'Item Link'
    ]
    PATH = os.path.join('.', 'data', 'f1_merch.csv')

    def __init__(self):
        super().__init__()

    def scrape(self):
        result = []
        page = 1

        while True:
            response = requests.get(self.URL.format(page))

            if response.status_code == 404:
                break

            else:
                response.raise_for_status()

            soup = BeautifulSoup(response.text, 'lxml')

            section = soup.select_one('._products-list')

            if section is None:
                raise ScrapingException('Could not find item section')

            for tag in section.select('._product-price-old'):
                tag.decompose()

            for tag in section.select('._product-discount._product-discount-fixed'):
                tag.decompose()

            item_tags = section.select('h3 a')
            price_tags = section.select('.bgn2eur-primary-currency')

            items = [item.getText() for item in item_tags]
            prices = [price.getText() for price in price_tags]
            print(prices)
            links = [link['href'] for link in item_tags]

            if len(items) == len(prices) == len(links):
                self.stats['records'] += len(items)

                records = list(zip(items, prices, links))
                result.extend(records)

            else:
                raise ScrapingException(
                    'Mismatched data counts: '
                    f'items: {len(items)} '
                    f'prices: {len(prices)} '
                    f'links: {len(links)} '
                )

            page += 1

        return result
