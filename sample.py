import os

os.chdir('D:\Hello')
f = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

f.reverse()

for i in f[5:]:
    os.remove(os.path.join('D:\Hello', i))
    
print("RECENT FILES ARE")

for i in f[:5]:
    print(i)

import zipfile

os.chdir('D:\Hello1')
exzip = zipfile.ZipFile('Recent.zip', 'w')
exzip.close()


         
import os
from pathlib import Path
from zipfile import ZipFile


DOWNLOAD_DIR = Path("D:\Hello")
ZIPPED_FILE_DIR = Path("D:\Hello")


def get_list_of_all_folders(download_dir: Path):
    return [f for f in download_dir.iterdir() if download_dir.is_dir()]


def zip_files():
    folder_list = get_list_of_all_folders(DOWNLOAD_DIR)
    with ZipFile(ZIPPED_FILE_DIR / "Recent.zip", "w") as zip:
        # writing each file one by one
        for folder in folder_list:
            zip.write(folder)
           
zip_files()
