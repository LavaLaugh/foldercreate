import glob
import os
import shutil

path = glob.glob("*.cbz")
path.sort()

for file in path:
    folder = file.replace(" ch1.cbz", "")
    os.makedirs(folder)
    dest = folder + "/" + file
    shutil.copy(file, dest)