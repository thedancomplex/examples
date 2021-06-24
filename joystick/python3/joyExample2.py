from __future__ import print_function
from time import sleep
from inputs import get_gamepad
import numpy as np

def joy2norm(v):
    v = v - 127
    v = v/127.0
    if (v > 1.0):  v = 1.0
    if (v < -1.0): v = -1.0
    return v

def joy2frame(v,j_type):
    if   (j_type == 'ABS_Y' ): v = -v
    elif (j_type == 'ABS_X' ): v = -v
    elif (j_type == 'ABS_RZ'): v = -v  
    elif (j_type == 'ABS_Z' ): v = -v

    return v

def joy2convert(v,t):
    v = joy2norm(v)
    v = joy2frame(v,t)
    return v

def joy2rad(x,y):
    ma = 0.25
    if   ( (x < ma) & (x > -ma) & (y < ma) & (y > -ma) ): return 0.0
    d = np.arctan2(y,x)
    return d

def checkHist(v):
    ma = 0.25
    x = v.linear.x
    y = v.angular.z
    if   ( (x < ma) & (x > -ma) & (y < ma) & (y > -ma) ): return True
    return False

def main(args=None):
    i = 0

    x = 0.0
    y = 0.0
    kx = 0.5
    kz = 0.5
    while True:
        events = get_gamepad()
        for event in events:
            #print(event.ev_type, event.code, event.state)
            #print(type(event.ev_type), type(event.code), type(event.state))
            v = joy2convert(event.state, event.code)
            if   (event.code == 'ABS_Y'): x = v
            elif (event.code == 'ABS_X'): y = v
            r = joy2rad(x,y)
            print(x,y,r)

if __name__ == '__main__':
    main()
