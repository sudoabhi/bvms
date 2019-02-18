import os

path='database'
arr=os.listdir(path)
print(arr)
print("Enter your aadhaar num:\n")
x=input()
for i in arr:
    if(x==i):
        os.chdir(path)
        f=open(i,'r')
        var=f.readline()
        print("Aadhaar verified.\nLook into the webcam for facial recognition")

os.chdir("..")
