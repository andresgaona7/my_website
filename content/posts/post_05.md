---
title: Robotic Grasping Using Evolutionary Deep Neural Networks
date: 2026-01-27T16:54:19+08:00
author: Andrés Gaona
featuredImage: post_05/cover.webp
categories:
  - Robotics
  - Artificial Intelligence
tags:
  - Robotics
  - Deep Learning
  - Computer Vision
  - PSO
  - Grasping
draft: false
---

AI-based robotic grasping system combining deep neural networks and evolutionary optimization for robust object grasp estimation.

<!--more-->

## 🧩 Overview & Challenges

Robotic grasping in real-world environments is a **hard problem**: objects vary widely in shape, size, orientation, and material, while perception systems are noisy and incomplete.  

Most deep-learning grasping methods face a **critical trade-off**:
- **High accuracy → slow inference**
- **Fast inference → unstable or unreliable grasps**

The challenge was to **break this trade-off** and design a system that is:
- Fast enough for **real-time robotic manipulation**
- Accurate and **repeatable across unseen objects**
- Directly deployable on **real robotic hardware**

![1](post_05/img1.webp)

---

## 🧠 Project Description

I developed an **AI-driven robotic grasping estimation framework** that combines:

- **Deep Neural Networks (CNNs)** for grasp feasibility classification  
- **Evolutionary optimization (Particle Swarm Optimization)** for refining grasp candidates  
- **Stereo vision** to convert 2D grasp predictions into executable 3D robot commands  

The system first detects whether graspable features exist, then **evolves grasp hypotheses** toward the most reliable configuration—explicitly optimizing for **accuracy, repeatability, and physical feasibility**.

Unlike end-to-end black-box models, this approach introduces **structured reasoning and confidence control**, allowing the robot to **reject unsafe grasps instead of failing blindly**.

![1](post_05/img5.mp4)

---

## 🛠️ My Contributions

I was the **main technical driver** of this project and delivered the system end-to-end:

- ✅ Designed and implemented the **AI grasping estimation algorithm**
- ✅ Developed the **real-time inference pipeline** (≈2 seconds per grasp)
- ✅ Built and labeled a **custom grasping dataset**, expanded to **1.5M+ samples** via data augmentation
- ✅ Integrated **CNN inference + evolutionary optimization** into a single decision framework
- ✅ Implemented **confidence-aware grasp rejection** to reduce real-world failures
- ✅ Deployed and validated the system on a **6-DOF industrial robot with a two-finger gripper**
- ✅ Benchmarked performance against **state-of-the-art grasping methods**

![1](post_05/img2.webp)

This was not a simulation-only project—the system was **executed on real hardware**, lifting and manipulating real objects.

---

## 📊 Results & Impact

### 🚀 Performance Gains
- **~10× faster inference** than classical deep-learning grasp detectors  
- **2.0 s average grasp estimation time** with stable convergence  
- **91.5% CNN classification accuracy** on unseen grasp features  

![1](post_05/img3.webp)


### 🤖 Real Robot Success
- **94% grasp success rate** on physical robot experiments (with confidence filtering)
- Reliable grasping across **30+ real objects**, including tools, household items, and personal objects
- High **repeatability**: consistent grasp location across multiple trials

![1](post_05/img4.webp)

### 📈 Competitive Advantage
Compared to widely used grasping approaches:
- Similar accuracy  
- **Order-of-magnitude faster execution**
- Explicit handling of **non-graspable objects**, reducing hardware damage risk

### 🌍 Practical Impact
This project demonstrates how **AI can be engineered—not just trained**:
- Modular and robot-agnostic design
- Adaptable to different grippers and object sizes
- Suitable for **industrial, service, and research robotics**

---

## 📎 Links

