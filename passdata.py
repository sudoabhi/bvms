print("Face verified.\n")
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
        passw=lines[7]

print("Place your thumb on sensor/Enter the password to proceed to the voting screen.\n")
os.chdir("..")
while(1):
    ps=input()
    if(ps==passw):
        import voteapp
        break
    else:
        print("Password Mismatch.\n Re-enter ur password.")
    

