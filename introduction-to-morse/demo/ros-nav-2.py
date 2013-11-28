from morse.builder import *
from morse.builder.robots.pr2 import PR2

# PR2 Robot with joints
james = BasePR2()
james.add_interface('ros')
james.translate(x=2.5, y=3.2, z=0.0)

# Laser Scan
scan = Hokuyo()
scan.translate(x=0.275, z=0.252)
james.append(scan)
scan.properties(Visible_arc = False)
scan.properties(laser_range = 30.0)
scan.properties(resolution = 1.0)
scan.properties(scan_window = 180.0)
scan.create_laser_arc()
scan.add_interface('ros', topic='/base_scan')

# An odometry sensor to get odometry information
odometry = Odometry()
james.append(odometry)
odometry.add_interface('ros', topic="/odom")

# Keyboard control
keyboard = Keyboard()
james.append(keyboard)

# Set the environment
env = Environment('tum_kitchen/tum_kitchen')
env.aim_camera([1.0470, 0, 0.7854])
