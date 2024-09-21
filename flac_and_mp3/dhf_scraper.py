"""
Scrape Decibel Hall of Fame website listings into a CSV
"""
import requests
from bs4 import BeautifulSoup
import pprint
import os
import csv

# need to set agent or get a 403 response code
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'}

all_stuff = {}

for page in range(1, 8):
    if page == 1:
        url = 'https://www.decibelmagazine.com/category/hall-of-fame/'
    else:
        url = ''.join(['https://www.decibelmagazine.com/category/hall-of-fame/', 'page/', str(page), '/'])

    c = 1
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")
        # grid-loop-title1
        # grid-loop-title2
        # grid-loop-number
        # grid-loop-date
        # grid-loop-date

        stuff = []
        for p in soup.find_all("p", {"class": ["grid-loop-title1", "grid-loop-title2", "grid-loop-number", "grid-loop-date"]}):
            stuff.append(p.text.strip())
            if (c % 5) == 0:
                id = stuff[2]
                all_stuff[id] = stuff
                stuff = []
            c += 1

if not os.path.exists('../data/dhf.csv'):
    with open('../data/dhf.csv', 'w') as outpf:
        my_writer = csv.writer(outpf, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        my_writer.writerow(['Artist', 'Album', 'hof_num', 'Label', 'rel_date'])
        for i in all_stuff:
            my_writer.writerow(all_stuff[i])


