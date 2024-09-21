"""
    scrape last.fm in order to retrive gigs I attended
"""

import requests
from bs4 import BeautifulSoup
import json

gigs = {}
gig_id = 1
for y in range(1999, 2017, 1):
    # i.e. https://www.last.fm/user/blackholesunn/events/2012
    url = 'https://www.last.fm/user/blackholesunn/events/{0}'.format(str(y))
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")

        for tr in soup.find_all("tr", {"class": "events-list-item js-link-block"}):
            gig_title = (tr.find("a", {"class": "link-block-target"})).text.strip()
            gig_lineup = (tr.find("div", {"class": "events-list-item-event--lineup"})).text.strip()
            gig_lineup_list = []
            for l in gig_lineup.split('\n'):
                gig_act = (l.replace('\n', '')).strip()
                if gig_act != '':
                    #  TODO - remove trailing comma (at moment I just do global replace in the out .json!)
                    gig_lineup_list.append(gig_act)
            gig_date = (tr.find("time", {"class": "calendar-icon"})).get("datetime")
            gig_venue = (tr.find("div", {"class": "events-list-item-venue--title"})).text.strip()
            gig_venue_location_city = (tr.find("div", {"class": "events-list-item-venue--city"})).text.strip()
            gig_venue_location_country = (tr.find("div", {"class": "events-list-item-venue--country"})).text.strip()

            gigs[gig_id] = {
                'gig_date': gig_date,
                'gig_title': gig_title,
                'gig_lineup': gig_lineup_list,
                'gig_venue': gig_venue,
                'gig_venue_location_city': gig_venue_location_city,
                'gig_venue_location_country': gig_venue_location_country
            }
            gig_id += 1

with open('../data/lastfm_gigs.json', 'w') as outpf:
    outpf.write(json.dumps(gigs, indent=4))







