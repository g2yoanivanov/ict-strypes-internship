from abc import ABC, abstractmethod


class Scraper(ABC):
    """
    Abstract base class for all the web scrapers. 
    """
    URL = None
    DATA_TYPE = None
    PATH = None

    def __init__(self):
        self.stats = {
            'site': self.URL,
            'data type': self.DATA_TYPE,
            'records': 0,
            'saved to': self.PATH
        }

    @abstractmethod
    def scrape(self):
        """
        Retrieve data from the selected source.
        """

    @abstractmethod
    def save_data(self):
        """
        Write the scraped data to a CSV file.
        """
