---
title: "Autonomous Mobile Robot (AMR) for Indoor Environments"
summary: "Design, construction, and control of an indoor autonomous mobile robot combining academic research and industrial ROS-based implementations."
tags: ["AMR", "Mobile Robotics", "ROS1", "ROS2", "Teleoperation", "Odometry", "EtherCAT"]
date: 2020-01-01
---

## Overview

This project presents the **design, construction, and control of an autonomous mobile robot (AMR) for indoor environments**, combining **academic research work** with **industrial-oriented robotic system development**.

The platform was initially developed as part of a **Bachelor research project**, focusing on **teleoperation, reactive navigation, and odometry**, and was later extended professionally with **real-time motor control, modular ROS architectures, and ROS 1 to ROS 2 migration**  [oai_citation:0‡Bachelor Degree Research.pdf](sediment://file_000000007c3472098e67bf1a92f9f3b1).

## Goals

- Design and build an indoor autonomous mobile robot  
- Develop a **modular mechanical, sensory, and control architecture**  
- Enable **teleoperation and reactive navigation**  
- Implement **odometry-based localization**  
- Build a scalable **ROS-based control stack**

## Responsibilities

- Mechanical system design and integration  
- Sensor selection and placement  
- Control architecture design  
- Odometry modeling and implementation  
- Teleoperation and navigation logic  
- ROS system integration and validation  

---

## System Architecture

The robot follows a **modular architecture**, allowing individual subsystems to be reused, replaced, or extended for different applications and research objectives  [oai_citation:1‡Bachelor Degree Research.pdf](sediment://file_000000007c3472098e67bf1a92f9f3b1).

### Mechanical System

- Differential-drive configuration  
- Two driven wheels with follower wheels for stability  
- Stepper motors sized through torque and slope analysis  
- Battery-powered embedded system  
- Compact footprint suitable for indoor operation  

### Sensory System

- Ultrasonic sensor ring for obstacle detection  
- Limit switches for safety bumpers  
- Wheel encoders for motion estimation  
- Gyroscope for orientation feedback  

This sensor fusion improves robustness in navigation and odometry estimation  [oai_citation:2‡Bachelor Degree Research.pdf](sediment://file_000000007c3472098e67bf1a92f9f3b1).

### Control System

- Distributed embedded control using microcontrollers  
- Separation of sensing, actuation, and signal generation  
- High-level coordination and processing implemented in **ROS**

---

## Navigation & Control

### Teleoperation

- Joystick-based control integrated in ROS  
- Real-time velocity and direction commands  
- Safety constraints enforced through navigation logic  

### Reactive Navigation

- Obstacle avoidance based on ultrasonic sensor states  
- Direction selection logic with priority and fallback behaviors  
- Continuous environment monitoring during motion  

### Odometry

- Differential-drive kinematic model  
- Encoder-based velocity estimation  
- Gyroscope-assisted orientation tracking  
- Continuous pose estimation in ROS  

Experimental validation showed odometry errors within acceptable ranges for indoor mobile robots  [oai_citation:3‡Bachelor Degree Research.pdf](sediment://file_000000007c3472098e67bf1a92f9f3b1).

---

## ROS-Based Implementation

### ROS 1

- Complete control stack implemented in ROS 1  
- Motor communication and testing  
- ROS nodes for odometry, teleoperation, and visualization  

### ROS 2

- Control stack migrated to ROS 2  
- Updated communication and execution model  
- Functional parity with ROS 1 implementation  

---

## Experimental Results

- Stable teleoperation without noticeable command latency  
- Continuous operation over several hours  
- Successful navigation on indoor slopes  
- Validated odometry and reactive navigation performance  

---

## Research Impact & Future Work

This platform serves as a **research and development testbed** for:

- Navigation and localization algorithms  
- SLAM and sensor fusion  
- Vision-based odometry  
- Probabilistic localization methods (EKF, Monte Carlo)  

 [oai_citation:4‡Bachelor Degree Research.pdf](sediment://file_000000007c3472098e67bf1a92f9f3b1)

---

## Demo

📹 Video demonstration:  
https://drive.google.com/file/d/1B4eOF7qcoUCnGY6H_zpIKhngEzBLI2MR/view?usp=sharing