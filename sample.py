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

os.chdir('D:\Hello1')
exzip = zipfile.ZipFile('Recent.zip', 'w')

for x in os.listdir('D:\Hello'):
    if x.endswith('.'):
    exzip.write(x, compress_type = zipfile.ZIP_DEFLATED)
exzip.close()


         

