from postgres import Postgres
import csv

db = Postgres('postgresql://james:MopMetal3@localhost:5432/musicman')
sql = 'SELECT distinct artist, album FROM music_library.flac_files ORDER BY artist'

artist_albums = []

rs = db.all(sql)
for r in rs:
    artist_albums.append(':'.join([r[0], r[1]]))

c = 0
mags_owned = 0

total_hof_entries = 1

# TODO the comparison test is missing some matches, needs to lcase etc...
with open('../data/dhf.csv', 'r') as inpf:
    my_reader = csv.DictReader(inpf)
    for r in my_reader:
        total_hof_entries += 1
        hof_album = ':'.join([r['Artist'], r['Album']])
        if hof_album in artist_albums:
            hof_num = int((r['hof_num']).replace('dB HoF No. ', ''))

            if hof_num >= 94:
                print(r['Artist'], '-->', r['Album'], '-->', r['hof_num'], '(*)')
                mags_owned += 1
            else:
                print(r['Artist'], '-->', r['Album'], '-->', r['hof_num'])
            c += 1

print('\nOf the {} Decibel Hall of Fame Albums \m/ \m/'.format(total_hof_entries))
print('I own {} '.format(c))
print('{} of which I own the mags for'.format(mags_owned))
print('Maybe check what albums are covered in the books!')




