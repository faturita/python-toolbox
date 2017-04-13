#coding: latin-1

#This works only with OpenCV 3
# source /usr/local/bin/virtualenvwrapper.sh
# workon cv

# Or you can use Conda: source activate cv (if you already have the env)


import time
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
#cap = cv2.VideoCapture('movie.mov')
#cap = cv2.VideoCapture('tcp://192.168.1.1:5555')

while(True):
   # Capture frame-by-frame
   ret, frame = cap.read()

   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   cv2.imwrite('01.png', gray)

   #Using AKAZE descriptors.
   detector = cv2.AKAZE_create()
   (kps, descs) = detector.detectAndCompute(gray, None)
   #print("keypoints: {}, descriptors: {}".format(len(kps), descs.shape))

   # draw the keypoints and show the output image
   cv2.drawKeypoints(frame, kps, frame, (0, 255, 0))

   cv2.imshow("ViewWindow", frame)

   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
