#!/usr/bin/env python
import roslib
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import rospy
import tf
roslib.load_manifest('rover_core_os')

# Global variables go here
autonomous = False

def navigation(data):
    logger.publish("Recieved!")

def controller_input(data):
    # Check if the back button has been pressed, and if it has, shutdown
    if data.buttons[6] == 1:
        logger.publish("Back Buttton Pressed, shutting down...")
        rospy.signal_shutdown("Back Button Pressed!")

    # Extract relevant data into useful local copies
    buttons = data.buttons # Array of int32
    # 0     A
    # 1     B
    # 2     X
    # 3     Y
    # 4     LB
    # 5     RB
    # 6     Back
    # 7     Start
    # 8     Middle Button
    # 9     Left Stick Click
    # 10    Right Stick Click
    axes = data.axes # Arrary of float32, each from -1.0 to 1.0
    # 0     Left/Right Axis stick left
    # 1     Up/Down Axis stick left
    # 2     Left/Right Axis stick right
    # 3     Up/Down Axis stick right
    # 4     RT
    # 5     LT
    # 6     cross key left/right
    # 7     cross key up/down

    if axes[2] > 0.00:
        logger.publish("Left Trigger")


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
