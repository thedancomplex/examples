#!/usr/bin/env python
import argparse
import sys
import rospy
import baxter_interface as bi

def main():
  print("init node")
  rospy.init_node("baxter_joint_pos_set")
  left  = bi.Limb('left')
  right = bi.Limb('right')
  rate = rospy.Rate(1000)
  angles_right = {'right_s0': 0.0, 'right_s1': 0.0, 'right_w0': 0.0, 'right_w1': 0.0, 'right_w2': 0.0, 'right_e0': 0.0, 'right_e1': 1.57}
#  angles_right = {'right_s0': 0.0, 'right_s1': 0.0, 'right_w0': 0.0, 'right_w1': 0.0, 'right_w2': 0.0, 'right_e0': 0.0, 'right_e1': 1.57}
  angles_left = {'left_s0': 0.0, 'left_s1': 0.0, 'left_w0': 0.0, 'left_w1': 0.0, 'left_w2': 0.0, 'left_e0': 0.0, 'left_e1': 1.57}
#  angles_left = {'left_s0': 0.0, 'left_s1': 0.0, 'left_w0': 0.0, 'left_w1': 0.0, 'left_w2': 0.0, 'left_e0': 0.0, 'left_e1': 1.57}
  left.move_to_joint_positions(angles_left)
  right.move_to_joint_positions(angles_right)

0.010737865515197896, 1.1830826826566254, -0.15953400194008302, -1.1919030721869666, -0.9445486701404435, 1.3349467806572812, 1.571179821991635, 0.177941771394708, 1.3410827038088229, -0.36508742751672846, -0.95490304045867, 1.0549952868681933, 1.1911360817930239, 0.14879613642488512, -12.565987119160338



  print left.joint_angle('left_s0')
  print right.joint_angle('right_e1')

if __name__ == '__main__':
  main()
