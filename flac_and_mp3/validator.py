import re
from postgres import Postgres
import csv


def normaliser(inStr):
    # TODO something like https://labrosa.ee.columbia.edu/projects/musicsim/normalization.html
    #  or https://musicbrainz.org/doc/Style/Language/English

    outStr = None
    outStr = re.sub("\s+", "", inStr.lower())

    return outStr


def validate_artist_tags():
    variants = {}
    db = Postgres('postgresql://james:MopMetal3@localhost:5432/musicman')

    sql = 'SELECT distinct artist FROM music_library.flac_files ORDER BY artist'

    rs = db.all(sql)
    for r in rs:
        artist = r
        normalised_artist = normaliser(artist)
        if normalised_artist in variants:
            variants[normalised_artist].append(artist)
        else:
            variants[normalised_artist] = [artist]

    with open('/home/james/Desktop/variants.csv', 'w') as outpf:
        my_writer = csv.writer(outpf, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        my_writer.writerow(['norm_to_update', 'current'])

        for variant in sorted(variants.keys()):
            for vv in variants[variant]:
                my_writer.writerow([variant, vv])



def main():
    validate_artist_tags()


if __name__ == "__main__":
    main()





