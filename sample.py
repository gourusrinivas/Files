import os

os.chdir('D:\Hello')
f = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

f.reverse()

for i in f[5:]:
    os.remove(os.path.join('D:\Hello', i))
    
print("RECENT FILES ARE")

for i in f[:5]:
    print(i)

import os
import zipfile

os.chdir('D:\Hello')

exzip = zipfile.ZipFile('recent.zip', 'w')
exzip.close()

import os
imort zipfile
os.chdir('D:\Hello')
os.getcwd()
myzipfile = zipfile.Zipfile('recent.zip')
myzipfile.namelist()
