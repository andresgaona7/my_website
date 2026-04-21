---
title: Robotic Controllers & Vision-Guided Manipulation
date: 2026-01-27T16:49:02+08:00
author: Andrés Gaona
featuredImage: post_04/cover.png
categories:
  - Motion control
  - Robotics control
  - Kinematics
tags:
  - Robotics
  - Motion control
  - Kinematics
  - Computer vision
  - EtherCAT
draft: false
---

Development of real-time robotic controllers integrating forward/inverse kinematics, EtherCAT motion control, and AI-based object detection for industrial manipulation.

<!--more-->

## 🧠 Overview & Challenges

This project focused on architecting **real-time robotic control systems** that combine motion precision, advanced kinematics, and vision-based perception for industrial automation. It tackled three core challenges:

- 🔄 **Deterministic real-time control** across multi-axis robotic systems
- 📐 **Accurate kinematic modeling** for robots with diverse geometries
- 👁️‍🗨️ **Vision-guided manipulation** in dynamic production environments

The goal was to create a **scalable, high-performance framework** capable of integrating heterogeneous hardware, complex motion planning, and perception in a single unified system — and deliver real, measurable impact in industrial robotics workflows.

---

## 🛠️ Project Overview

Modern industrial systems demand robots that are **precise, responsive, and adaptable**. This project delivered:

### 🔧 Real-Time Multi-Axis Motion Control
- Designed **deterministic multi-axis controllers** able to operate in strict real-time with EtherCAT communication.
- Supported multiple control paradigms — **CSP (Cyclic Synchronous Position)** and **PP (Profile Position)** — across motors from different manufacturers.
- Built tools for **large-scale integration** of multi-vendor EtherCAT networks, enhancing system compatibility.

### 📐 Forward & Inverse Kinematics Engines
- Built high-fidelity **FK/IK solvers** for:
  - Standard industrial manipulators
  <!-- - Parallel mechanisms such as **Stewart platforms** used for dynamic testbeds (e.g., drone motion testing). -->
- Validated solver accuracy through trajectory tracking and closed-loop control experiments.

### 👁️ Vision & Object Detection
- Integrated **AI-based vision pipelines** directly into the motion planning loop.
- Enabled robots to **identify object types and positions** (e.g., microchips) and act autonomously from perception to actuation.
- Merged perception data seamlessly into motion control, drastically reducing latency and increasing reactivity.

![1](post_04/img1.png)

---

## 💡 My Contributions

I built and delivered the core elements of the system:

- ⚙️ **High-performance real-time robotic controllers** with EtherCAT determinism.
- 📊 **Robust kinematic solvers** for both serial and parallel mechanisms.
- 🤖 **Vision-integrated automation**, bridging perception and motion in a unified architecture.
- 🛠️ **Multi-vendor hardware compatibility**, enabling scalable industrial deployment.
- 📈 **Architectural innovation** that reduced system latency and improved responsiveness.

---

## 🎯 Results & Impact

This work achieved measurable improvements in both capability and performance:

### 🚀 Performance & Precision
- **Deterministic control loops** that met real-time constraints in demanding industrial scenarios.
- High-accuracy motion tracking backed by validated FK/IK solvers.

### 🤝 System Integration & Scalability
- A **scalable control framework** that supports heterogeneous motors and communication networks.
- Reduced complexity in industrial setups through unified control + perception architecture.

### 🤖 Real-World Automation Gains
- Enabled **vision-guided robotic picking**, reducing manual intervention.
<!-- - Supported complex tasks such as **precision manipulation** and **drone testing on Stewart platforms**. -->
- Demonstrated AI-assisted automation ready for industrial adoption.

![1](post_04/img2.png)

---

## 📎 Links