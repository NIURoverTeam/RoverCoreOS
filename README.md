:warning::construction:Under Construction:construction::warning:

# Rover 2.0 Core OS

<img src="https://github.com/NIURoverTeam/RoverCoreOS/blob/master/assets/NIU%20Rover%20Logo%20V2.png" width="250" height="250"/>

## Developers Start Here

Looking to get started developing for the NIU Mars Rover Team? Check out the [wiki](https://github.com/NIURoverTeam/RoverCoreOS/wiki) to find our Getting Started Guide!

## Working With RoverCoreOS

Before you can run RoverCoreOS, you'll need to set up Robotic Operating System (ROS) Development Environment. Check [here](https://github.com/NIURoverTeam/RoverCoreOS/wiki/Setting-Up-a-Development-Environment) to learn how to set one up.

*TODO: Add a description of the Topography of the Repo and how to use each launch file/script*

### Downloading & Installing Rover Core OS

You can grab the source code from this repository using git. Make sure you clone it into your catkin workspace's `src` directory (if you setup everything according to the ROS tutorial, probably `~/catkin_ws/src`). Any development should be done on a branch distinct from `master` with working code being merged in via pull requests.

Next, you can run the dependency install script in the `scripts` directory. Before you run this you should install the [Realsense SDK 2.0](https://realsense.intel.com/sdk-2/#install)

Once that's done, you should be able to run `catkin_make_isolated --pkg rover_core_os` in the catkin workspace root directory to build the neccessary code and dependencies.

### Running
You can get Rover 2.0 up and running using `roslaunch`

First, run `roscore` in a separate terminal. Next run one of the following:
* `roslaunch rover_core_os display_model.launch`
* `roslaunch rover_core_os start_rover.launch`
* `roslaunch rover_core_os base_station.launch`

# Getting in Touch

Interested in joining, want to sponsor or contribute, or have questions? Here's some ways you can reach out or find out more about us:

* [NIURover@gmail.com](mailto:niurover@gmail.com)
* [Our site](https://niurover.wixsite.com/niurover)
* [Facebook](https://www.facebook.com/NIURover)
* [NIU CEET Student Organization Page](https://www.niu.edu/CEET/student-organizations/index.shtml)
