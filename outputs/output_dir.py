from glob import glob
import os

path = "../test_dir/*"

files = glob(path)

for file in files:
    os.mkdir('./' + file.split('\\',1)[1])