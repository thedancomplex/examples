# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

#For OpenCV
import cv2
import numpy as np
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
 
# allow the camera to warmup
time.sleep(0.1)

# Color Paramaters in 8-bit HSV
lowerBound=np.array([160,50,50])
upperBound=np.array([179,255,255])



def getCenter(img):
  M = cv2.moments(img)
  cx = int(M['m10']/M['m00'])
  cy = int(M['m01']/M['m00'])
  theOut = (cx, cy)
  return theOut

def getCenterSlow(img):
  height, width = img.shape[:2]
  xt = 0.0
  yt = 0.0
  i = 0
  for y in range(height):
    for x in range(width):
      if(img[y,x] > 0):
        xt = xt + x
        yt = yt + y
        i = i+1

  if( i > 0):
    xt = xt / i
    yt = yt / i
  theOut = (int(xt), int(yt))
  return theOut


while True:
  tick = time.time() 
  # grab an image from the camera
  rawCapture = PiRGBArray(camera)
  camera.capture(rawCapture, format="bgr")
  image = rawCapture.array

  # resize
  ## img=cv2.resize(image,(160,120))
  img = image

  # image to HSV from BGR
  imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

  # Get mask
  mask=cv2.inRange(imgHSV,lowerBound,upperBound)

  # Get center
  center = getCenter(mask)

  # draw circle
  cv2.circle(img,center,50,(0,0,255),-1)

  print center

  cv2.imshow("Image", img)
  #cv2.imshow("Mask", mask)
  
  tock = time.time()
  print "Time to complete = " + str(tock - tick) + " sec"

  cv2.waitKey(10)
  #time.sleep(2.0)
# display the image on screen and wait for a keypress
#cv2.imshow("Image", image)
#cv2.waitKey(0)
