"""
    when use soundconvertor to convert music from flac -> mp3, it does not seem to
    set tags which is inconvenient so reconstruct tags from the .flac filename
    format that ripcd / abcde produces and use mutagen to set these tags on the mp3
"""

import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, ID3NoHeaderError


def main():
    skip_list = []
    for root, folders, files in os.walk('/mydrives/hdd2/mp3'):
        for fn in files:
            if os.path.splitext(fn)[-1] == '.mp3':
                # determine artist, album, title and tracknumber from filename
                l = fn.split('-')
                artist = l[0]
                album = l[1]
                if album == 'Fluid Liquid Inversions':
                    album = 'Fluid Existential Inversions'

                title = l[-1].replace('.mp3', '')

                # TODO - does not cope when - is contained in tokens i.e. title etc
                try:
                    tracknumber = str(int(l[-2:-1][0]))
                except ValueError:
                    if fn == 'Napalm Death-Throes of Joy in the Jaws of Defeatism-12-Feral Carve-Up.mp3':
                        tracknumber = str(12)
                    if fn == 'DVNE-Etemen Ænka-07-Sì-XIV.mp3':
                        tracknumber = str(7)

                    else:
                        tracknumber = None

                if tracknumber is not None:
                    # use mutagen to add tags to the mp3
                    # mutagen is painful to use
                    # 1st we need to detect if the mp3 has a header and if not add one
                    # https://github.com/quodlibet/mutagen/issues/327
                    try:
                        tags = ID3(os.path.join(root, fn))
                    except ID3NoHeaderError:
                        tags = ID3()
                    tags.save(os.path.join(root, fn))

                    # 2nd, having added the header we can add tags to the header
                    # https://stackoverflow.com/questions/18369188/python-add-id3-tags-to-mp3-file-that-has-no-tags
                    print('Updating: ', os.path.join(root, fn))
                    meta = EasyID3(os.path.join(root, fn))
                    meta['title'] = title
                    meta['artist'] = artist
                    meta['album'] = album
                    meta['tracknumber'] = tracknumber
                    meta.save(os.path.join(root, fn), v1=2)
                else:
                    skip_list.append(fn)

    if len(skip_list) > 0:
        print('Skipped: ')
        for i in skip_list:
            print(i)


if __name__ == "__main__":
    main()

