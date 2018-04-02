import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)

while(True):
   tick = time.time()
   # Capture frame-by-frame
   ret, frame = cap.read()
   # Our operations on the frame come here
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   # Display the resulting frame
   cv2.imshow('frame',gray)

   tock = time.time()
   print tock-tick
   cv2.waitKey(1)
       
