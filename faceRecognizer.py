import cv2
import numpy as np
import os
import getuid

u=int(getuid.var)


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#initiate id counter
id = 0

# names related to ids:
names = ['None', 'Abhishek', 'Aman', 'Tanwar', 'Z', 'W'] 

# Initialize and start realtime video capture
hcam = cv2.VideoCapture(0)
hcam.set(3, 640) # set video widht
hcam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*hcam.get(3)
minH = 0.1*hcam.get(4)

while True:

    ret, img =hcam.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 50 and u==id):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            import getdata
                
        else:
            id = "person not recognised"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
        
          
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
hcam.release()
cv2.destroyAllWindows()
