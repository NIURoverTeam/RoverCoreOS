#!/usr/bin/env python
import roslib
from std_msgs.msg import String
roslib.load_manifest('rover_core_os')

import rospy
import tf

if __name__ == '__main__':
    logger = rospy.Publisher('logger', String, queue_size=10)
    rospy.init_node('driver')
    log_string = 'Starting Rover 2.0....%s' % rospy.get_time()
    rospy.loginfo(log_string)
    logger.publish(log_string)
    rospy.spin()
