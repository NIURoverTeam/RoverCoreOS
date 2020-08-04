<img src="https://github.com/NIURoverTeam/RoverCoreOS/blob/master/assets/NIU%20Rover%20Logo%20V2.png" width="250" height="250"/>

# Arm-Code

### Introduction
A branch for me to experiment with python in order to build code to control a Rover arm with 3 DOF. The calculations will have to be tweaked for whatever measurements our completed arm will come out to.

The python code will make the calculations and the arduino IDE should control the motors

### Overview 
The completed application, should connect to the arm via serial and allowed the user to move the goal position of the end-effector by clicking and dragging, or by sending commands from another application running on the same computer

The design I'll be using is based on industrial pallet-packing robots, and at its core has three degrees of freedom, or ‘axes’ on which it can move. Think left to right, in and out and up and down; it basically means that the arm can move in three different ways. The GIFs below show the different types of movement: the entire arm can swivel on its base, the “main arm” translates the elbow in and out from the centre, and the “actuator” drives the forearm, which in turn translates the end-effector up and down. A 3-DOF arm like this has the handy property of having a unique solution for each possible position of its end-effector.

![actuator](https://user-images.githubusercontent.com/44382721/89333518-b036bf00-d65a-11ea-8554-92a171176571.gif)
![main](https://user-images.githubusercontent.com/44382721/89333522-b0cf5580-d65a-11ea-98f3-8f970d6ea0a3.gif)
![swing](https://user-images.githubusercontent.com/44382721/89333525-b0cf5580-d65a-11ea-9992-026ee032de70.gif)



### Tech Stack

The tech stack I used included:

* **Python**

TODO

Getting Started
---
### Pre-requisites and Local Development

TODO

Authors
---
Kofi Adu-Gyan

Acknowledgements
---
https://robohub.org/robotics-maths-python-a-fledgling-computer-scientists-guide-to-inverse-kinematics/

Alistair Wick for the GIF images
