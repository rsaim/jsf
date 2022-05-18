# Python program to rename all file
# names in your directory
import os
from sys import argv
import imghdr
# >>> imghdr.what('/tmp/bass')
# 'gif'

dir = os.path.realpath(argv[1])
os.chdir(dir)
print(f"Renaming files in {dir}")

# Save file contents with name in order to avoid 
# overwriting of existing files
new_files = {}

count = 1
for oldname in os.listdir():
    if not imghdr.what(oldname):
        continue
    
    f_name, f_ext = os.path.splitext(oldname)
    new_name = f'{count:03d}{f_ext}'
    with open(oldname, "rb") as f:
        new_files[(oldname, new_name)] = f.read()
    os.unlink(oldname)
    count += 1

for (oldname, new_name), f_data in new_files.items():
    print(f"Writing {oldname} -> {new_name}")
    with open(new_name, "wb+") as f:
        f.write(f_data)
