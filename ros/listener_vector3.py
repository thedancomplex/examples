#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3

def callback(data):
    rospy.loginfo("x = " + str(data.x) + " y = " + str(data.y) + " z = " + str(data.z))
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('euler_listener', anonymous=True)

    rospy.Subscriber("euler_ref", Vector3, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
