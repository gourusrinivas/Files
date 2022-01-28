import os

path='D:\Hello'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

recent = files[-5:]

print(recent)

import os

path='D:\Hello'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

old = files[0]

print(os.remove(old))


import os
from pathlib import Path
from zipfile import ZipFile


DOWNLOAD_DIR = Path("D:\Hello")
ZIPPED_FILE_DIR = Path("D:\Hello")


def get_list_of_all_folders(download_dir: Path):
    return [f for f in download_dir.iterdir() if download_dir.is_dir()]


def zip_files():
    folder_list = get_list_of_all_folders(DOWNLOAD_DIR)
    with ZipFile(ZIPPED_FILE_DIR / "Other.zip", "w") as zip:
        # writing each file one by one
        for folder in folder_list:
            zip.write(folder)
           
zip_files()
