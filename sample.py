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
import os

os.chdir('D:\Hello')
exzip = zipfile.ZipFile('Recent.zip', 'w')
exzip.close()

import os

for fn in os.listdir("Recent.zip"):
    with open(os.path.join('D:\Hello', fn), 'r') as f:
        text = f.read()
        

