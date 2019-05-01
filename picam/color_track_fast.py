import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)

# Color Paramaters in 8-bit HSV
# Blue
# H = 240
# S = 100
# V = 100
H = int(np.floor(240/2))
diff = 20
lowerBound=np.array([H-diff,100,10])
upperBound=np.array([H+diff,255,255])



def getCenter(img):
  M = cv2.moments(img)
  d = M['m00']
  if (d < 0.001):
    d = 1.0
  cx = int(M['m10']/d)
  cy = int(M['m01']/d)
  theOut = (cx, cy)
  return theOut




while(True):
   tick = time.time()
   # Capture frame-by-frame
   ret, frame = cap.read()

   # image to HSV from BGR - 0.016
   imgHSV= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

   # Get mask  - 0.009
   mask=cv2.inRange(imgHSV,lowerBound,upperBound)

   
   cv2.imshow("Mask (no filter)", mask)
   
   # erode/diolate
   kernel = np.ones((3,3), np.uint8)
   mask = cv2.erode(mask, kernel, iterations=1)
   mask = cv2.dilate(mask, kernel, iterations=1)

   # Get center  - 0.008
   center = getCenter(mask)

   iheight, iwidth, ichannel = frame.shape
   x = int(np.floor(iwidth)/2)
   y = int(np.floor(iheight)/2)
   #print imgHSV[y,x]
   #center = (x,y)

   # draw circle
   iheight, iwidth, ichannel = frame.shape
   dim = int(np.ceil(iheight/20))
   cv2.circle(frame,center,dim,(0,0,255),-1)


   cv2.imshow("Image", frame)
   cv2.imshow("Mask", mask)


   tock = time.time()
   print tock-tick
   cv2.waitKey(1)
       
