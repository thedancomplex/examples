    # ******************************************************************************
     # Argon Design Ltd. Project P8008 Slam
     # (c) Copyright 2014 Argon Design Ltd. All rights reserved.
     #
     # Module : oculusVideo2
     # Author : Joel Goddard
     # $Id: oculusVideo.py 6409 2014-08-18 14:26:50Z xxx $
     # ******************************************************************************
     
     #"""
     #Oculus Video: streams two camera feeds into the Oculus Rift after having distorted
     #      them to account for pincushion effect
     #May require some calibration through sliders provided
     #      (They will appear on the Oculus Rift)
     #For this to work the oculus rift should be the main screen
     #Please note this code is not dynamic and will need to be calibrated manually
     #Requires OpenCV 2.4.9, numpy 1.8.1 and ovrsdk
     #"""
     
     #import timeit
import cv2
from cv2 import cv
import socket
import numpy as np
import time
#from ovrsdk import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os
import threading
#import glut_teapot
import urllib
from copy import deepcopy

# mjpg server
import Image
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import StringIO


#ipcam
stream=urllib.urlopen('http://127.0.0.1:8080/.mjpg')
bytes=''

def getStream():
  global bytes
  global stream
  img2 = np.zeros((480,640,3), np.uint8)
  while(True):
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        img2 = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
#        cv2.imshow('i',img2)
        if cv2.waitKey(1) ==27:
            exit(0)
#        print('---------------')
#        print(type(img2))
#        print('---------------')
        break 
  return img2

def main():
  cv2.namedWindow('vid', 16 | cv2.CV_WINDOW_AUTOSIZE)
  cv2.setWindowProperty("vid", cv2.CV_WINDOW_AUTOSIZE, cv2.cv.CV_WINDOW_FULLSCREEN)
  while True:
     img = getStream()
     cv2.imshow('vid',img)
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if __name__ == "__main__":
  main()
