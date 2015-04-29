import cv2
import sys

# help get rid of the "select timeout"
#/#bin/bash
#rmmod uvcvideo
#modprobe uvcvideo nodrop=1 timeout=5000 quirks=0x80
#http://www.raspberrypi.org/forums/viewtopic.php?t=35689&p=300710
#The Select Timeout is caused by not being able to get an image from the camera quickly enough

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frameL = video_capture.read()
    
    frame = cv2.resize(frameL,(320,240))

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
