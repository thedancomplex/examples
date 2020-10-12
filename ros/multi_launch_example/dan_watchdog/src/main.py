#! /usr/bin/env python

print "dan_watchdog"
import rospy
from sensor_msgs.msg import JointState
from nav_msgs.msg import Odometry
from std_msgs.msg import String 
from geometry_msgs.msg import Twist
import numpy as np
import time as t


MAX_TIME = 2.0

# starting time
t0 = t.time()

def callback(msg): 
    global t0
    t0 = t.time()
    print msg.data

        


rospy.init_node('dan_move_robot')
sub = rospy.Subscriber('/key_press', String, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

while(True):
    t1 = t.time()
    dt = t1 - t0
    if(dt > MAX_TIME):
        tw = Twist()
        pub.publish(tw)
        #print "timeout"
    t.sleep(0.1)