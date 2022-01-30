import os

os.chdir('D:\Hello')
f = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

f.reverse()

for i in f[5:]:
    os.remove(os.path.join('D:\Hello', i))
    
print("RECENT FILES ARE")

for i in f[:5]:
    print(i)

import patoolib
import zipfile

patoolib.create_zip("recent.zip", ('Hello'))

