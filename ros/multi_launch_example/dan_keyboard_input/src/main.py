#! /usr/bin/env python

print "dan_keyboard"

import rospy
from std_msgs.msg import String 
import numpy as np

rospy.init_node('dan_keypress')
pub = rospy.Publisher('/key_press', String, queue_size=1)


while(True):
    val = raw_input("Input W/A/S/D: ")
    print(val)
    pub.publish(val)

