#!/usr/bin/env python
import roslib
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import rospy
import struct
import serial
from time import sleep
import tf
# from smbus2 import SMBus

roslib.load_manifest('rover_core_os')

# Configure our I2C Bus
# bus = SMBus(0)
# dev_adr = 0x41
ser = serial.Serial('/dev/ttyACM0', 9600)

def controller_input(data):
    # Check if the back button has been pressed, and if it has, shutdown
    if data.buttons[6] == 1:
        logger.publish("Back Buttton Pressed, shutting down...")
        rospy.signal_shutdown("Back Button Pressed!")

    # Calculate the power based on the vertical position of the left and right thumbsticks
    leftPower = round(data.axes[1] * 250)
    rightPower = round(data.axes[4] * 250)
    leftDir = 0x4C if leftPower >= 0 else 0x6C
    rightDir = 0x52 if rightPower >= 0 else 0x72

    # Write to I2C
    # bus.write_i2c_block_data(dev_adr,0,[leftDir,int(abs(leftPower)),rightDir,int(abs(rightPower))])
    ser.write(struct.pack('>BBBB', leftDir, int(abs(leftPower)),rightDir, int(abs(rightPower))))
if __name__ == '__main__':
    #Prep all the topics we want to publish/subscribe to
    logger = rospy.Publisher('logger', String, queue_size=10)

    rospy.Subscriber("joy", Joy, controller_input)

    # Start the driver node
    rospy.init_node('base_controller')

    # Start node logging
    log_string = 'Starting base_controller....%s' % rospy.get_time()
    rospy.loginfo(log_string)
    logger.publish(log_string)

rospy.spin()
