# Decisions Log

Lightweight architecture/decision record for this capstone. Each entry:
what was decided, when, and why — so the reasoning survives even if the
person who made the call (you, months from now, under deadline pressure)
forgets it.

---

## 2026-09-01 — Eye-to-hand camera configuration
**Decision:** Camera is fixed on a stand watching the arm (not mounted on
the arm). Tracks a fiducial marker on the end-effector.
**Why:** Simplifies the camera-to-base transform to a single one-time
hand-eye calibration, at the cost of that calibration being a hard
dependency for everything downstream.

## 2026-09-01 — 3D requirement (not planar)
**Decision:** The end-effector must move and be tracked in full 3D space.
**Why:** An earlier planar version (dot on a wall) was rejected by the
capstone advisor as too limited. This is a hard constraint on camera
placement, marker choice, and workspace design.

## 2026-09-01 — ROS 2 Jazzy Jalisco + Gazebo Harmonic
**Decision:** Use ROS 2 Jazzy (LTS, supported to 2029) and Gazebo Harmonic,
not the newer Lyrical release.
**Why:** Ecosystem maturity matters more than newness for a deadline-bound
project.

## 2026-09-01 — Robot arm: buy, don't build
**Decision:** Purchase a pre-assembled arm (~$300-500 budget) rather than
building one.
**Status:** We picked the SO-101 on 2026-09-08 (see that entry below).
No 3D printer available, which rules out print-it-yourself kits.
**Why:** The arm is the substrate, not the contribution; buying protects
project time for the actual research (Jacobian estimation).

## 2026-09-01 — MVP scope requires both estimators
**Decision:** The MVP must run **both** Broyden and Kalman-based Jacobian
estimation live on real hardware, not Broyden-only.
**Why:** Revised from an earlier Broyden-only recommendation. Increases
MVP risk (Kalman tuning is the harder, more fragile piece) — mitigated by
front-loading hardware bring-up (Phase 2) earlier, since Kalman tuning
needs real hardware noise characteristics, not just simulation.
**Consequence:** Phase 2 timeline should be pulled earlier than originally
planned to leave room for Kalman tuning before the Dec 9 CMU deadline.

## 2026-09-01 — Visual servo control loop: basic proportional
**Decision:** MVP control loop is a basic proportional visual servo, not
trajectory-optimized.
**Why:** The novelty of this project is the Jacobian estimator, not the
controller. No reason to spend time or risk on a solved sub-problem.

## 2026-09-01 — Stretch 2 timing
**Decision:** Attempt robustness demos (disturbance recovery,
near-singularity behavior, online target changes) before Dec 9 if ahead of
schedule; otherwise hold for the Dec 9-18 window.

## 2026-09-01 — Explicitly out of scope
**Decision:** Multi-camera/stereo rigs, force/torque sensing, multi-arm
coordination, custom firmware/PCB work, mobile base integration, and
learned/neural-network Jacobian estimation are out of scope. The last item
may be mentioned as future work in the final report.
**Why:** Protects the timeline; none of these serve the core contribution.

## 2026-09-01 — Development environment: dual-boot Ubuntu on primary PC
**Decision:** Dual-boot Ubuntu 24.04 LTS on the primary (strong) desktop PC as
the main ROS 2 / Gazebo / hardware development machine. The M1 MacBook Air
is used for lightweight, portable work only (report writing, git, and
early Broyden/Kalman math prototyping in plain Python or PyBullet — no
ROS 2 needed for that).
**Why:** The project depends on continuous, low-latency USB access to two
pieces of hardware (camera, servo bus). Any virtualization layer (VM on
either machine, or WSL2 on Windows) adds a USB-passthrough risk layer on
top of hand-eye calibration and the sim-to-real gap, which are already
flagged as the hardest parts of this project. Apple Silicon has no
Boot Camp option, ruling out dual-boot on the Mac.

