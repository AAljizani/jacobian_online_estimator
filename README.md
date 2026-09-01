# jacobian_online_estimator (Project ObserVo)

ROS 2 package for **online estimation of a robot arm's Jacobian** — without a
precise kinematic model — using a fixed (eye-to-hand) camera watching the
end-effector. Built as a senior capstone project.

*"ObserVo" (observe + servo) is the project's short name, used in the demo video and the
writeup. The ROS 2 package itself
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

## Status

Early scaffolding stage — see `CHANGELOG.md` for what's landed and
`DECISIONS.md` for why the project looks the way it does. Package interfaces
below are stubs until Phase 1 (simulation validation) is underway.

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

1. Simulation validation (PyBullet / Gazebo Harmonic vs. KDL baseline)
2. Hardware bring-up (arm + camera talking to ROS 2)
3. Live deployment (closed-loop visual servoing on real hardware, 3D)
4. Analysis and writeup

## License

MIT — see `LICENSE`.
