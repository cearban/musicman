import json
from postgres import Postgres

db = Postgres('postgresql://james:MopMetal3@localhost:5432/musicman')

sql = 'SELECT distinct artist FROM music_library.flac_files ORDER BY artist'

known_artists = []

rs = db.all(sql)
for r in rs:
    if r not in known_artists:
        known_artists.append(r)

#print(known_artists)

gig_title_artists_not_known = []

with open('../data/lastfm_and_google_cal_sorted.json', 'r') as inpf:
    data = json.load(inpf)
    for k in sorted(data.keys()):
        gig_date = k[:10]
        gig_title = data[k]["gig_title"]
        gig_lineup = data[k]["gig_lineup"]
        gig_venue = data[k]["gig_venue"]
        gig_venue_location_city = data[k]["gig_venue_location_city"]
        gig_venue_location_country = data[k]["gig_venue_location_country"]
        #print(gig_date)
        #print(gig_title)
        if gig_title not in known_artists:
            if gig_title not in gig_title_artists_not_known:
                gig_title_artists_not_known.append(gig_title)

if len(gig_title_artists_not_known) > 0:
    for i in sorted(gig_title_artists_not_known):
        print(i)






