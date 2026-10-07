from bs4 import BeautifulSoup
from itertools import zip_longest
import requests
import os
import datetime

from .scraper import Scraper

from exceptions.scraping_exception import ScrapingException


class CalScraper(Scraper):
    """
    Scraper class for F1 calendar
    """
    # 2013 - 2027
    URL = 'https://www.f1-fansite.com/f1-calendar/{}-f1-calendar/'
    # 1950 - 2012
    # https://www.f1-fansite.com/f1-calendar/f1-{}-calendar-schedule/
    DATA_TYPE = [
        'Grand Prix',
        'Circuit',
        'Date',
        'Winner'
    ]
    PATH = os.path.join('.', 'data', 'f1_calendar.csv')

    def __init__(self):
        super().__init__()

    def scrape(self):
        year = datetime.date.today().year
        result = []

        while True:
            response = requests.get(self.URL.format(year))

            if response.status_code == 404:
                break

            else:
                response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')

            races = soup.select_one('.f1fs-race-calendar')

            if races is None:
                raise ScrapingException('Could not find race calendar')

            grand_prix_tags = races.select('.f1fs-race-name-long')
            circuit_tags = races.select('.f1fs-race-meta__circuit')
            date_tags = races.select('.f1fs-race-meta__date')
            winner_tags = races.select('.f1fs-race-winner__driver')

            grand_prix = []
            circuits = []
            dates = []
            winners = []

            for gp in grand_prix_tags:
                grand_prix.append(gp.getText())

            for circuit in circuit_tags:
                circuits.append(circuit.getText())

            for tag in date_tags:
                time = tag.select_one('time')
                date = time['datetime']
                dates.append(date)

            for winner in winner_tags:
                winners.append(winner.getText())

            if len(winners) > len(grand_prix):
                raise ScrapingException(
                    'Missmatched data counts: '
                    f'Grand Prix: {len(grand_prix)} '
                    f'Winners: {len(winners)} '
                )

            elif len(grand_prix) == len(circuits) == len(dates):
                self.stats['records'] += len(grand_prix)

                calendar = list(zip_longest(grand_prix, circuits, dates, winners, fillvalue='TBD'))
                result.extend(calendar)

            else:
                raise ScrapingException(
                    'Missmatched data counts: '
                    f'Grand Prix: {len(grand_prix)} '
                    f'Circuits: {len(circuits)} '
                    f'Dates: {len(dates)} '
                )

            year -= 1

        return result
