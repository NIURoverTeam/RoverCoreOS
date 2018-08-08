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

# Function called when Twist messages are published
def navigation(data):
    logger.publish("Recieved!")

# Function to publish Twist messages to direct the Rover's movement
def create_twist(horizontal, vertical):
    twist = Twist()
    # Assign forward velocity based on up/down of thumbstick
    twist.linear.x = vertical
    # Rotate using tankdrive based on left/right of thumbstick
    twist.angular.z = horizontal
    twister.publish(twist)

# Triggers when a Joy message is published
# and decides what to do with the input
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
    # 0     Left Thumbstick : 1:Left, -1:Right
    # 1     Left Thumbstick : 1:Up, -1:Down
    # 2     Left Trigger : -1:Pressed, 1:Released
    # 3     Right Thumbstick : 1:Left, -1:Right
    # 4     Right Thumbstick : 1:Up, -1:Down
    # 5     Right Trigger : -1:Pressed, 1:Released
    # 6     D-PAD : 1:Left, -1:Right
    # 7     D-PAD : 1:Up, -1:Down

    if autonomous == False and (axes[0] != 0 or axes[1] != 0):
        create_twist(axes[0], axes[1])


if __name__ == '__main__':
    #Prep all the topics we want to publish/subscribe to
    logger = rospy.Publisher('logger', String, queue_size=10)
    twister = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    rospy.Subscriber("cmd_vel", Twist, navigation)
    rospy.Subscriber("joy", Joy, controller_input)

    # Start the driver node
    rospy.init_node('driver')

    # Start node logging
    log_string = 'Starting Rover 2.0....%s' % rospy.get_time()
    rospy.loginfo(log_string)
    logger.publish(log_string)

    rospy.spin()
