import taglib
import os
import csv

# TODO update for win10
p = '/home/james/Desktop/Music'

problems = []

with open('../data/all_flac.csv', 'w') as outpf:
    my_writer = csv.writer(outpf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    my_writer.writerow(['artist', 'album', 'song', 'location'])
    for root, folders, files in os.walk(p):
        for f in files:
            if os.path.splitext(f)[-1] == ".flac":
                fn = os.path.join(root, f)
                s = taglib.File(fn)

                have_artist, have_album, have_title = True, True, True

                # TODO use albumartist rather than artist since this is what
                #  AIMP uses to group by artist
                try:
                    artist = s.tags['ARTIST'][0]
                except KeyError:
                    artist = 'Unknown'
                    have_artist = True

                try:
                    album = s.tags['ALBUM'][0]
                except KeyError:
                    album = 'Unknown'
                    have_album = True

                try:
                    title = s.tags['TITLE'][0]
                except KeyError:
                    title = 'Untitled'
                    have_title = True

                if have_artist and have_album and have_title:
                    my_writer.writerow([artist, album, title, fn])
                else:
                    problems.append({
                        'fn': fn,
                        'have_artist': have_artist,
                        'have_album': have_album,
                        'have_title': have_title
                    })

if len(problems) > 0:
    print('Had problems fetching tags from this lot:')
    for p in problems:
        print(p)






