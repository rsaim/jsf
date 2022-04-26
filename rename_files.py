# Python program to rename all file
# names in your directory
import os
from sys import argv

dir = argv[1]
os.chdir(dir)
print(f"Renaming files in {dir}")

for count, f in enumerate(os.listdir()):
	f_name, f_ext = os.path.splitext(f)
	f_name = f"img{count:02d}"
	new_name = f'{f_name}{f_ext}'
	os.rename(f, new_name)
