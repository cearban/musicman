import csv
import json
import datetime

gigs = {}
gig_id = 1

cutoff_date = datetime.date(year=2016, month=3, day=19)

unq_locns = []

locns_lookup = {
    'Audio': 'Audio',
    'BL': 'The Banshee Labyrinth',
    'BM': 'Bannermans',
    'BM`s': 'Bannermans',
    'BMs': 'Bannermans',
    'BarrowL': 'Barrowland Ballroom',
    'Berkeley': '',
    'CG': 'The Classic Grand',
    'Cathouse': 'The Cathouse',
    'Drygate': 'Drygate Brewery',
    'Garage': 'The Garage',
    'Glasgow': '',
    'Henry`s': "Henry's Cellar Bar",
    'Henrys': "Henry's Cellar Bar",
    'LBA': 'La Belle Angele',
    'LDN': '',
    'Leeds': '',
    'Londinium': '',
    'MCR': '',
    'O2 Academy': 'O2 Academy Glasgow',
    'OL': '',
    'Opium': 'Opium',
    'QMU': 'Queen Margaret Union',
    'QueensHall': "The Queen's Hall",
    'S24': 'Studio 24',
    'SH': 'Summerhall',
    'SL': "St Luke's",
    'Sheffield': '',
    'Smash': 'Smash',
    "St Luke's": "St Luke's",
    'Stereo': 'Stereo',
}

more_locns_lookup = {
    'Alcest (Glasgow)': '',
    'BTBAM (MCR)': '',
    'Conjurer (Sheffield)': '',
    'Cult of Luna (LDN)': '',
    'Damnation Fest (Leeds)': 'Leeds University Union',
    'Damnation Festival (Leeds)': 'Leeds University Union',
    'Dream Theater (Glasgow)': '',
    'Dream Theater (MCR)': '',
    'Metal Festival Alliance (OL)': '',
    'Mithras (Glasgow)': '',
    'Neurosis (Berkeley)': '',
    'Neurosis (Londinium)': '',
    'Pallbearer (MCR)': '',
    'Ritual Fest pre-show (Leeds)': '',
    'Ritual Festival (Leeds)': '',
    'Yob (Glasgow)': ''
}

with open('../data/james.rc.crone@googlemail.com.csv', 'r') as inpf:
    my_reader = csv.DictReader(inpf)
    for r in my_reader:
        gig_date = ((r['Start Time']).split(' '))[0]
        (gig_date_yr, gig_date_mo, gig_date_day) = gig_date.split('-')
        gig_date_obj = datetime.date(year=int(gig_date_yr), month=int(gig_date_mo), day=int(gig_date_day))
        if gig_date_obj >= cutoff_date:
            #print('\t gig_date:', gig_date, gig_date_obj)

            gig_title = (r['Summary'])[2:-1]
            gig_title_has_locn = False

            if '(' in gig_title:
                if ')' in gig_title:
                    gig_title_has_locn = True

            if gig_title_has_locn:
                locn = gig_title[gig_title.find('(')+1:gig_title.find(')')]
                if locn != '0!':
                    #if locn not in unq_locns:
                    #    unq_locns.append(locn)
                    normalised_locn = locns_lookup[locn]
                    if normalised_locn == '':
                        print(gig_title, gig_date)
                        #print('HasLocn: ', gig_title, locn, '-->!', normalised_locn, '!')
            else:
                pass
                #print('!Locn: ', gig_title)

            gig_location = r['Location']

            gig_lineup_list = []
            gig_venue = None
            gig_venue_location_city = None
            gig_venue_location_country = None

            gigs[gig_id] = {
                'gig_date': gig_date,
                'gig_title': gig_title,
                'gig_lineup': gig_lineup_list,
                'gig_venue': gig_venue,
                'gig_venue_location_city': gig_venue_location_city,
                'gig_venue_location_country': gig_venue_location_country
            }
            gig_id += 1

with open('../data/google_cal_gigs.json', 'w') as outpf:
    outpf.write(json.dumps(gigs, indent=4))

#for l in sorted(unq_locns):
#    print(l)




