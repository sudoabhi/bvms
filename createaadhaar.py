import os
path='database'
filename = input ("enter ur aadhaar num: \n");

with open (os.path.join(path,filename), "w") as f:
  f.write(input())

