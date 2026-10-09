"""
Formula 1 calendar scraper implementation.
"""

from itertools import zip_longest
import os
import datetime
import requests
from bs4 import BeautifulSoup

from exceptions.scraping_exception import ScrapingException

from .scraper import Scraper


class CalScraper(Scraper):
    """
    Scraper class for F1 calendar.

    Extracted data:
        Grand Prix: Official name of the Formula 1 Grand Prix
        Race Circuit: Name of the circuit on which the race is held
        Race Date: Scheduled date of the race weekend
        Race Winner: Winning driver of the race, or 'TBD' if the race has not yet taken place.
    """
    # 2013 - 2027
    URL = 'https://www.f1-fansite.com/f1-calendar/{}-f1-calendar/'
    # 1950 - 2012
    # https://www.f1-fansite.com/f1-calendar/f1-{}-calendar-schedule/
    DATA_TYPE = [
        'Grand Prix',
        'Race Circuit',
        'Race Date',
        'Race Winner'
    ]
    PATH = os.path.join('.', 'data', 'f1_calendar.csv')

    def scrape(self):
        year = datetime.date.today().year
        result = []

        while True:
            response = requests.get(self.URL.format(year), timeout=10)

            if response.status_code == 404:
                break

            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'lxml')

            races = soup.select_one('.f1fs-race-calendar')

            if races is None:
                raise ScrapingException('Could not find race calendar')

            grand_prix_tags = races.select('.f1fs-race-name-long')
            circuit_tags = races.select('.f1fs-race-meta__circuit')
            date_tags = races.select('.f1fs-race-meta__date')
            winner_tags = races.select('.f1fs-race-winner__driver')

            grand_prix = [gp.getText() for gp in grand_prix_tags]
            circuits = [circuit.getText() for circuit in circuit_tags]
            winners = [winner.getText() for winner in winner_tags]

            dates = []
            for tag in date_tags:
                time = tag.select_one('time')
                date = time['datetime']
                dates.append(date)

            if len(winners) > len(grand_prix):
                raise ScrapingException(
                    'Mismatched data counts: '
                    f'Grand Prix: {len(grand_prix)} '
                    f'Winners: {len(winners)} '
                )

            if len(grand_prix) == len(circuits) == len(dates):
                self.stats['records'] += len(grand_prix)

                records = list(zip_longest(grand_prix, circuits, dates, winners, fillvalue='TBD'))
                result.extend(records)

            else:
                raise ScrapingException(
                    'Mismatched data counts: '
                    f'Grand Prix: {len(grand_prix)} '
                    f'Circuits: {len(circuits)} '
                    f'Dates: {len(dates)} '
                )

            year -= 1

        return result
