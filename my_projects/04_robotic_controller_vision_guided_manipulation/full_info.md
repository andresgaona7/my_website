---
title: "Robotic Controllers & Vision-Guided Manipulation"
date: 2019-01-01
summary: "Development of real-time robotic controllers integrating forward/inverse kinematics, EtherCAT motion control, and AI-based object detection for industrial manipulation."
tags: ["Robotics", "Motion Control", "Kinematics", "Computer Vision", "EtherCAT"]
---

## Overview

This project focuses on the **development of real-time robotic controllers** combining **multi-axis motion control**, **forward and inverse kinematics**, and **vision-based object detection** for industrial robotic systems.  
The work spans robot arms, Stewart platforms, and vision-guided picking systems, emphasizing **precision, compatibility, and real-time performance**.

---

## Technical Focus

### Robotic Motion Control
- Designed and implemented **real-time multi-axis controllers** for industrial robots.
- Integrated **EtherCAT-based communication** to ensure deterministic control loops.
- Supported multiple **control modes** (CSP / PP) across heterogeneous motor vendors.
- Developed compatibility tools enabling large-scale multi-vendor EtherCAT integration.

### Forward & Inverse Kinematics
- Implemented **forward and inverse kinematics (FK/IK)** for:
  - Industrial robot arms
  - Stewart platforms for drone testing
- Validated kinematic solvers through trajectory tracking and motion accuracy tests.
- Used FK/IK as the foundation for trajectory generation and closed-loop motion control.

### Vision & Object Detection
- Integrated **computer vision and AI-based object detection** into robotic workflows.
- Developed systems to:
  - Identify object type and position (e.g., microchips)
  - Feed perception results directly into motion planning and control loops
- Combined **vision and motion control in a single system architecture**, reducing latency and improving responsiveness  [oai_citation:0‡Final Presentation OpenCV Scara (1).pptx](sediment://file_00000000d128720994fe8f72e0f052d3)

---

## Key Contributions

- Implemented **real-time robotic controllers** with EtherCAT for industrial manipulation.
- Developed **robust FK/IK solvers** for robot arms and parallel mechanisms.
- Integrated **vision-based object detection** for autonomous picking and manipulation.
- Delivered a **unified motion + vision control architecture** for industrial robots.
- Improved system compatibility and scalability across hardware vendors.

---

## Applications

- Vision-guided robotic picking
- Precision industrial manipulation
- Drone testing using Stewart platforms
- AI-assisted robotic automation