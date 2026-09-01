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
**Status:** Pending final pick — leaning Hiwonder xArm 2.0 vs. SO-101 /
SO-ARM100 (LeRobot). No 3D printer available, which rules out
print-it-yourself kits.
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
planned to leave room for Kalman tuning before the end of the semester.

## 2026-09-01 — Visual servo control loop: basic proportional
**Decision:** MVP control loop is a basic proportional visual servo, not
trajectory-optimized.
**Why:** The novelty of this project is the Jacobian estimator, not the
controller. No reason to spend time or risk on a solved sub-problem.

## 2026-09-01 — Stretch 2 timing
**Decision:** Attempt robustness demos (disturbance recovery,
near-singularity behavior, online target changes) if ahead of
schedule; otherwise hold until the end if time allows.

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
servo) in conversation, the demo video, and the
writeup. The ROS 2 package itself keeps its existing name,
`jacobian_online_estimator` — that stays as-is per ROS 2 naming
convention (lowercase with underscores) and because renaming it now would
break the repo/import paths already committed.
**Why:** A short, memorable name is more useful than the technical
package name in a conversation with a reviewer,
without needing to touch the actual codebase.
