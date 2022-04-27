from subprocess import Popen
from sys import argv
import os

url = argv[1]
dir = os.path.realpath(argv[2])
os.chdir(dir)
print(f"Downloading images from {url} to {dir}")

Popen(f"wget -p -A .jpg,.jpeg,.png -H -nd {url}", shell=True).wait()
Popen(f"python3 ~/github/jsf/remove_similar_images.py .", shell=True).wait()
Popen(f"python3 ~/github/jsf/rename_images_serially.py .", shell=True).wait()