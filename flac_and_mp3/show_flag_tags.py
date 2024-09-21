import taglib
import glob
import os


def show_tags(pth):
    for fn in glob.glob(os.path.join(pth, '*.flac')):
        song = taglib.File(fn)
        print(fn, song.tags.keys(), song.tags['ALBUMARTIST'])
        #print(song.tags.keys())
        #print(song.tags)


show_tags(pth='F:\\flac\\Wayfarer - A Romance With Violence')