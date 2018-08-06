#!/usr/bin/env python
import roslib
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
roslib.load_manifest('rover_core_os')

import rospy
import tf

def navigation(data):
    rospy.loginfo("Recieved!")
    logger.publish("Recieved!")

def controller_input(data):
    rospy.loginfo("Input!")
    logger.publish("Input!")


if __name__ == '__main__':
    #Prep all the topics we want to publish/subscribe to
    logger = rospy.Publisher('logger', String, queue_size=10)

    rospy.Subscriber("cmd_vel", Twist, navigation)
    rospy.Subscriber("joy", Joy, controller_input)

    # Start the driver node
    rospy.init_node('driver')
    # Start node logging
    log_string = 'Starting Rover 2.0....%s' % rospy.get_time()
    rospy.loginfo(log_string)
    logger.publish(log_string)
    rospy.spin()
