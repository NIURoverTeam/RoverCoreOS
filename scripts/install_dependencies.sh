# Install dependency packages for building
sudo apt-get update
sudo apt-get install -y libusb-1.0-0-dev pkg-config libglfw3-dev qtcreator cmake-curses-gui build-essential libgtk-3-dev libssl-dev python-wstool python-rosdep ninja-build git-core libusb-1.0-0 libusb-1.0-0-dev

################ Cartographer Install ################
cd ~/catkin_ws
wstool init src

# Merge the cartographer_ros.rosinstall file and fetch code for dependencies.
wstool merge -t src https://raw.githubusercontent.com/googlecartographer/cartographer_ros/master/cartographer_ros.rosinstall
wstool update -t src

# Install proto3.
src/cartographer/scripts/install_proto3.sh

# Install deb dependencies.
# The command 'sudo rosdep init' will print an error if you have already
# executed it since installing ROS. This error can be ignored.
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y

# Build and install.
catkin_make_isolated --install --use-ninja --pkg cartographer_ros_msgs ceres-solver cartographer cartographer_ros
################ Realsense ROS Install ################

# Install librealsense into home directory
cd $HOME
git clone https://github.com/IntelRealSense/librealsense.git
cd librealsense
# Checkout version 2.10.1 of librealsense, last tested version
git checkout v2.10.1
# Install Qt libraries
sudo scripts/install_qt.sh
# Copy over the udev rules so that camera can be run from user space
sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && udevadm trigger
# Now compile librealsense and install
mkdir build && cd build
# Build examples, including graphical ones
cmake ../ -DBUILD_EXAMPLES=true
# The library will be installed in /usr/local/lib, header files in /usr/local/include
# The demos, tutorials and tests will located in /usr/local/bin.
make && sudo make install

cd ~/catkin_ws/src 

# Install Intel RealSense ROS Package
git clone https://github.com/intel-ros/realsense.git
cd realsense
git checkout 2.0.3
cd ../..
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
catkin_make_isolated --install --pkg realsense2_camera


################ Phidgets Spatial ROS Install ################
cd ~/catkin_ws/src
git clone -b lunar https://github.com/ros-drivers/phidgets_drivers.git
sudo apt-get install libusb-1.0-0 libusb-1.0-0-dev
cd ..
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
catkin_make_isolated --install --pkg libphidget21 phidgets_api phidgets_drivers phidgets_high_speed_encoder phidgets_ik phidgets_imu

cd ~/catkin_ws/src
git clone https://github.com/ccny-ros-pkg/imu_tools.git
cd ..
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
catkin_make_isolated --install --pkg imu_complementary_filter imu_filter_madgwick imu_tools

source install_isolated/setup.bash
