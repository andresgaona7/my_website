---
title: Four-Legged Robot Platform
date: 2026-01-27T17:18:00+08:00
author: Andrés Gaona
featuredImage: post_09/cover.webp
categories:
  - Robotics
  - Artificial intelligence
tags:
  - Robotics
  - Model-based control
  - Control systems
draft: false
---

Design and development of a real-time, torque-controlled quadruped robot using EtherCAT, model-based control, and MPC.

<!--more-->

## 🚀 Overview & Challenges

Designing a quadruped robot that **walks with stability, precision, and robustness in real-time** is a multifaceted systems challenge. It demands coordination across hardware, low-latency communication, control theory, and middleware infrastructure — all without compromising safety or performance.

The primary challenge was to build a full-stack robotics solution capable of real-time torque control and dynamic locomotion, supporting multiple gait modes with responsive posture correction and stable long-duration operation.

---

## 🛠️ General Project Description

This project delivered a fully functional four-legged robotic platform that integrates:

- Real-time system infrastructure 
- Robust motor communication interfaces
- Model-based and optimization-based locomotion control
- Seamless integration between high-level and low-level modules

The outcome is a modular, extensible, real-time quadruped, capable of standing, walking, and trotting with high stability and performance — ready for advanced research and future autonomous behaviors.

---

## 📌 My Contributions

### 🔌 Motor Communication & Low-Level Infrastructure

- Architected and implemented motor communication interfaces supporting multiple protocols (EtherCAT, RS485, LCM)
- Built a robust OSC2-based actuator pipeline
- Tuned real-time Linux (PREEMPT-RT) for low latency & deterministic cycles

### 🧠 High-Level Locomotion Control

- Designed and deployed gait control algorithms supporting:
  - Standing
  - Walking
  - Trotting  
- Integrated model-based and whole-body control (MPC/WBC) strategies
- Ensured smooth hand-off between high-level planner and low-level motor control

<!-- ![1](post_09/img1.mp4) -->

### 🔄 System Integration & Validation

- Led cross-team integration across software and hardware layers
- Conducted comprehensive real-world testing & long-duration runs
- Iteratively optimized balance and posture correction modules

<!-- ![1](post_09/img2.mp4) -->

---

## 📊 Results & Impact

### Real-Time Performance & System Reliability

- Achieved sub-millisecond system latency
- Communication latency reliably < 10 ms, jitter < 1 ms
- Safety mechanisms validated with > 99% reliability
- Deterministic control loop performance > 50 Hz

![1](post_09/img3.webp)

### High-Quality Locomotion

- Parameter mismatch with real-time execution < 4%
- End-to-end locomotion latency < 10 ms
- Dynamic balance maintained with > 85% stability during motion

<!-- ![1](post_09/img4.mp4) -->

### Long-Duration Validation

- 6+ hours continuous operation without crashes
- 90% success rate across real-world scenarios
- 90% issue resolution through iterative optimization

### Strategic Impact

- Built a high-performance, torque-controlled quadruped platform
- Platform is real-time capable, modular, and extensible
- Provides a scalable foundation for:
  - Advanced locomotion research
  - Perception and autonomy integration
  - Adaptive, real-world robotic behavior development

<!-- ![1](post_09/img5.mp4) -->

---

## 📎 Links

