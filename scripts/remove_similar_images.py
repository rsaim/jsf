"""# Removing Duplicate Images Using imagehash"""
# Inspired from https://github.com/JohannesBuchner/imagehash repository

import numpy as np
import os
import imagehash
from PIL import Image, UnidentifiedImageError
import numpy as np
from sys import argv


dir = os.path.realpath(argv[1])
os.chdir(dir)
print(f"Removing duplicate files in {dir}")

file_list = os.listdir()
duplicates = []
hash_keys = dict()

def alpharemover(image):
    if image.mode != 'RGBA':
        return image
    canvas = Image.new('RGBA', image.size, (255,255,255,255))
    canvas.paste(image, mask=image)
    return canvas.convert('RGB')


def with_ztransform_preprocess(hashfunc, hash_size=8):
    def function(path):
        image = alpharemover(Image.open(path))
        image = image.convert("L").resize((hash_size, hash_size), Image.ANTIALIAS)
        data = image.getdata()
        quantiles = np.arange(100)
        quantiles_values = np.percentile(data, quantiles)
        zdata = (np.interp(data, quantiles_values, quantiles) / 100 * 255).astype(np.uint8)
        image.putdata(zdata)
        return hashfunc(image)
    return function
  
dhash_z_transformed = with_ztransform_preprocess(imagehash.dhash, hash_size = 8)
# print(dhash_z_transformed("/Users/saim/github/jsf/images/jsf/flood/img44.jpg"))
# print(dhash_z_transformed("/Users/saim/github/jsf/images/jsf/flood/img49.jpg"))


def file_hash(filepath):
    return(dhash_z_transformed(filepath))

for index, filename in  enumerate(os.listdir('.')): 
    if os.path.isfile(filename):
        try:
            filehash = file_hash(filename)
        except UnidentifiedImageError as err:
            print(f"Ignoring {filename}: {err}")
            continue
        if filehash not in hash_keys: 
            hash_keys[filehash] = index
        else:
            duplicates.append((index,hash_keys[filehash]))

for index in duplicates:
    os.remove(file_list[index[0]])
