#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Vector3

def talker():
    pub = rospy.Publisher('euler_ref', Vector3, queue_size=10)
    rospy.init_node('camera', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        euler_ref_msg = Vector3()
        euler_ref_msg.x = 1
        euler_ref_msg.y = 2
        euler_ref_msg.z = 3
        rospy.loginfo(euler_ref_msg)
        pub.publish(euler_ref_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
