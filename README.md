# Rover 2.0 Core OS

<img src="https://github.com/NIURoverTeam/RoverCoreOS/blob/master/assets/NIU%20Rover%20Logo%20V2.png" width="250" height="250"/>

## Developers Start Here

Looking to get started developing for the NIU Mars Rover Team? Check out the [wiki](https://github.com/NIURoverTeam/RoverCoreOS/wiki) to find our Getting Started Guide!

## Working With RoverCoreOS

Before you can run RoverCoreOS, you'll need to set up Robotic Operating System (ROS) Development Environment. Check [here](https://github.com/NIURoverTeam/RoverCoreOS/wiki/Setting-Up-a-Development-Environment) to learn how to set one up.

### Structure and Topography

* `assets`: images and other auxiliary files
* `config`: configuration files for packages used by the Rover, including the Navigation Stack
* `launch`: launch files to run various aspects of the Rovers functionality, in part or in whole. For usage instructions, see the "Running" section below
* `nodes`: individual Python or C++ files that encapsulate important aspects of the Rovers code
* `rviz`: configuration files for displaying UI tools using Rviz
* `urdf`: model files for visualizing the Rover

### Downloading & Installing Rover Core OS

You can grab the source code from this repository using git: `git clone https://github.com/NIURoverTeam/RoverCoreOS`. Make sure you clone it into your catkin workspace's `src` directory (if you setup everything according to the ROS tutorial, probably `~/catkin_ws/src`). Any development should be done on a branch distinct from `master` with working code being merged in via pull requests.

#### Install Dependencies

1. `sudo apt-get install ros-melodic-navigation`
1. Run `cd ~/catkin_ws && rosdep install --from-paths src --ignore-src -r -y`
1. Install the [Realsense SDK 2.0](https://realsense.intel.com/sdk-2/#install)
1. Install the [Realsense ROS Wrapper](https://github.com/IntelRealSense/realsense-ros#step-3-install-intel-realsense-ros-from-sources). 
  1. Note: use `catkin_make install --pkg realsense2_description realsense2_camera` instead of `catkin_make install`

### Running
You can get Rover 2.0 up and running using `roslaunch`.

First, run `roscore` in a separate terminal. Next run one of the following:
* `roslaunch rover_core_os display_rover.launch`: displays the URDF model of the Rover in Rviz
* `roslaunch rover_core_os start_rover.launch`: launch file to run on the Rover itself
* `roslaunch rover_core_os control_center.launch`: starts the base station to remotely control the Rover
* `roslaunch rover_core_os mapping.launch`: launch file wrapping the mapping functionality of the Rover, meant to be called in either the Rover or Control Center launch files, but can be called separately for troubleshooting purposes.

# Getting in Touch

Interested in joining, want to sponsor or contribute, or have questions? Here's some ways you can reach out or find out more about us:

* [NIURover@gmail.com](mailto:niurover@gmail.com)
* [Our site](https://niurover.wixsite.com/niurover)
* [Facebook](https://www.facebook.com/NIURover)
* [NIU CEET Student Organization Page](https://www.niu.edu/CEET/student-organizations/index.shtml)
