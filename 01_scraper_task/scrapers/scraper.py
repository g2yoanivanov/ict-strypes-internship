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

    def __str__(self):
        info = f"Site scraped: {self.URL}\n" \
        f"File location: {self.PATH}\n" \
        f"Data types: {self.DATA_TYPE}"
        
        return info