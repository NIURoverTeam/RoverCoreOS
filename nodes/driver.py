#!/usr/bin/env python
import roslib
from std_msgs.msg import String
from geometry_msgs.msg import Twist
roslib.load_manifest('rover_core_os')

import rospy
import tf

def drive(data):
    rospy.loginfo("Recieved!")

if __name__ == '__main__':
    # Start the driver node
    rospy.init_node('driver')
    # Start node logging
    logger = rospy.Publisher('logger', String, queue_size=10)
    log_string = 'Starting Rover 2.0....%s' % rospy.get_time()
    rospy.loginfo(log_string)
    logger.publish(log_string)
    # Subscribe to the Nav stack's output and wait
    rospy.Subscriber("cmd_vel", Twist, drive)
    rospy.spin()
