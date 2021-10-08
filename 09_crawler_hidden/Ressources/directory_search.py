import os
import sys

walk_dir = sys.argv[1]
readmes = []
for root, subdirs, files in os.walk(walk_dir):
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    if "README" in files:
        with open(root + "/README", mode="r") as f:
            txt = f.read()
            if txt not in readmes:
                readmes.append(txt)
                print("{}/README :".format(root), txt)
