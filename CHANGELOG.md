# Changelog

This file is a list of what we got done and when. For why we did things a certain way, check DECISIONS.md.

## Oct 26
- Installed LeRobot 0.6.2 in a conda env with Python 3.12. It needs 3.12 or newer, which is the same Python that ROS 2 Jazzy uses.
- Set the servo IDs 1 to 6 one servo at a time, starting with the gripper and going down to shoulder_pan. Then chained them all together from the base up.
- Calibrated the follower arm and saved it as config/observo_follower.json. Each arm joint got about 190 to 215 degrees of range.
- Calibrating again moved the joint zeros by about 5 to 10 degrees each time, so we're keeping this one calibration for the trials.
- wrist_flex and gripper have homing offsets around 1800, which probably means those horns went on off from the servo center. wrist_roll came out at 2047, which is the most the servo can store, so we still need to check its zero.

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

## Sep 12
- Set up dual boot with Ubuntu 24.04 on the desktop. Press F11 at the MSI screen to pick Ubuntu.
- Installed ROS 2 Jazzy, Gazebo Harmonic, and ros2_control. Built the SO-101 packages from source (brukg/SO-100-arm and brukg/so_arm_100_hardware) and got gz.launch.py running.
- Bought the camera (Arducam B0332, OV9281) and the parts to mount it.

## Sep 8
- Ordered the SO-101 follower arm from PartaBot with 12V servos.
- Wrote the decisions for the arm, 12V servos, update gating, dither, trial order, marker placement, zero position check, and camera setup.

## Sep 1
- Set up the repo with the ROS 2 package structure and placeholder files for the joint interface, ArUco pose, Jacobian estimator (Broyden and Kalman), and the controller.
- Started DECISIONS.md and this changelog.
- Decided both Broyden and Kalman have to run on the real arm for the minimum version.
- Decided to dual boot Ubuntu 24.04 on the desktop for ROS 2 work and use the MacBook only for things that don't need ROS 2.
- Named the project Project ObserVo. The package name stays jacobian_online_estimator.
