# jacobian_online_estimator (Project ObserVo)

ROS 2 package for **online estimation of a robot arm's Jacobian** — without a
precise kinematic model — using a fixed (eye-to-hand) camera watching the
end-effector. Built as a senior capstone project.

*"ObserVo" (observe + servo) is the project's short name, used in the demo video, and portfolio writeup. The ROS 2 package itself
keeps the descriptive name `jacobian_online_estimator`.*

## Core idea

Instead of assuming exact link lengths / joint offsets, this package estimates
the joint-velocity-to-end-effector-velocity mapping (the Jacobian) online, by
moving the joints and watching the resulting end-effector motion through a
fixed camera, then updating the estimate continuously.

Two estimation strategies are implemented and compared:
- **Broyden rank-1 update** — lightweight baseline.
- **Kalman-filter-based estimation** — more robust to noise.

An analytical Jacobian (via KDL) is used as ground truth in simulation to
validate both.

## Setup

We use an SO-101 follower arm, which has 5 joints plus a gripper and uses 12V STS3215 servos. The camera is an Arducam OV9281 global shutter USB camera. It sits level and straight ahead of the arm and tracks one ArUco marker that is on the arm. We track the marker's full pose (position and rotation), so the Jacobian we estimate is 6x5.

Software: Ubuntu 24.04, ROS 2 Jazzy, Gazebo Harmonic, OpenCV, KDL, and colcon.

## Status

We are in Phase 1 (simulation). Both estimators run in a MuJoCo sim, and the SO-101 model runs in Gazebo with ArUco detection working. The arm hasn't arrived yet. The ROS 2 node files below are still stubs, and the sim code is outside this repo for now. See `CHANGELOG.md` for what we've done and `DECISIONS.md` for why.

## Package layout

```
jacobian_online_estimator/
├── joint_interface_node.py      # reads/writes joint angles (arm servo bridge)
├── aruco_pose_node.py           # camera calibration + ArUco marker pose
├── jacobian_estimator_node.py   # runs the selected estimator (Broyden/Kalman)
├── estimators/
│   ├── broyden.py               # Broyden rank-1 update
│   └── kalman.py                # Kalman-filter-based estimator
└── visual_servo_controller_node.py  # closes the loop: error -> joint command
```

## Build (once ROS 2 Jazzy is set up)

```bash
colcon build --packages-select jacobian_online_estimator
source install/setup.bash
ros2 launch jacobian_online_estimator bringup.launch.py
```

## Project phases

1. Simulation validation (MuJoCo / Gazebo Harmonic vs. KDL baseline)
2. Hardware bring-up (arm + camera talking to ROS 2)
3. Live deployment (closed-loop visual servoing on real hardware, 3D)
4. Analysis and writeup

## License

MIT — see `LICENSE`.
