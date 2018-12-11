import taglib
import os

p = "/home/james/Desktop/Agalloch - The Mantle"

for root, folders, files in os.walk("/home/james/Desktop/Agalloch - The Mantle"):
    for f in files:
        if os.path.splitext(f)[-1] == ".flac":
            fn = os.path.join(root, f)
            song = taglib.File(fn)
            print(song.tags)

