#!/usr/bin/env python

# Command Line Usage:
#   To use i2c:         rosrun rover_core_os base_controller.py _is_i2c:=true _device:=0
#   To use Serial:      rosrun rover_core_os base_controller.py _is_i2c:=false _device:=/dev/ttyACM0
# Launch File Usage:
#   To use i2c:
#       <node pkg="rover_core_os" type="base_controller.py" name="base_controller">
#           <param name='is_i2c' value='true'/>
#           <param name='device' value='0'/>
#       </node>
#   To use Serial:
#       <node pkg="rover_core_os" type="base_controller.py" name="base_controller">
#           <param name='is_i2c' value='false'/>
#           <param name='device' value='/dev/ttyACM0'/>
#       </node>

import roslib
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import struct
from time import sleep
from smbus2 import SMBus
import serial

roslib.load_manifest("rover_core_os")

# Figure out whether we want i2c or serial
if rospy.get_param("/base_controller/is_i2c") == "true":
    # Configure our I2C Bus
    bus = SMBus(rospy.get_param("/base_controller/device"))
    dev_adr = 0x08
else:
    ser = serial.Serial(rospy.get_param("/base_controller/device"), 9600)


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

    # Write to I2C or Serial, depending
    if rospy.get_param("/base_controller/is_i2c") == "true":
        bus.write_i2c_block_data(
            dev_adr, 0, [leftDir, int(abs(leftPower)), rightDir, int(abs(rightPower))]
        )
    else:
        ser.write(
            struct.pack(
                ">BBBB", leftDir, int(abs(leftPower)), rightDir, int(abs(rightPower))
            )
        )


# Main execution starts here
if __name__ == "__main__":
    # Prep all the topics we want to publish/subscribe to
    logger = rospy.Publisher("logger", String, queue_size=10)

    rospy.Subscriber("joy", Joy, controller_input)

    # Start the driver node
    rospy.init_node("base_controller")

    # Start node logging
    log_string = "Starting base_controller....%s" % rospy.get_time()
    rospy.loginfo(log_string)
    logger.publish(log_string)

    rospy.spin()
