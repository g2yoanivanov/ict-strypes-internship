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
            'records': 0,
        }

    @abstractmethod
    def scrape(self):
        """
        Retrieve data from the selected source.
        """

    def __str__(self):
        data_type_str = "".join(
            f"- {data}\n"
            for data in self.DATA_TYPE
        )

        info = f"Site scraped: {self.URL}\n" \
        f"File location: {self.PATH}\n" \
        f"Data types extracted:\n" \
        f"{data_type_str}"

        return info