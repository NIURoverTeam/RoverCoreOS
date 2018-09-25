# Rover 2.0 OS Developer's Guide
## Getting Started
### Setting up ROS
Rover 2.0 runs on the open source [Robotic Operating System](https://www.ros.org), specifically Lunar Loggerhead. To start developing with ROS, you'll need access to a Linux distro (preferably Ubuntu, as we run Ubuntu on the rover itself).

You have 2 options here:
1. Install Ubuntu's Xenial Distro (16.04.3) on a laptop or desktop
2. Use a Virtual Machine
3. Install Windows Subsystem for Linux (Windows only)

If you choose to use a virtual machine, you can try running NIU Rover's prebuilt VM with ROS already installed, or you can create your own. The prebuilt is intended for VMWare Player 12+ running on a windows machine.

* [Rover's VM](https://www.dropbox.com/sh/jpjyvxjzwur0kr5/AACAhvjKlyJO1A8gTY04oAKDa?dl=0) - Note this is a read-only link (password for the default account is picusmartius)
* [VMWare Player](https://my.vmware.com/en/web/vmware/free#desktop_end_user_computing/vmware_workstation_player/14_0)
* [Ubuntu VM Distros](https://www.osboxes.org/ubuntu/) - Choose 16.04.4 Xenial, either VirtualBox for Mac or Vmware for windows
* [ROS Lunar Install Page](http://wiki.ros.org/lunar/Installation)

### Learning ROS
The best way to learn ROS is to jump into the [extensive tutorials](http://wiki.ros.org/ROS/Tutorials) on the organizations main wiki page. I'd recommend at least going through the beginner tutorials to get a basic understanding of how ROS works before looking into Rover 2.0's code. Your path after that largely depends on which part of the code you want to work on first.

## Getting the Rover Up and Running

### Setting up the TX2
You can follow [this](https://github.com/NVIDIA-Jetson/jetson-trashformers/wiki/Jetson%E2%84%A2-Flashing-and-Setup-Guide-for-a-Connect-Tech-Carrier-Board) guide to install or reinstall linux on the Nvidia TX2 board. Note: The Orbitty Carrier we're using requires additional steps before you flash the OS: if ignored, the TX2 won't have things like a working USB port.

### Setup the RealSense Camera
With a freshly imaged TX2, you'll need to install drivers for Intel's RealSense camera. I'd start by trying to run [this](https://github.com/syedharoonalam/installLibrealsenseTX2) install script, but there's no guarantees it'll work. If it doesn't, you might have to search around for updated RealSense D345 install instructions, as these seem to break often for the TX2.

### Downloading & Installing Rover Core OS

You can grab the source code from this repository using git. Make sure you clone it into your catkin workspace's `src` directory (if you setup everything according to the ROS tutorial, probably `~/catkin_ws/src`). Any development should be done on a branch distinct from `master` with working code being merged in via pull requests. 

Next, you can run the dependency install script in the `scripts` directory.

Once that's done, you should be able to run `catkin_make` in the catkin workspace root directory to build the neccessary code and dependencies.

You'll probably also have to install [Google Cartographer](https://google-cartographer-ros.readthedocs.io/en/latest/index.html) and [Intel's Real Sense package](http://wiki.ros.org/RealSense)

### Running
You can get Rover 2.0 up and running using `roslaunch`

First, run `roscore` in a separate terminal. Next run one of the following:
* `roslaunch rover_core_os display_model.launch`
* `roslaunch rover_core_os start_rover.launch`
* `roslaunch rover_core_os base_station.launch`
