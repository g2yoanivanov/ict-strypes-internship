'''
Section 15: Web Scraping Exercises
'''

import requests
import bs4


URL = 'https://quotes.toscrape.com/page/12'
site = requests.get(URL)
soup = bs4.BeautifulSoup(site.text, 'lxml')

quotes = soup.select('.quote')
tags_box = soup.select('.tags-box')


def get_authors_on_page(quotes):
    author_names = []

    for quote in quotes:
        authors = quote.select('small.author')

        for author in authors:
            author_names.append(author.getText())

    author_names = list(set(author_names))
    return author_names


def get_quotes_page1():
    quotes_text = []

    for quote in quotes:
        quote_elements = quote.select('span.text')

        for quote_el in quote_elements:
            quotes_text.append(quote_el.getText())

    return quotes_text


def get_top10():
    top10 = []

    tags = tags_box[0].select('.tag-item')
    for tag in tags:
        top10.append(tag.getText().strip())

    return top10


def get_all_authors():
    all_authors = []

    page = 1
    while True:
        url = f'https://quotes.toscrape.com/page/{page}'
        site = requests.get(url)
        soup = bs4.BeautifulSoup(site.text, 'lxml')
        
        quotes = soup.select('.quote')

        if not quotes:
            break

        all_authors.extend(get_authors_on_page(quotes))
        page += 1

    all_authors = list(set(all_authors))
    return all_authors

print(get_all_authors())