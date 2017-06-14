import os
import requests
import shutil

#TODO: Modift this file so it saves with random names and modifies saves refrences to files images already downloaded
def download_image(url, path):
    r = requests.request('GET', url, stream=True)
    with open(path, 'wb') as out_file:
        shutil.copyfileobj(r.raw, out_file)
    del r

