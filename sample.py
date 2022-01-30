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
from zipfile import ZipFile

zipObj = ZipFile('Sample.zip')
zinObj.write('D:\Hello')
zipObj.close()
         

