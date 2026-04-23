---
title: Autonomous Mobile Robot (AMR) for Indoor Environments
date: 2026-01-27T17:08:08+08:00
author: Andrés Gaona
featuredImage: post_08/cover.webp
categories:
  - Mobile robotics
tags:
  - AMR
  - Mobile robotics
  - ROS
  - Teleoperation
  - Odometry
  - EtherCAT
draft: false
---

Design, construction, and control of an indoor autonomous mobile robot combining academic research and industrial ROS-based implementations.

<!--more-->

## 🚀 Overview & Challenges

This project covers the **end-to-end design, construction, and control of an Autonomous Mobile Robot (AMR)** for indoor environments. It bridges academic research rigor with real-world robotic system engineering, evolving from a Bachelor’s research project into a professionally structured, ROS-based robotic platform.

The main challenge was building a complete robotic system from scratch—mechanical, electronic, and software—while ensuring modularity, reliability, and scalability. Beyond making the robot move, the goal was to design a system that could grow, be reused, and serve as a long-term research and development testbed.

---

## 🧠 General Project Description

The robot was designed as a modular indoor AMR capable of:

- Teleoperation and reactive navigation
- Odometry-based localization
- Real-time motor control
- ROS-based distributed control

From mechanical design to high-level software, the platform follows clear architectural separation between sensing, actuation, control, and coordination. This allowed rapid experimentation while maintaining system stability and clarity—key for both research and industrial contexts.

![1](post_08/img1.mp4)

---

## 🛠️ My Contributions

I led and implemented the **core system components**, taking ownership of the robot from concept to validated prototype:

### 🔧 System & Mechanical Design
- Designed a differential-drive mobile base optimized for indoor use  
- Selected and sized stepper motors using torque, load, and slope analysis  
- Integrated power, actuation, and sensing into a compact, robust platform  

### 👁️ Sensors & State Estimation
- Designed the sensor layout (ultrasonic sensors, lidar, encoders, gyroscope, bumpers)  
- Implemented encoder- and gyro-based odometry using a differential-drive model  
- Improved robustness through sensor fusion for motion estimation

### 🧩 Control & Software Architecture
- Designed a distributed control architecture separating low-level actuation from high-level logic  
- Implemented teleoperation, reactive navigation, and odometry as ROS nodes  
- Ensured clean interfaces to enable testing, extension, and reuse  

### 🔄 ROS 1 → ROS 2 Migration
- Migrated the full control stack from ROS 1 to ROS 2
- Adapted to the new communication and execution model
- Achieved functional parity while improving system structure and maintainability  

![1](post_08/img4.mp4)

---

## 📊 Results & Impact

### ✅ Technical Results
- Stable teleoperation with no noticeable command latency  
- Reliable odometry with acceptable error for indoor navigation  
- Continuous operation over several hours without system instability  
- Successful navigation on flat floors and indoor slopes

![1](post_08/img3.mp4)

### 📈 Engineering Impact
- Delivered a **fully working AMR**, not just isolated algorithms  
- Created a scalable and reusable robotic platform
- Demonstrated the ability to design, integrate, and validate complex robotic systems end-to-end

---

## 📎 Links





