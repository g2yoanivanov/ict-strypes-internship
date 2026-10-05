import requests
import bs4
import csv
import os

RATES_URL = 'https://taxatlas.io/tax-rates'
CSV_PATH = './tax_rates.csv'

def scrape_rates():
    """
    Scrape income tax rates from TaxAtlas.
    
    Retrieves country names and their corresponding tax rates
    and combines them into tuples

    Return:
        result: a list of (country, tax_rate) tuples
    """
    site = requests.get(RATES_URL)
    soup = bs4.BeautifulSoup(site.text, 'lxml')

    countries = soup.select('h3.font-semibold.text-white.transition-colors')
    rates = soup.select('p.text-green-400')

    countries_text = []
    rates_text = []

    for country in countries:
        countries_text.append(country.getText())

    for rate in rates:
        rates_text.append(rate.getText())

    result = list(zip(countries_text, rates_text))
    return result


def save_rates_to_csv(rates, filepath):
    """
    Save country tax rates to a CSV file.

    Creates a CSV file and writes the provided
    country/tax rate pairs, including a header row.

    Args:
        rates: Iterable of (country, tax_rate) tuples.
        filepath (str): Path of the CSV file to create.

    Returns:
        None
    """
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        writer.writerow(['Country', 'Rate'])

        for row in rates:
            writer.writerow(row)


def take_income_input():
    while True:
        try:
            user_income = int(input('Enter your income: '))

            if user_income <= 0:
                raise ValueError

        except:
            print('Please enter valid income!')

        else:
            return user_income


def take_country_input(countries):
    while True:
        try:
            user_country = input('Enter yout country: ')

            if user_country not in countries:
                raise ValueError

        except ValueError:
            print('The entry is not a country in the database')

        else:
            return user_country


def get_data_from_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            csv_data = csv.reader(f)
            lines = list(csv_data)
            return lines
        
    except FileNotFoundError:
        print('File not found!')
        return None


def get_rate(country):
    pass


def calculate_tax():
    pass


def main():
    if not os.path.exists(CSV_PATH):
        rates = scrape_rates()
        save_rates_to_csv(rates, CSV_PATH)

    countries = get_data_from_file(CSV_PATH)


if __name__ == '__main__':
    main()
