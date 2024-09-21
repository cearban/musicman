import os

mg_pth = 'G:\\flac'
lcl_pth = 'F:\\flac'

for root, folders, files in os.walk(lcl_pth):
    for fld in folders:
        if not os.path.exists(os.path.join(mg_pth, fld)):
            print(os.path.join(lcl_pth, fld))





