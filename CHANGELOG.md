# Changelog

This file is a list of what we got done and when. For why we did things a certain way, check DECISIONS.md.

## Sep 1
- Set up the repo with the ROS 2 package structure and placeholder files for the joint interface, ArUco pose, Jacobian estimator (Broyden and Kalman), and the controller.
- Started DECISIONS.md and this changelog.
- Decided both Broyden and Kalman have to run on the real arm for the minimum version.
- Decided to dual boot Ubuntu 24.04 on the desktop for ROS 2 work and use the MacBook only for things that don't need ROS 2.
- Named the project Project ObserVo. The package name stays jacobian_online_estimator.
