---
title: "Deep Learning–Based Robotic Waste Classification"
summary: "A high-speed robotic system for real-time plastic waste detection, classification, and picking using YOLOv4 and delta robot control."
date: 2022-01-01
tags: ["Deep Learning", "Computer Vision", "Robotics", "YOLO", "Waste Sorting", "Delta Robot"]
categories: ["Robotics", "AI"]
featured: true
---

## Overview

This project focuses on developing and deploying a **deep-learning-based robotic solution** for the **automatic classification and sorting of plastic waste**.  
The system combines **real-time computer vision**, **high-speed motion control**, and **robotic picking** to improve recycling quality and throughput.

The work was carried out as part of an industrial **Trash Sorting Robot** system between **2022–2023**, targeting real-world recycling plant conditions  [oai_citation:0‡Trash Classifier Plastic Waste.pptx](sediment://file_00000000916471faa2f33a6c5976a4cb).

---

## Goal

Develop and deploy a **robotic waste-sorting solution** capable of:
- Detecting plastic waste in real time
- Classifying different plastic types
- Picking objects accurately from a moving conveyor belt

---

## Challenges

- Real-time plastic waste detection under uncontrolled conditions  
- High-speed robotic picking with precise synchronization  
- Conveyor tracking using industrial communication protocols  
- Reducing sorting errors from traditional mechanical systems  

---

## Core Technologies

- **Deep Learning & Vision**
  - YOLOv4 object detection
  - CNN-based classification
  - GPU-accelerated inference
  - Multi-object detection & tracking

- **Motion & Control**
  - Delta robot kinematics
  - High-speed trajectory planning
  - Conveyor tracking
  - MODBUS communication protocol

- **Hardware**
  - Delta robot with vacuum end-effector
  - Industrial PC
  - 3D camera
  - Conveyor belt system
  - Servo drivers, air compressor, electric valves

---

## My Contributions

- Trained a **YOLOv4 model** to classify different types of plastic waste  
- Built a **hardware-accelerated vision system** using GPU inference  
- Implemented **object tracking and localization** for moving targets  
- Designed a **fast-picking algorithm** for delta robot motion  
- Implemented **communication between vision and motion modules** using MODBUS  

---

## System Architecture

### Vision Pipeline
1. Image acquisition  
2. Object detection & classification  
3. Filtering and depth calculation  
4. Object database update  

### Motion Pipeline
1. Object data acquisition  
2. Trajectory planning & feasibility check  
3. Command generation  
4. Real-time robot motion control  

Vision and motion run in **parallel threads** to minimize latency.

---

## Performance & Results

- **Detection & classification accuracy:** up to **97%**
- **Vision inference speed:** ~21 FPS
- **Picking speed:** ~60 robot cycles per minute
- **Correct pick & drop rate:** **87%**
- **Industrial deployment throughput:** ~70 picks/sec
- **YOLO-based vision accuracy:** ~83% detection accuracy in production

---

## Impact

This project demonstrates how **deep learning and robotics** can significantly improve **recycling efficiency**, reduce manual labor, and support **circular economy strategies** by enhancing quality control in plastic waste sorting.

---

## Keywords

YOLOv4 · Deep Learning · Robotic Vision · Delta Robot · Waste Sorting · Industrial Automation