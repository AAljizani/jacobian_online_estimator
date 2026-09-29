# jacobian_online_estimator (Project ObserVo)

This is a ROS 2 package that estimates a robot arm's Jacobian while the arm is running, without relying on an exact model of the arm. A fixed camera watches the end of the arm (eye-to-hand), and the package uses what it sees to keep updating the estimate. We are building it as our senior capstone project.

We call the project ObserVo (observe + servo) for short, like in the demo video and the writeup. The ROS 2 package keeps the longer name, jacobian_online_estimator.

## Core idea

The Jacobian tells you how the end of the arm moves when each joint moves a little. Normally you calculate it from the arm's link lengths and joint offsets, but on a cheap arm those don't always match the real thing because of things like servo deadband, backlash in the gears, and parts heating up. So instead of trusting the model, this package moves the joints, watches how the marker on the end of the arm moves through the camera, and keeps updating its guess of the Jacobian.

We are comparing two ways to do the updating:
- Broyden rank-1 update: a simple update that only changes the estimate in the direction the joints just moved.
- Kalman filter: also updates the estimate, but keeps track of how uncertain it is about each part of the Jacobian.

We don't know yet which one works better. That's what the project is trying to find out. In simulation, we use KDL to calculate the real Jacobian from the arm's URDF, and compare both estimators against it.

## Setup

We use an SO-101 follower arm, which has 5 joints plus a gripper and uses 12V STS3215 servos. The camera is an Arducam OV9281 global shutter USB camera. It sits level and straight ahead of the arm and tracks one ArUco marker that is on the arm. We track the marker's full pose (position and rotation), so the Jacobian we estimate is 6x5.

Software: Ubuntu 24.04, ROS 2 Jazzy, Gazebo Harmonic, OpenCV, KDL, and colcon.

## Status

We are in Phase 1 (simulation). Both estimators run in a MuJoCo sim, and the SO-101 model runs in Gazebo with ArUco detection working. The arm hasn't arrived yet. The ROS 2 node files below are still placeholders, and the sim code is outside this repo for now. See CHANGELOG.md for what we've done and DECISIONS.md for why.

## Package layout

```
jacobian_online_estimator/
├── joint_interface_node.py          # talks to the arm's servos, reads and sends joint angles
├── aruco_pose_node.py               # finds the ArUco marker in the camera image and gets its pose
├── jacobian_estimator_node.py       # runs Broyden or Kalman to update the Jacobian
├── estimators/
│   ├── broyden.py                   # the Broyden update
│   └── kalman.py                    # the Kalman filter update
└── visual_servo_controller_node.py  # turns the error into joint commands to move the arm
```

## Build (once ROS 2 Jazzy is set up)

Put this repo inside the src folder of your ROS 2 workspace. Then run these from the workspace folder itself, not from inside the repo:

```bash
colcon build --packages-select jacobian_online_estimator
source install/setup.bash
ros2 launch jacobian_online_estimator bringup.launch.py
```

## Project phases

1. Simulation: get both estimators working in MuJoCo and Gazebo and compare them to the KDL Jacobian
2. Hardware setup: get the arm and camera talking to ROS 2
3. Running it live: close the loop and control the real arm in 3D using the camera
4. Analysis and writing the report

## License

MIT, see LICENSE.
