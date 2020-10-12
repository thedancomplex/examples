#! /usr/bin/env python

print "dan_move_robot"

#! /usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from nav_msgs.msg import Odometry
from std_msgs.msg import String 
from geometry_msgs.msg import Twist
import numpy as np

## Global Frame Velocities 
## Initial conditions
x0 = 0.0 # x (m)
y0 = 0.0 # y (m)
t0 = 0.0 # theta (rad)


tt0 = None
def callback(msg): 
    print msg.data
    d = msg.data
    tw = Twist()
    if (d == "w"):
        tw.linear.x = 0.5 
    elif (d == "s"):
        tw.linear.x = -0.5
    elif (d == "d"):
        tw.angular.z = -0.5
    elif (d == "a"):
        tw.angular.z = 0.5
    else:
        pass
    pub.publish(tw)

rospy.init_node('dan_move_robot')
sub = rospy.Subscriber('/key_press', String, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)


rospy.spin()