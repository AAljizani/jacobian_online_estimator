# Changelog

All notable changes to this project are logged here. This file is the
human-readable timeline of the project — see `DECISIONS.md` for the *why*
behind scope and design changes, and use `git log` / tags for the
commit-level detail.

Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

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
  demo video, and the writeup. ROS 2 package name unchanged
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
