import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')
html_data = BeautifulSoup(response.text, 'html.parser')
quotes = html_data.find_all(class_='quote')


for quote in quotes:
    print('_________________________________________')
    print(quote.find(class_='text').get_text())
    print(quote.find(class_='author').get_text())
    print(quote.find(class_='keywords')['content'])
