# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
 
# allow the camera to warmup
time.sleep(0.1)

while True: 
  # grab an image from the camera
  rawCapture = PiRGBArray(camera)
  camera.capture(rawCapture, format="bgr")
  image = rawCapture.array
  print len(image)
  cv2.imshow("Image", image)
  cv2.waitKey(10)
  #time.sleep(2.0)
# display the image on screen and wait for a keypress
#cv2.imshow("Image", image)
#cv2.waitKey(0)
