# Python program to rename all file
# names in your directory
import os
from sys import argv

dir = os.path.realpath(argv[1])
os.chdir(dir)
print(f"Renaming files in {dir}")

# Save file contents with name in order to avoid 
# overwriting of existing files
new_files = {}

for count, filename in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(filename)
    new_name = f'{1 + count:03d}{f_ext}'
    with open(filename, "rb") as f:
        new_files[new_name] = f.read()
    os.unlink(filename)

for new_name, f_data in new_files.items():
    with open(new_name, "wb+") as f:
        f.write(f_data)
