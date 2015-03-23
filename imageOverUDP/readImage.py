import numpy as np
import cv2
import time
from cv2 import cv
import socket


if __name__ == "__main__":
## ---------- UDP Start ---------------
      UDP_IP = "127.0.0.1"
      UDP_PORT = 5005
#      MESSAGE = "Hello, World!"
      sock = socket.socket(socket.AF_INET, # Internet
                           socket.SOCK_DGRAM) # UDP
      sock.bind((UDP_IP, UDP_PORT))
## ---------- UDP End -----------------



      while(True):

        img_str, addr = sock.recvfrom(10000000) # buffer size is 1024 bytes 
      # CV2
#        print type(img_str)
        nparr = np.fromstring(img_str, np.uint8)
        frame = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)

        cv2.imshow('frame',frame)
##        cv2.imshow('mask',mask)
#    cv2.imshow('res',res)





        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
	   ipCam.close()
           break
