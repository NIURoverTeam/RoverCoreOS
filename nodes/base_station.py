#!/usr/bin/env python
import roslib
roslib.load_manifest('rover_core_os')

import rospy

if __name__ == '__main__':
    rospy.init_node('base_station')
