import hello_helpers.hello_misc as hm
import numpy as np

node = hm.HelloNode.quick_create('my_test_node')

node.stow_the_robot()
node.move_to_pose({'joint_lift': 1.1, 'joint_arm' : 0.5}, blocking=True)

node.move_to_pose({'joint_wrist_yaw': np.radians(30)}, blocking=True)
node.move_to_pose({'joint_wrist_pitch': np.radians(15)}, blocking=True)
node.move_to_pose({'joint_wrist_roll': np.radians(70)}, blocking=True)

node.move_to_pose({'joint_gripper_finger_left': np.radians(50)}, blocking=True)
node.move_to_pose({'joint_gripper_finger_left': np.radians(0)}, blocking=True)

node.move_to_pose({'joint_head_pan': np.radians(60)}, blocking=True)
node.move_to_pose({'joint_head_tilt': np.radians(-30)}, blocking=True)

node.stow_the_robot()

node.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)
node.move_to_pose({'rotate_mobile_base':np.radians(180)}, blocking=True)
node.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)









