import os

all = {}

if os.path.exists('data/Owned_DVDs.csv'):
    media_type = None
    with open('data/Owned_DVDs.csv', 'r') as inpf:
        for l in inpf:
            d = l[0:l.find('\n')+1]
            d = d.replace('\n', '')
            if d[0] == '#':
                media_type = d[1:]
            else:
                #print(d, media_type)
                if d not in all:
                    all[d] = [media_type]
                else:
                    all[d].append(media_type)

for k in sorted(all.keys()):
    tags = all[k]
    if len(tags) > 1:
        print('>>>', k, all[k])
    else:
        print(k, all[k])







