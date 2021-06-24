#from writer import UDP_Writer
from joystick import Joystick
import time

#writer = UDP_Writer("127.0.0.1")
joystick = Joystick(0)

m = [0,0,0]
while True:
    # get each axis strength
    s0, s1, s2, s3, brake = joystick.get_sticks()
    print(s0)
    print(s3)

    
    # convert to thrust inputs
    # vertical
    m[0] = s0
    
    
    # left
    m[1] = s3
    m[2] = brake
    msg = ""
    msg = msg + str(m[0]) +","
    msg = msg + (str(m[1]))+","
    msg = msg + (str(m[2]))
 #   writer.send(msg)
    time.sleep(0.01)
