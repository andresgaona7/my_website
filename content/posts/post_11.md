---
title: Real-Time Multi-Vendor EtherCAT Motion Control (MCCL)
date: 2026-01-27T17:24:41+08:00
author: Andrés Gaona
featuredImage: post_11/cover.png
categories:
  - Motion control library
tags:
  - MCCL
  - EtherCAT
  - Preset tool
  - Profile position
  - Control synchronous position
draft: false
---

A real-time, multi-vendor EtherCAT motion control platform was developed to abstract vendor differences while ensuring deterministic, synchronized multi-axis motion. 

<!--more-->

## Summary

A real-time, multi-vendor EtherCAT motion control solution was developed to remove vendor-specific complexity while preserving deterministic performance. The project centered on a scalable compatibility layer that unified 84 EtherCAT devices from different manufacturers under a single motion control API, with full support for standard CSP and PP motion modes. To accelerate deployment and reduce configuration errors, an automated preset tool was created to convert vendor ESI files into compliant ENI configurations, significantly reducing setup time. Running on an RTX-based real-time platform and implemented in C++, the system improved motion compatibility by ~20% and enabled reliable multi-axis synchronization. Beyond the technical outcomes, the solution supported customer adoption and contributed to a 100% increase in customer requests through close collaboration with international industrial partners.

## 🧠 Overview & Challenges

In industrial automation, achieving deterministic, synchronized motion control across multiple EtherCAT vendors remains a major bottleneck. Each vendor’s device behaves slightly differently — inconsistencies in parameter mapping, configuration files, and motion modes make real-time integration complex, error-prone, and unscalable.

The challenge of this project was to:

- Abstract away vendor differences without sacrificing performance.
- Build a scalable, real-time motion control stack that supports standard profiles like CoE, CSP, and PP.
- Enable seamless multi-axis synchronization with predictable timing.
- Reduce setup time and manual configuration errors across heterogeneous EtherCAT networks.

---

## 📦 Project Description

This project delivered a full digital EtherCAT motion control solution built on a deterministic RTX-based platform in C++.

The architecture consists of:

- MCCL API – High-level motion control interface used by applications.
- EcDriver – Low-level EtherCAT driver handling frame I/O, sync, and mode abstraction (CSP/PP).
- Preset Tool SDK – Automated device onboarding via ESI parsing and ENI generation.
- RTX Runtime – Hard real-time task execution to ensure predictable multi-axis behavior.

Together, these technologies enable *plug-and-scale EtherCAT motion control* with consistent performance — eliminating vendor fragmentation while supporting industry-standard motion profiles.

---

## ⭐ Key Contributions

### 1. **Multi-Vendor EtherCAT Compatibility Layer**

Designed and developed a unified abstraction that:

- Integrates 84 EtherCAT slave modules across multiple manufacturers.
- Normalizes discrepancies in CoE objects, sync behavior, and motion mode semantics.
- Provides a consistent API for motion applications.

### 2. **Preset Tool SDK**

Created a configuration automation toolkit that:

- Parses vendor ESI files and generates compliant ENI configurations.
- Removes manual configurations and drastically reduces setup time.
- Minimizes human errors during device integration.

### 3. **Full Digital Motion Control Solution**

Delivered end-to-end support for real-time EtherCAT motion:

- Implemented CSP and PP mode support with standardized state transitions.
- Built scalable driver interfaces for adding new servo drives effortlessly.
- Improved system compatibility by ~20% through software-first solutions.

### 4. **Cross-Functional Collaboration**

Worked closely with:

- PCB and semiconductor partners in Malaysia
- Customer integration teams

This collaboration increased adoption and drove a 100% growth in customer requests for motion solutions, turning technical capability into real-world demand.

---

## 📈 Results & Impact

| Outcome | Impact |
|---------|--------|
| 🔧 Multi-vendor support | Unified motion control across 84+ EtherCAT devices |
| ⏱ Deterministic performance | Predictable, real-time multi-axis synchronization |
| 🚀 Onboarding automation | Faster setup & fewer errors from ESI → ENI generation |
| 📊 Increased compatibility | ~20% broader support for standard motion profiles |
| 🤝 Customer growth | 100% boost in customer requests through improved integration |

