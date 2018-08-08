#!/usr/bin/env python
import roslib
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import rospy
import rosnode
roslib.load_manifest('rover_core_os')

def controller_listener(data):
    # Check if the back button has been pressed, and if it has, shutdown
    if data.buttons[6] == 1:
        logger.publish("Back Buttton Pressed, shutting down...")
        rosnode.kill_nodes(['joystick_controller'])
        rospy.signal_shutdown("Back Button Pressed!")

    logger.publish("Activity!")

if __name__ == '__main__':
    # Prep all the topics we want to publish/subscribe to
    logger = rospy.Publisher('logger', String, queue_size=10)

    rospy.Subscriber("joy", Joy, controller_listener)

    # Start the base_station node
    rospy.init_node('base_station')

    # Start node logging
    log_string = 'Starting Rover Base Station.....%s' % rospy.get_time()
    rospy.loginfo(log_string)
    logger.publish(log_string)

    rospy.spin()
