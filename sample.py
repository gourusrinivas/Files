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
path = 'Hello'
with zipfile.ZipFile('final.zip', 'w') as zipF:
    for file in path:
        zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)
        


