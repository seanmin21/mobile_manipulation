import time
import numpy as np
import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

robot.stow()

robot.arm.move_to(0.5)
robot.lift.move_to(1.1)
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('wrist_yaw', np.radians(30))
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('wrist_pitch', np.radians(30))
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('wrist_roll', np.radians(30))
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('stretch_gripper', 100)
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('stretch_gripper', -10)
robot.push_command()
robot.wait_command()

robot.head.move_by('head_pan', np.radians(50)) # Move head pan
robot.head.move_by('head_tilt', np.radians(50)) # Move head tilt
robot.push_command()
robot.wait_command()

robot.stow()

robot.base.translate_by(0.3) # Move robot base 0.3 meters forward
robot.push_command()
robot.wait_command()
robot.base.rotate_by(np.radians(180)) # Rotate base by 180 degrees
robot.push_command()
robot.wait_command()
robot.base.translate_by(0.3)
robot.push_command()
robot.wait_command()
