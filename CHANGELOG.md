# Changelog

All notable changes to this project are logged here. This file is the
human-readable timeline of the project — see `DECISIONS.md` for the *why*
behind scope and design changes, and use `git log` / tags for the
commit-level detail.

Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## Sep 28
- Got both estimators running in a MuJoCo sim. Even with no noise added, the parts of the Jacobian for joints that weren't moving stayed out of date. Kalman had lower overall error, but Broyden was better at predicting along the direction the arm was actually moving.
- Changed the update check so it adds up joint movement since the last update, because checking one step at a time almost never passed 1.5 degrees.
- Got the SO-101 model running in Gazebo. We had to use full file:// paths for the meshes, set damping to 0.6 and friction to 0.052 to match the STS3215, use P = 17.8 and D = 0, and add a fixed world_to_base joint. The arm just holding still in the working pose is normal, it only moves when commanded.
- Got ArUco detection working. OpenCV 4.6 needed minMarkerDistanceRate set to 0.02 or it dropped the marker. About 1 in 10 frames the marker rotation flips because of pose ambiguity at 0.8 m.
- Ran the full loop in the sim. With the perfect Jacobian the arm got within 8.7 mm and 6.5 degrees at 0.8 m, but both estimators got stuck far from the goal because the rotation part was hard to see. Moving the camera to 0.5 m and using 10 degree exploration moves brought the starting Jacobian error down from 128% to 62%.
- The sim code is in ~/observo_sim, not in this repo yet.

## Sep 24
- Switched to tracking the full marker pose, so the Jacobian is 6x5 now instead of 3x5.
- Wrote up the math notes. One thing we found is that Broyden is the same as the Kalman update if you set P = I and R = 0.

## Sep 22
- Decided the camera goes straight ahead of the arm and level, and the marker goes directly on the arm.
- Finished the SRS and the Sprint 0 presentation.

## Sep 17
- Asked PartaBot to switch the order to the full kit so we also get the leader arm.

## Sep 12
- Set up dual boot with Ubuntu 24.04 on the desktop. Press F11 at the MSI screen to pick Ubuntu.
- Installed ROS 2 Jazzy, Gazebo Harmonic, and ros2_control. Built the SO-101 packages from source (brukg/SO-100-arm and brukg/so_arm_100_hardware) and got gz.launch.py running.
- Bought the camera (Arducam B0332, OV9281) and the parts to mount it.

## Sep 8
- Ordered the SO-101 follower arm from PartaBot with 12V servos.
- Wrote the decisions for the arm, 12V servos, update gating, dither, trial order, marker placement, zero position check, and camera setup.

## [Unreleased]

### Added
- Initial repository scaffolding: ROS 2 ament_python package structure,
  node stubs for joint interface, ArUco pose, Jacobian estimator
  (Broyden + Kalman), and visual servo controller.
- `DECISIONS.md` to track scope and design decisions over time.
- `CHANGELOG.md` (this file) to track progress over time.

### Scope
- MVP finalized to require **both** Broyden and Kalman estimators running
  live on hardware (not Broyden-only). See `DECISIONS.md` entry 2026-09-01.

### Environment
- Development environment decided: dual-boot Ubuntu 24.04 on the primary
  PC for ROS 2/Gazebo/hardware work; M1 MacBook Air for portable, non-ROS
  work only. See `DECISIONS.md`.

### Naming
- Project is now referred to as **Project ObserVo** in conversation, the
  CMU application, and portfolio materials. ROS 2 package name unchanged
  (`jacobian_online_estimator`). See `DECISIONS.md`.

<!--
Template for future entries:

## [phase1-sim-validated] - YYYY-MM-DD
### Added
- ...
### Changed
- ...
### Fixed
- ...
-->
