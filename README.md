# Rover 2.0 OS Developer's Guide
## Getting Started
### Setting up ROS
Rover 2.0 runs on the open source [Robotic Operating System](https://www.ros.org), specifically Lunar Loggerhead. To start developing with ROS, you'll need access to a Linux distro (preferably Ubuntu, as we run Ubuntu on the rover itself).

You have 3 options here:
1. Install Ubuntu's Xenial Distro (16.04.3) on a laptop or desktop
1. Use a Virtual Machine
    1. Install [VMWare Player](https://my.vmware.com/en/web/vmware/free#desktop_end_user_computing/vmware_workstation_player/14_0)
    1. You can download Rover's VM [here](https://www.dropbox.com/sh/jpjyvxjzwur0kr5/AACAhvjKlyJO1A8gTY04oAKDa?dl=0) - Note this is a read-only link (password for the default account is picusmartius)
    1. Or, if you want to build your own VM: [Ubuntu VM Distros](https://www.osboxes.org/ubuntu/) - Choose 16.04.4 Xenial, either VirtualBox for Mac or Vmware for windows
1. Install Windows Subsystem for Linux (Windows only)

Once you have a VM, or have installed and setup WSL:
#### **[ROS Lunar Install Page](http://wiki.ros.org/lunar/Installation)**

### Learning ROS

#### [ROS Tutorials](http://wiki.ros.org/ROS/Tutorials)

The best way to learn ROS is to jump into the extensive tutorials, linked above, on the organizations main wiki page. I'd recommend at least going through the beginner tutorials to get a basic understanding of how ROS works before looking into Rover 2.0's code. Your path after that largely depends on which part of the code you want to work on first.

## Getting the Rover Up and Running

### Setting up the TX2
You can follow [this](https://github.com/NVIDIA-Jetson/jetson-trashformers/wiki/Jetson%E2%84%A2-Flashing-and-Setup-Guide-for-a-Connect-Tech-Carrier-Board) guide to install or reinstall linux on the Nvidia TX2 board. Note: The Orbitty Carrier we're using requires additional steps before you flash the OS: if ignored, the TX2 won't have things like a working USB port.

Once the TX2 is up and running, edit the `/etc/apt/sources.list` file and replace `deb http://archive.ubuntu.com/ubuntu trusty universe main` with `deb [arch=amd64,i386] http://archive.ubuntu.com/ubuntu trusty universe main`.

### Downloading & Installing Rover Core OS

You can grab the source code from this repository using git. Make sure you clone it into your catkin workspace's `src` directory (if you setup everything according to the ROS tutorial, probably `~/catkin_ws/src`). Any development should be done on a branch distinct from `master` with working code being merged in via pull requests.

Next, you can run the dependency install script in the `scripts` directory.

Once that's done, you should be able to run `catkin_make_isolated --pkg rover_core_os` in the catkin workspace root directory to build the neccessary code and dependencies.

### Running
You can get Rover 2.0 up and running using `roslaunch`

First, run `roscore` in a separate terminal. Next run one of the following:
* `roslaunch rover_core_os display_model.launch`
* `roslaunch rover_core_os start_rover.launch`
* `roslaunch rover_core_os base_station.launch`
