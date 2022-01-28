import os

path='D:\Hello'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

recent = files[-1,-2,-3,-4,-5]

print(recent)
