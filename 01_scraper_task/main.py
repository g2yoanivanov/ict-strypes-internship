"""
CLI implementation.
"""

from scrapers.news_scraper import NewsScraper
from scrapers.calendar_scraper import CalScraper
from scrapers.merch_scraper import MerchScraper

from writers.csv_writer import CSVWriter
from writers.json_writer import JSONWriter

from exceptions.file_write_exception import FileWriteException
from exceptions.scraping_exception import ScrapingException

import requests


INFO = "Options:\n" \
    "0. Exit\n" \
    "1. F1 News: MotorSport.com\n" \
    "2. F1 Calendar: F1-Fansite.com\n" \
    "3. F1 Merch: Fanraces.bg"

EXTENSIONS = "Supported file formats:\n" \
            "1. CSV\n" \
            "2. JSON"


def get_user_input():
    """
    Get user's choice (site to scrape ot exit).
    """
    while True:
        try:
            print(INFO)
            option = input('Enter a number: ')
            print()

            if option not in ['0', '1', '2', '3']:
                raise ValueError

        except ValueError:
            print()
            print('Invalid option')
            print()

        else:
            return option

def get_extension():
    while True:
        try:
            print(EXTENSIONS)
            option = input('Enter a number: ')
            print()
    
            if option not in ['1', '2']:
                raise ValueError
    
        except ValueError:
            print()
            print('Invalid option')
            print()
    
        else:
            if option == '1':
                return 'csv'

            elif option == '2':
                return 'json'


def create_writer(extension):
    if extension == 'csv':
        return CSVWriter()

    if extension == 'json':
        return JSONWriter()


def main():
    """
    Run the scraper application.

    Displays the user menu, executes the selected scraper,
    saves the extracted data to a file, and prints a
    summary of the scraping results.
    """
    #TODO: Change to session_summary = []
    session_stats = {
        'news': None,
        'calendar': None,
        'merch': None
    }

    #TODO: stat_key is not needed
    stat_key = None
    successful_scrape = False
    total_records = 0

    first_call = True

    print('SCRAPING F1')
    print()
    while True:
        try:
            data = None
            header = None
            path = None
            scraper = None

            option = get_user_input()
            
            if option == '0':
                print('Session summary:')
                #TODO: for x in session_summary: print(x)
                # And remove the session_stats logic
                for _, val in session_stats.items():
                    if val is not None:
                        print(val)
                        print()

                print(f'Total records extracted: {total_records}')
                break

            extension = get_extension()
            writer = create_writer(extension)

            if option == '1':
                scraper = NewsScraper(extension)
                stat_key = 'news'

            elif option == '2':
                scraper = CalScraper(extension)
                stat_key = 'calendar'

            elif option == '3':
                scraper = MerchScraper(extension)
                stat_key = 'merch'

            print('Extracting data...')

            data = scraper.scrape()
            header = scraper.DATA_TYPE
            path = scraper.PATH.format(extension)

            print('Saving to file...')
            writer.save_data(header, data, path, first_call)

            print()
            print('Done!')
            print()
            print('Summary:')

            print(scraper)
            print(f'Records extracted: {scraper.stats['records']}')
            total_records += scraper.stats['records']
    
            print()

        except requests.RequestException as e:
            print(f'Network error: {e}')

        except ScrapingException as e:
            print(f'Scraping error: {e}')

        except FileWriteException as e:
            print(f'File error: {e}')

        except Exception as e:
            print(f'Unexpected error: {e}')

        else:
            successful_scrape = True

        finally:
            if successful_scrape:
                #TODO: Change to session_summary.appen(str(scraper))
                session_stats[stat_key] = str(scraper)

            if first_call:
                first_call = False


if __name__ == '__main__':
    main()
