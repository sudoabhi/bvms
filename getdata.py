print("\n\nHello! Welcome to BVM voting portal....\n")
import os
from getuid import var
g=int(var)

path='database'

arr=os.listdir(path)

os.chdir(path)
for i in arr:
    if(arr[g-1]==i):
        f=open(i,'r')
        lines=f.readlines()
        fname=lines[1]
        lname=lines[2]
        sex=lines[3]
        age=lines[4]
        address=lines[5]
        consti=lines[6]

print("First Name: " + fname)
print("Last Name: "+lname)
print("Gender: "+sex)
print("Age: "+age)
print("Permanent Address: "+address)
print("Constituency: "+consti)

os.chdir("..")
    
import passdata
