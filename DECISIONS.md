# Decisions

This file is where we write down the decisions we make for the project, when we made them, and why. We started it so that later on, when we're busy and don't remember why we did something a certain way, we can come back here and check. If a decision changes, we add a new entry and mark the old one as replaced instead of deleting it.

## 2026-09-01 - Fixed camera watching the arm (eye-to-hand)

Decision: The camera is on a fixed stand watching the arm, instead of being mounted on the arm. It tracks a marker on the end of the arm. This setup is called eye-to-hand.

Why: With the camera in one fixed spot, we only have to figure out where the camera is compared to the arm base once. This is called hand-eye calibration. The downside is that everything after that depends on that calibration being right, so if it's off, everything else will be off too.

## 2026-09-01 - The arm has to work in 3D

Decision: The end of the arm has to move and be tracked in full 3D, not just on a flat surface.

Why: Our first idea was to track a dot moving on a wall, which is only 2D. Our advisor said that was too limited for a capstone. Working in 3D affects a lot of other choices, like where the camera goes, what marker we use, and how we set up the workspace.

## 2026-09-01 - Using ROS 2 Jazzy and Gazebo Harmonic

Decision: We are using ROS 2 Jazzy and Gazebo Harmonic instead of the newer ROS 2 release (Lyrical).

Why: Jazzy is a long term support release, so it's supported until 2029, and most packages already work with it. Since we have deadlines, we care more about things working than about having the newest version.

## 2026-09-01 - Buying an arm instead of building one

Decision: We are buying an arm instead of building our own. Our budget was around $300 to $500. We don't have a 3D printer, so kits where you print your own parts were out. We haven't picked one yet. Right now it's between the Hiwonder xArm 2.0 and the SO-101 (SO-ARM100).

Why: The arm is just what we run our experiments on. The actual project is the Jacobian estimation, so we didn't want to spend our time building an arm when we could buy one and focus on the estimators.

## 2026-09-01 - Both estimators have to run on the real arm

Decision: For our minimum working version, both Broyden and Kalman have to run live on the real arm, not just Broyden.

Why: At first the plan was to only have Broyden running for the minimum version, but we changed it because comparing the two is the whole point of the project. This makes things riskier, because Kalman is harder to tune. Kalman needs to know how noisy the real sensors are, and we can only really find that out on the real hardware, not in the sim. Because of that, we need to start working with the hardware earlier than we first planned, so we have time to tune Kalman before the end of the semester.

## 2026-09-01 - Keeping the controller simple

Decision: The controller that moves the arm toward the goal is a basic proportional controller. We are not doing any trajectory planning or optimization.

Why: What's new in this project is the Jacobian estimation, not the controller. Controllers like this have already been figured out, so there's no reason to spend time on a fancy one or add more things that could go wrong.

## 2026-09-01 - Extra demos if we have time

Decision: If we are ahead of schedule, we will try some extra demos. These are recovering after the arm gets pushed, how it acts near singularities, and changing the target while it's moving. If we aren't ahead, we will only try them at the end if there's time left.

## 2026-09-01 - Things that are out of scope

Decision: We are not doing multiple cameras or stereo cameras, force or torque sensors, more than one arm, custom firmware or circuit boards, putting the arm on a mobile base, or using neural networks to learn the Jacobian. We might mention the neural network idea as future work in the final report.

Why: None of these help with what we're actually trying to show, and each one would take a lot of time we don't have.

## 2026-09-01 - Dual booting Ubuntu on the desktop

Decision: We are going to set up Ubuntu 24.04 as a dual boot on the desktop PC, and that's where all the ROS 2, Gazebo, and hardware work will happen. The M1 MacBook Air is only for things that don't need ROS 2, like writing the report, using git, and trying out the math in plain Python.

Why: The project needs a steady, fast USB connection to two things, the camera and the servo bus. If we ran Ubuntu in a virtual machine or used WSL2 on Windows, the USB has to be passed through an extra layer, and that could cause problems. Hand-eye calibration and getting the sim to match the real arm are already the hardest parts of the project, so we didn't want to add another thing that could break. We couldn't dual boot the Mac because Apple Silicon Macs don't support Boot Camp.

## 2026-09-01 - Calling it Project ObserVo

Decision: We call the project Project ObserVo (observe + servo) when we talk about it, in the demo video, and in the writeup. The ROS 2 package is still called jacobian_online_estimator.

Why: ObserVo is short and easier to remember than the package name, which helps when talking about the project or writing about it. We kept the package name the same because ROS 2 packages are supposed to be lowercase with underscores, and renaming it would break paths we already committed.
