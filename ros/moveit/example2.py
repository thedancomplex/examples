import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

import time as t


# init
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_example2', anonymous=True)


# initiate the robot
robot = moveit_commander.RobotCommander()


# initiate the scene
scene = moveit_commander.PlanningSceneInterface()


# init a group
group_name = "panda_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)



# display trajectory publisher
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)

# get a planning frame
planning_frame = move_group.get_planning_frame()
print "=== Planning frame: %s" % planning_frame

# end effector names
eef_link = move_group.get_end_effector_link()
print "=== End effector link: %s" % eef_link

# avaliable grups
group_names = robot.get_group_names()
print "=== Available Planning Groups:", robot.get_group_names()




# Get robots current state
print "=== Printing robot state"
print robot.get_current_state()


# Get current joint values
joint_goal = move_group.get_current_joint_values()
print "=== Current joint space values", joint_goal


# Set new joint space values
joint_goal[0] = 0
joint_goal[1] = -pi/4
joint_goal[2] = 0
joint_goal[3] = -pi/2
joint_goal[4] = 0
joint_goal[5] = pi/3
joint_goal[6] = 0



# Apply new joint space values
move_group.go(joint_goal, wait=True)

# Stop all motion
move_group.stop()


# Set new joint space values
joint_goal[0] = 0
joint_goal[1] = -1
joint_goal[2] = 0
joint_goal[3] = -1
joint_goal[4] = 0
joint_goal[5] = 1
joint_goal[6] = 0



# Apply new joint space values
move_group.go(joint_goal, wait=True)

# Stop all motion
move_group.stop()




# Move to target position
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.w = 1.0
pose_goal.position.x = 0.4
pose_goal.position.y = 0.1
pose_goal.position.z = 0.4

move_group.set_pose_target(pose_goal)

plan = move_group.go(wait=True)

move_group.stop()


# Clear end effector goal position targets
move_group.clear_pose_targets()



# cartesian paths and waypoints
waypoints = []
scale = 1.0
wpose = move_group.get_current_pose().pose
wpose.position.z -= scale * 0.1  # First move up (z)
wpose.position.y += scale * 0.2  # and sideways (y)
waypoints.append(copy.deepcopy(wpose))

wpose.position.x += scale * 0.1  # Second move forward/backwards in (x)
waypoints.append(copy.deepcopy(wpose))

wpose.position.y -= scale * 0.1  # Third move sideways (y)
waypoints.append(copy.deepcopy(wpose))

# make path at a resolution of 1cm (0.01) with no jump threshold

(plan, fraction) = move_group.compute_cartesian_path(
                                   waypoints,   # waypoints to follow
                                   0.01,        # eef_step
                                   0.0)         # jump_threshold


# display trajectory
display_trajectory = moveit_msgs.msg.DisplayTrajectory()
display_trajectory.trajectory_start = robot.get_current_state()
display_trajectory.trajectory.append(plan)

# Publish
display_trajectory_publisher.publish(display_trajectory);

print "=== displaying the trajectory"
t.sleep(5.0)

print "=== running the profile"
move_group.execute(plan, wait=True)




# add object to the plannign scene
box_pose = geometry_msgs.msg.PoseStamped()
box_pose.header.frame_id = "panda_leftfinger"
box_pose.pose.orientation.w = 1.0
box_pose.pose.position.z = 0.07 # slightly above the end effector
box_name = "box"
scene.add_box(box_name, box_pose, size=(0.1, 0.1, 0.1))



