# http://quotes.toscrape.com/

import csv
import requests
from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com/')
html_data = BeautifulSoup(response.text, features="html.parser")
quotes = html_data.find_all(class_='quote')


with open('New_Scraping_File.csv', 'w', newline='', encoding='utf-8') as scrap_file:
    headers_list = ['text', 'author', 'keywords']
    writer = csv.DictWriter(scrap_file, fieldnames=headers_list, delimiter=";")
    writer.writeheader()

    for quote in quotes:
        print(quote.find(class_='text').get_text())
        print(quote.find(class_='author').get_text())
        print(quote.find(class_='keywords')['content'])
        writer.writerow({
            'text': quote.find(class_='text').get_text(),
            'author': quote.find(class_='author').get_text(),
            'keywords': quote.find(class_='keywords')['content']
        })

        # writer.writerow({'text': quote.find(class_='text').get_text()})
        # writer.writerow({'author': quote.find(class_='author').get_text()})
        # writer.writerow({'keywords': quote.find(class_='keywords')['content']})
