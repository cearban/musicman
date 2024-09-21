"""
    update tags in .flac`s
    i.e. so that we can standardise the tags in music collection

    tags that abcde has set and that we can update are:
    title, tracktotal, album, artist, tracknumber, genre, cddb, date

    e.g. at moment in my flac collection, rhythmbox lists BTBAM under artist as:
    Between the Buried and Me
    Between The Buried And Me
    BetweenThe Buried And Me

    we just want:

    Between The Buried And Me

    240421: set_albumartist_if_missing(fn) deals with files where artist is set
    but albumartist is missing. AIMP uses albumartist rather than artist for
    grouping by artist etc
"""

import os
from mutagen.flac import FLAC
import csv
import glob

# def fetch_fix_lookups():
#     lu = {}
#     with open('../data/update_list_triad_woes.csv', 'r') as inpf:
#         my_reader = csv.DictReader(inpf)
#         for r in my_reader:
#             norm_to_update = r['norm_to_update']
#             current = r['current']
#             lu[current] = norm_to_update
#
#     return lu
#
#
# for root, folders, files in os.walk('/home/james/Desktop/Music'):
#     for fn in files:
#         if os.path.splitext(fn)[-1] == '.flac':
#             my_flac = FLAC(os.path.join(root, fn))
#             if my_flac["artist"][0] in fix_lu:
#                 my_flac["artist"] = fix_lu[my_flac["artist"][0]]
#                 my_flac.save()


def set_albumartist_if_missing(fn):
    """
    in some cases there were .flac files where the artist tag was
    present and populated but there was no albumartist tag. Where
    there was no albumartist tag present AIMP grouped the file under
    None category rather than artist which was annoying so did this
    to scan all flac files for missing albumartist and then set this
    to artist.

    then removed ALL files from AIMP library db and readded them all
    again.

    This appears to have fixed things.

    :param fn:
    :return:
    """

    has_artist = False
    artist = None
    has_albumartist = False

    my_flac = FLAC(fn)

    if 'artist' in my_flac.tags.keys():
        has_artist = True
        artist = my_flac.tags['artist'][0]

    if 'albumartist' in my_flac.tags.keys():
        has_albumartist = True

    if not has_albumartist:
        if has_artist:
            if artist is not None:
                print('For {} setting albumartist --> {}'.format(
                    fn,
                    artist
                ))
                my_flac["albumartist"] = artist
                my_flac.save()


def main():
    for root, folders, files in os.walk('F:\\flac'):
        for fn in files:
            if os.path.splitext(fn)[-1] == '.flac':
                set_albumartist_if_missing(os.path.join(root, fn))


if __name__ == "__main__":
    main()