## 2026-09-01 — Project name: "Project ObserVo"
**Decision:** The project is referred to as **Project ObserVo** (observe +
servo) in conversation, the CMU application, demo video, and portfolio
writeup. The ROS 2 package itself keeps its existing name,
`jacobian_online_estimator` — that stays as-is per ROS 2 naming
convention (lowercase with underscores) and because renaming it now would
break the repo/import paths already committed.
**Why:** A short, memorable name is more useful than the technical
package name in an application essay or a conversation with a reviewer,
without needing to touch the actual codebase.

## 2026-09-08 - Using the SO-101 follower arm

Decision: We are using one SO-101 follower arm. We ordered it from PartaBot (order #2165). It came unassembled with the 12V STS3215 servos. On 2026-09-17 we asked PartaBot to switch the order to the full kit so we also get the leader arm, but we still need to check if they actually did that.

Why: The biggest reason is the URDF. In simulation we compare our estimators against the real Jacobian that KDL calculates from the URDF, so the URDF has to match the actual arm. The SO-101 has URDF and MJCF models made from its original CAD files, and there is already a ROS 2 Control package for it (so_arm_100_hardware). None of the other arms in our budget had both of those.

The servos also report back a lot of useful information: position, speed, load, voltage, temperature, and errors. That means we can get the real joint angles for the estimator and also log the servo temperature during trials.

The arm has five joints (shoulder_pan, shoulder_lift, elbow_flex, wrist_flex, wrist_roll) and a gripper. Some sellers call it a 6-DOF arm because they count the gripper, but the gripper doesn't move the arm around, so it's really a 5-DOF arm plus a gripper. We always call it 5-DOF in our docs.

Other arms we looked at and why we didn't pick them:
- Hiwonder xArm 1S and 2.0: they use their own protocol and there is no ROS 2 URDF we could trust.
- Hiwonder LeArm: one version uses PWM servos, which don't report position back.
- Hiwonder ArmPi FPV: its camera is mounted on the gripper, but our camera is fixed and watches the arm. It also needs its own Raspberry Pi.
- ROBOTIS Koch v1.1: you need a 3D printer to build it, and the motors cost about twice as much.
- Waveshare RoArm-M1: it has no wrist roll joint, and its board does its own inverse kinematics and smoothing, so we couldn't clearly see what we commanded versus what actually happened.
- Hiwonder's version of the SO-ARM101: they changed some of the parts to make them stronger, so the arm doesn't match the original CAD and the URDF would be off.

## 2026-09-08 - Going with the 12V servos

Decision: We are keeping the 12V STS3215 servos that came with the kit. This means we need a 12V power supply that can give at least 5A.

Why: The 12V servos have about 30 kg*cm of torque, compared to about 16.5 for the 7.4V ones. With more torque, each servo works less hard to do the same motion, so it should heat up less. Heat is a problem for our experiments (see the thermal entry below), so this helps. Also, the test data we found online about the STS3215 (backlash, deadband, heating) was measured on this same 12V version, so we can use those numbers directly. The voltage doesn't change the encoder, the protocol, or the kinematics, so the URDF and ROS 2 package still work.

The downside is that the default servo gains in the ROS 2 package were probably tuned for 7.4V servos, so we will need to retune them. The extra torque could also damage the plastic parts, so before we power the arm for the first time we need to lower the torque limit and the overload timeout in the servo settings. We also plan to run the arm slowly on purpose.

Still to do: On 2026-09-15 the spare servo we looked at was the 7.4V C001, which doesn't match this. We need to check the label on the servos we actually get before buying any spares.

## 2026-09-08 - Jacobian size and keeping the wrist roll joint

This entry was partly replaced by the 2026-09-24 entry, because we switched from position only (3x5) to full pose (6x5). We are keeping it here so the history makes sense. The part about keeping wrist_roll active still applies.

Decision: At first we only tracked the marker's 3D position, which made the Jacobian 3x5 (3 position values and 5 joints). To turn the error into joint commands we use damped least squares:

    q_dot = J^T (J J^T + lambda^2 I)^-1 s_dot

We also decided to keep the wrist_roll joint active and never lock it.

Why: Broyden's update only changes the Jacobian in the direction the joints actually moved. So if the arm never moves in some direction, that part of the estimate never gets updated and just gets older and older. It doesn't blow up, it just goes stale. The problem feeds itself too. The controller only moves the arm in directions the current estimate thinks are useful, so the directions the estimate got wrong never get moved in, and never get fixed.

The Kalman filter handles this differently because it keeps track of how uncertain it is about each part of the Jacobian. Directions that aren't moving show up as growing uncertainty instead of just staying stale. This difference between the two methods is the main thing we are comparing. If we locked wrist_roll, a lot of this behavior would go away, and so would the thing we are trying to study.

## 2026-09-08 - Only update the estimator when the joints actually moved

Decision: The estimator only updates when the measured joint change is at least 1.5 degrees. We use the joint angles the servos report back, not the angles we told them to go to. On 2026-09-28 we also changed it to add up the joint change since the last update instead of looking at one control step at a time.

Why: The STS3215 servos have a deadband of about 10 encoder counts, which works out to around 0.88 degrees. If the error between where the servo is and where it's told to go is smaller than that, the servo just doesn't move. On top of that there is some backlash in the gears, around 0.5 to 0.9 degrees, which shows up when a joint changes direction. Put together, small commands can pile up without the joint moving at all, and then the joint jumps once the error gets big enough. This is called stick-slip. It also means the joint moves at uneven times, so the Kalman filter can't assume the time between updates is always the same.

This matters for the estimator because Broyden and Kalman both learn from pairs of "how much the joints moved" and "how much the marker moved." If we used the commanded angle, we would be telling the estimator the joint moved when it really didn't, and the marker change would just be camera noise. Over time that pulls the Jacobian estimate in the wrong direction. It's also where the estimate can blow up, because the update divides by the size of the joint change squared, and dividing by a number close to zero gives huge values.

In the sim we found that looking at one step at a time almost never passed the 1.5 degree check when the arm moves slowly, so we switched to adding up the change since the last update.

Still to do: The deadband is a setting stored in the servo, so we need to read the real value off our servos once the arm arrives instead of assuming 10 counts. On Ubuntu we can use FT_SCServo_Debug_Qt for this. The 1.5 degree number might change after that, and we should log whatever value we end up using.

## 2026-09-08 - Adding a small back and forth motion (dither)

Decision: To keep the estimator learning, we add a slow, small back and forth motion on top of the joint commands. This is called dither. It has to be bigger than the deadband and backlash, so for now bigger than 1.5 degrees.

Why: If the dither is too small or too fast, the servo and the gear backlash basically swallow it. The joint doesn't really move, but we would still be commanding a change. That gives the estimator the same bad data we talked about in the gating entry, where it thinks the joint moved but the marker change is just noise.

Still to do: Once the arm arrives, move each joint back and forth with smaller and smaller steps until the marker stops responding. That number tells us both the dither size and the gating threshold.

## 2026-09-08 - Mixing up trial order because of servo heat

Decision: We will mix Broyden and Kalman trials together in a random order instead of running all of one and then all of the other. We will log the servo temperature the whole time, and the software will stop the experiment well before 70 C.

Why: Someone tested the STS3215 moving back and forth continuously, and it went from 48 C to 71 C in about 110 minutes. They didn't see the servo shut itself off when it got too hot, and the position error got worse as it heated up. Our experiments are a lot of small repeated motions, which is pretty much the same thing. If we ran all the Broyden trials first and all the Kalman trials after, the Kalman trials would happen on hotter servos. Then we wouldn't know if Kalman did worse because of the method or because of the heat, and there would be no way to fix that after the fact.

## 2026-09-08 - Where to put the ArUco marker

This entry was partly replaced by the 2026-09-22 entry, because we decided to put the marker directly on the arm instead of on a separate tab. The reasoning about the offset still matters.

Decision: The marker should not sit exactly on the wrist_roll axis. We planned to pick how far off the axis it sits by testing different distances in the sim.

Why: If the marker is right on the wrist_roll axis, rolling the wrist only spins the marker in place and doesn't move its position, so that joint's column in the Jacobian is basically zero. If the marker is too far off the axis, it tilts away from the camera when the wrist rolls, and ArUco pose gets worse at steep angles. The depth estimate gets bad first. So there is a middle range that works best.

Still to do: In the sim, try different offsets and plot how big the wrist_roll column is against how tilted the marker gets. Before trusting any estimator results, also log the size of each column of the KDL Jacobian across the workspace.

## 2026-09-08 - Checking the joint zero positions

Decision: Before we trust any comparison between the sim and the real arm, we need to check that the joint zero positions on the real arm match the URDF.

Why: There are two ways this could go wrong without us noticing. First, the SO-101 models support two different ways of setting zero. The newer way puts zero in the middle of each joint's range, and the older way puts zero with the arm stretched out flat. If ours doesn't match the URDF, KDL will calculate the Jacobian for the wrong arm pose. Second, if there is no calibration file, the hardware package falls back to a generic formula, (ticks - 2048) * 2pi / 4096, which gives the wrong joint range. Either problem would still let the sim check pass, just against the wrong answer, so we would never see an error.

Still to do: Command a known angle, measure the actual joint angle by hand, and compare it to /joint_states. Take a photo of each joint at zero while building the arm. Ask PartaBot which zero convention their build uses. Until this is done, Phase 1 isn't really finished.

## 2026-09-08 - Camera type and keeping everything rigid

Decision: We are using a global shutter black and white camera watching the arm from a fixed spot. The camera and the arm base will be clamped to the same rigid surface, and we will use our own diffuse lighting instead of just room lights.

We bought the camera on 2026-09-12. It's an Arducam B0332 (OV9281, USB). We also bought a SmallRig magic arm clamp, a CAMVATE cheese plate, and Velcro straps to mount it. We still haven't picked the baseplate.

Why: A normal rolling shutter camera captures the image one row at a time, so a moving marker looks slightly bent. That would mess up the pose, and the error would change with how fast the arm moves, which the estimator would think is part of the Jacobian. A global shutter captures the whole image at once, so this doesn't happen. The catch is that global shutter with a short exposure needs a lot of light, and if the marker corners are too dark, the pose gets noisier. That's why we need our own lighting.

The camera and arm have to stay locked together because the camera to arm transform is only correct while nothing moves. If the camera shifts even a little during a session, from a cable getting pulled or someone bumping the desk, it would look like Jacobian error that neither estimator actually caused.

## 2026-09-22 - Camera placement and marker mounting

Decision: The camera sits straight ahead of the arm and is level, with no tilt up or down. It's fixed to the same rigid surface as the arm. The ArUco marker goes directly on the arm, not on a bracket. ROS 2 runs on the desktop PC.

Why: With the camera straight ahead and level, the marker faces the camera pretty directly in the working pose. ArUco pose is most accurate when the marker faces the camera, so this gives us the best data.

## 2026-09-24 - Tracking the full marker pose (6x5 Jacobian)

Decision: We now track the full pose of the marker, which is 3 position values and 3 rotation values. With 5 joints, the Jacobian is now 6x5. This replaces the 3x5 position only setup from 2026-09-08. We are using one ArUco marker for now, and maybe more later. For frame notation we write the frame it's measured in as a superscript before the letter and the frame it describes as a subscript after, so {}^C T_M is the marker pose in the camera frame.

Why: The arm doesn't just move the marker around, it also rotates it. Only tracking position throws away the rotation information, and a lot of what wrist_roll does is rotation.

Still to decide: The 2026-09-08 entry talked about the null space, which is the set of joint motions that don't change what we're tracking. That made sense for 3x5, where there are more joints than things being tracked. But 6x5 has more tracked values than joints, so if the Jacobian is full rank there isn't a null space anymore. The problem is still there, it's just better described as directions that don't get moved much or are hard to see. The 2026-09-28 sim showed this with the rotation rows. We need to pick one way to describe this and use it everywhere in the report.
