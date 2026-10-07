from bs4 import BeautifulSoup
import requests
import os

from .scraper import Scraper

from exceptions.scraping_exception import ScrapingException


class DriverScraper(Scraper):
    URL = 'https://www.autosport.com/f1/drivers/?y={}'
    DATA_TYPE = [
        'Name',
        'Number',
        'Team',
        'Birthdate',
        'Nationality'
    ]

    def __init__(self):
        super().__init__()