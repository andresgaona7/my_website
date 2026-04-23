---
title: Deep Learning-Driven Robotic Plastic Waste Sorter
date: 2026-01-27T17:00:12+08:00
author: Andrés Gaona
featuredImage: post_06/cover.webp
categories:
  - Robotics
  - Artificial intelligence
tags:
  - Deep learning
  - Computer vision
  - Robotics
  - YOLO
  - Waste Sorting
  - Delta Robot
draft: false
---

A high-speed robotic system for real-time plastic waste detection, classification, and picking using YOLOv4 and delta robot control.

<!--more-->

## 🧠 Overview & Challenges

This project involved the design, implementation, and **industrial deployment** of a **deep-learning-based robotic system** for **automatic plastic waste classification and sorting** in real recycling plant conditions.

The goal was to go beyond traditional mechanical sorters by combining real-time computer vision, high-speed motion control and precision robotic picking. This system was engineered to handle uncontrolled industrial environments, with real belts, moving targets, and strict throughput requirements.

**Key challenges included:**
- Detecting and classifying plastic waste *in real time* under variable lighting and clutter
- Precisely timing high-speed picks from a continuously moving conveyor
- Tracking objects reliably and robot control using *industrial communication protocols* (e.g. MODBUS, EtherCAT)
- Significantly reducing sorting errors compared to mechanical alternatives

![1](post_06/img1.mp4)

---

## 💡 Project Description

The system integrates:
- A **GPU-accelerated deep vision pipeline**, powered by YOLOv4 and CNN classifiers
- A **parallel motion planning pipeline** for a high-speed delta robot
- Robust *vision-to-motion synchronization* via industrial protocols

Vision and motion modules run in **parallel threads** to minimize latency and boost throughput.

The result was a fully functional automation solution that could:

✔ Detect plastic pieces  
✔ Classify multiple plastic types  
✔ Predict 3D location and timing  
✔ Command the robot to pick and sort continuously

---

## 🛠️ My Contributions

I took ownership of the vision and motion integration end-to-end:

### 🔍 Vision & Classification
- Trained and optimized a **YOLOv4 model** for plastic type recognition
- Built a **hardware-accelerated vision stack** with fast GPU inference
- Developed **object tracking & depth localization** for moving items

![2](post_06/img2.webp)

### 🤖 Motion & Control
- Designed a **fast-picking algorithm** tailored for *delta robot kinematics*
- Synchronized high-speed motion with conveyor tracking
- Implemented robust **MODBUS communication** between vision and motion modules

![2](post_06/img3.webp)

### 🧠 System Design
- Architected parallel vision + motion pipelines for minimal delay
- Ensured real-time responsiveness and scalability for industrial deployment

---

## 📊 Results & Impact

This system delivered **measurable performance gains** in an industrial setting:

| Metric | Result |
|--------|--------|
| **Detection & Classification Accuracy** | Up to **97%** |
| **Vision Inference Speed** | ~21 FPS |
| **Robot Pick Cycles** | ~60 cycles/min |
| **Correct Pick & Drop Rate** | **87%** |
| **Production Throughput** | ~70 picks/sec |
| **Field Vision Accuracy** | ~83% in production conditions |

![2](post_06/img4.mp4)

🎯 **Impact Highlights**
- Cut sorting errors significantly compared to mechanical systems
- Boosted throughput with *predictable, repeatable robotic picking*
- Reduced manual labor and operational costs
- Supported recycling plant efficiency and *circular economy goals*

---

## 📎 Links

