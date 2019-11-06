#!/usr/bin/env python3

from string import ascii_lowercase
from random import sample

import requests
from bs4 import BeautifulSoup

URL_TEMPLATE = 'http://phrontistery.info/{}.html'
ALPHABET = list(ascii_lowercase)
BS_PARSER = 'html5lib'

alphabet_pages = [URL_TEMPLATE.format(letter) for letter in ALPHABET]
url = sample(alphabet_pages, 1)[0]
request = requests.get(url)
soup = BeautifulSoup(request.content, BS_PARSER)
table = soup.find_all("table", {"class": "words"})[0]
words = [[td.get_text(strip=True) for td in tr.find_all('td')] for tr in table.find_all('tr')]
words.pop(0)
word = sample(words, 1)[0]

print(
    f'''
    Your sesquipedalian word of the day is: {word[0]}
    Its definition is: {word[1]}
    '''
)
