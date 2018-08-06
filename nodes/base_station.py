#!/usr/bin/env python
import roslib
from sensor_msgs.msg import Joy
roslib.load_manifest('rover_core_os')

import rospy

def controller_listener(data):
    rospy.loginfo(data.header)
    rospy.loginfo(data.axes)
    rospy.loginfo(data.buttons)

if __name__ == '__main__':
    # Start the base_station node
    rospy.init_node('base_station')
    # Start node logging
    logger = rospy.Publisher('logger', String, queue_size=10)
    log_string = 'Starting Rover Base Station.....%s' % rospy.get_time()
    rospy.loginfo(log_string)
    logger.publish(log_string)
    # Listen for joystick input and wait
    rospy.Subscriber("joy", Joy, controller_listener)
    rospy.spin()
