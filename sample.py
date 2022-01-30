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
p = 'D:\Hello'
os.chdir(p)

exzip = zipfile.ZipFile('recent.zip', 'w')
exzip.close()


os.chdir(p)
os.getcwd()
myzipfile = zipfile.ZipFile('recent.zip')
myzipfile.namelist()
