from scrapers.news_scraper import NewsScraper
from scrapers.calendar_scraper import CalScraper
from scrapers.merch_scraper import MerchScraper

from data_writer import Writer

from exceptions.file_write_exception import FileWriteException
from exceptions.scraping_exception import ScrapingException

import requests


INFO = "Options:\n" \
    "0. Exit\n" \
    "1. F1 News: MotorSport.com\n" \
    "2. F1 Calendar: F1-Fansite.com\n" \
    "3. F1 Merch: Fanraces.bg"


def get_user_input():
    while True:
        try:
            print(INFO)
            option = input('User choice: ')
            print()

            if option not in ['0', '1', '2', '3']:
                raise ValueError
            
        except ValueError:
            print()
            print('Invalid option')
            print()

        else:
            return option


def main():
    writer = Writer()

    session_stats = {
        'news': 0,
        'calendar': 0,
        'merch': 0
    }

    successful_scrape = False

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
                for _, val in session_stats.items():
                    if val != 0:
                        print(val)
                        print()

                break

            if option == '1':
                scraper = NewsScraper()
                stat_key = 'news'

            elif option == '2':
                scraper = CalScraper()
                stat_key = 'calendar'

            elif option == '3':
                scraper = MerchScraper()
                stat_key = 'merch'

            print('Extracting data...')

            data = scraper.scrape()
            header = scraper.DATA_TYPE
            path = scraper.PATH

            print('Saving to file...')
            writer.save_data(header, data, path)

            print()
            print('Done!')
            print()
            print('Summary:')

            for key, val in scraper.stats.items():
                print(f'{key.title()}: {val}')
                
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
                session_stats[stat_key] = str(scraper)


if __name__ == '__main__':
    main()