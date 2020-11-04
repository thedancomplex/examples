#!/usr/bin/env python3
# license removed for brevity
import rospy
from gazebo_msgs.srv import ApplyJointEffort
from gazebo_msgs.srv import GetJointProperties
from std_msgs.msg import Header


def setRot(pub, val):
    buff = ApplyJointEffort()
    buff.effort = val

    start_time = rospy.Time(0,0)
    end_time = rospy.Time(0.01,0)

    buff.joint_name = "dd_robot::left_wheel_hinge"
    pub(buff.joint_name,  buff.effort, start_time, end_time)
    buff.joint_name = "dd_robot::right_wheel_hinge"
    pub(buff.joint_name, -buff.effort, start_time, end_time)


def getPos(pub):
    buff = GetJointProperties()
    buff.joint_name = 'dd_robot::left_wheel_hinge'

    val = pub(buff.joint_name)
    leftw = val.rate[0]
    buff.joint_name = 'dd_robot::right_wheel_hinge'
    val = pub(buff.joint_name)
    rightw = val.rate[0]
    v = (leftw, rightw)
    return v


def talker():
#    pub = rospy.Publisher('/gazebo/apply_joint_effort', ApplyJointEffort, queue_size=10)
    rospy.init_node('dd_ctrl', anonymous=True)
    pub    = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)
    pubget = rospy.ServiceProxy('/gazebo/get_joint_properties',GetJointProperties)
    rate = rospy.Rate(10) # 10hz
    i = 0
    val = 1.0
    while not rospy.is_shutdown():
        if i > 30:
            if val > 0:
                i = 0
            else:
                i = -30
            val = -val
        i = i + 1
        setRot(pub, val)
        v = getPos(pubget)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
