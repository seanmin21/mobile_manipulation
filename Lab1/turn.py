import time
import numpy as np
import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

robot.stow()

robot.base.rotate_by(np.radians(180))
robot.push_command()
