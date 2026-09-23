---
title: Reliable Pick-and-Place with ROS 2 and MoveIt 2
date: 2026-09-23T12:00:00+08:00
weight: 5
author: Andrés Gaona
featuredImage: post_12/cover.webp
categories:
  - Robotics
  - Motion planning
tags:
  - ROS 2
  - MoveIt 2
  - MoveIt Task Constructor
  - Manipulation
  - Inverse kinematics
  - Collision checking
  - C++
draft: false
---

Building a pick-and-place system for a custom bionic panda robot, from the first robot model to reliable grasp planning with the complete upper body.

<!--more-->

## Overview & Challenges

The goal of this project was simple to describe: **make the panda robot see an object, plan how to reach it, pick it up, and place it somewhere else**.

Doing this reliably required more than moving an arm between two positions. The software had to understand the robot, locate the object, avoid collisions, and pass a safe motion to the low-level controller.

The project grew in several steps:

- Prepare the robot model for MoveIt
- Configure motion planning for one arm
- Connect planned trajectories to the existing control system
- Build a complete pick-and-place sequence
- Improve grasps that failed during planning
- Add the torso, second arm, and head to collision checking
- Test where the robot could complete the full task successfully

My work focused on preparing the robot model, configuring MoveIt, and connecting planned trajectories to low-level control. The wider project expanded this foundation with full-body modeling, grasp planning, and workspace testing.

---

## From Robot Description to Executable Motion

Before MoveIt can plan a motion, it needs an accurate description of the robot.

The **URDF/Xacro model** describes the robot's links, joints, limits, and physical shape. MoveIt adds information about the arms, gripper, and allowed contacts.

The motion pipeline can be summarized as:

1. Read the robot model and its current joint positions.
2. Receive a target for the arm or gripper.
3. Search for a motion that respects joint limits and avoids collisions.
4. Add timing to the motion.
5. Send the trajectory to the controller.
6. Monitor the real joint positions to confirm that the robot moved.

This last step is important. Seeing a successful animation in RViz only means that MoveIt found a path. It does not prove that the controller received it or that the physical robot followed it.

{{< image-pair
  left="post_12/img1_1.webp"
  left_alt="MoveIt Setup Assistant configuration, first view"
  right="post_12/img1_2.webp"
  right_alt="MoveIt Setup Assistant configuration, second view"
>}}

### Preparing the custom robot model

The arm was built as a chain of joints and links. Each moving link included a visual shape for display and a simpler shape for collision checking. A fixed link at the end represented the gripper reference point.

That final reference point told MoveIt exactly where the gripper should go. Without it, the arm could still move, but the result would be harder to control.

Using the MoveIt Setup Assistant, I configured:

- The connection between the robot and the world
- The arm planning groups
- The inverse-kinematics solver
- A default motion planner
- Useful predefined poses
- Joint velocity and acceleration limits
- The connection between MoveIt and the trajectory controller

Two small configuration problems showed how sensitive the complete pipeline can be. Missing acceleration limits prevented MoveIt from producing a usable trajectory. A missing action name prevented MoveIt from finding the controller that should execute it.

---

## Connecting MoveIt to the Existing Control Stack

The standard MoveIt demo uses a simulated controller. For this project, MoveIt had to work with the panda's existing low-level control system instead.

The launch process started three main components:

- A robot-state publisher to update the robot model from live joint data
- MoveIt's `move_group` process to plan motions
- RViz to display the robot, targets, and planned paths

The low-level controller had to be running first and publishing current joint positions. Otherwise, MoveIt would not know the real starting position of the arm.

The C++ application planned a trajectory for each target. A custom executor then smoothed the points, applied velocity limits, and passed commands to the motors.

After sending a trajectory, the program continued reading the joints. It moved to the next target only when the current one was close enough to its goal. If the arm did not arrive in time, the program reported a timeout.

The main lesson was straightforward: **sending a trajectory is not the same as completing a movement**. Planning, sending, execution, and feedback must all be checked separately.

<!-- ![2](post_12/img2_2.mp4) -->
<video controls style="display:block; margin:0 auto; width:75%;">
  <source src="img2_2.mp4" type="video/mp4">
</video>

<!-- ### A practical integration

The custom executor was a useful bridge to the existing controller, but it was not a hard real-time system. In a future version, I would use the standard `ros2_control` interface to handle execution, feedback, cancellation, and errors more consistently. -->

---

## Building the Pick-and-Place Task with MTC

Once the arm could follow MoveIt trajectories, the next step was to build a complete pick-and-place task with the MoveIt Task Constructor.

The system divided the task into smaller stages:

1. Receive the object's position from the perception system.
2. Add the object to MoveIt's planning scene.
3. Generate possible grasp positions.
4. Find a safe way to approach the object.
5. Close the gripper and attach the object to the robot model.
6. Move the object to the destination.
7. Release it and update the planning scene.

Breaking the task into stages made failures easier to understand. Instead of seeing only “planning failed,” we could identify whether the problem came from the object position, grasp angle, joint limits, or a collision.

<!--
IMAGE SLOT: img3.webp
Suggested source: Upper Body Pick and Place, page 3.
Suggested caption: MTC pipeline from object-pose input through scene management, task construction, and execution.
Add later as: ![MoveIt Task Constructor pipeline](post_12/img3.webp)
-->

### Improving grasp reliability

The first version often failed while searching for a valid grasp. The object was sometimes within reach, but the planner stopped before finding a suitable arm position.

There were two main reasons:

- The solver tried too few arm configurations.
- The gripper approached the object with only one palm orientation.

To improve this, the task was changed to:

- Try up to 32 inverse-kinematics solutions
- Generate 32 grasp angles around the bamboo
- Avoid keeping several nearly identical solutions
- Try a second grasp with the palm flipped in the opposite direction
- Use simpler collision shapes where detailed meshes were unnecessary

These changes gave the planner more useful choices. A grasp that failed with one hand orientation could succeed with the other.

{{< image-pair
  left="post_12/img4_1.webp"
  left_alt="Alternative grasp orientation, first view"
  right="post_12/img4_2.webp"
  right_alt="Alternative grasp orientation, second view"
>}}

### What an IK failure really means

Inverse kinematics calculates the joint positions needed to place the gripper at a target. A failure does not always mean that the target is too far away.

It can also mean that:

- The requested gripper angle is difficult to reach
- A joint would move beyond its limit
- The arm or gripper would collide with something
- The solver started from an unfavorable position
- The arm is close to a position where some movement directions become difficult

The improvements in this project came from better grasp choices, more IK candidates, and more accurate collision settings—not from replacing MoveIt's IK solver.

---

## Planned Contact Is Not Compliant Contact

The panda's custom gripper was designed so that part of the final arm link could touch the bamboo during a grasp. MoveIt originally treated this contact as a collision and rejected almost every valid grasp.

The solution was to tell MoveIt which hand and arm links were intentionally allowed to touch the object. After the bamboo was picked up, it was also attached to the robot model so MoveIt would continue considering its size while moving it.

This setting only tells the planner that a contact is expected. It does not measure force or make the arm physically compliant. Unexpected contact would need a separate safety layer with sensing, limits, and a defined stop or retreat response.

{{< image-pair
  left="post_12/img5_1.webp"
  left_alt="Gripper collision geometry, first view"
  right="post_12/img5_2.webp"
  right_alt="Gripper collision geometry, second view"
>}}

---

## Extending Planning to the Full Upper Body

The first tests used only one arm. This was useful for development, but it ignored possible collisions with the rest of the robot.

The model was therefore expanded to include:

- The left arm and hand
- The right arm and hand
- The torso
- The panda head and its collision geometry

This changed the planning problem. A gripper target could look valid while the elbow touched the body, the arm crossed the head, or the carried object hit another part of the robot.

<!-- During this work, the MoveIt Setup Assistant also started crashing while loading valid robot files. Testing with standard robot models showed that the problem was not our URDF. It came from a regression in the installed `rviz-common` package. Using a known working package version restored the setup process. -->

{{< image-pair
  left="post_12/img6_1.webp"
  left_alt="Upper-body collision model, first view"
  right="post_12/img6_2.webp"
  right_alt="Upper-body collision model, second view"
>}}

---

## Reachability as a Task-Level Test

To understand where the robot could work reliably, a test program moved the virtual bamboo through a three-dimensional grid.

At each position, the program ran the same complete pick-and-place planner used by the application. Green markers represented positions where the full task succeeded. Red markers represented positions where it failed.

The test covered:

- `x = 0.20` to `0.40 m`
- `y = -0.30` to `0.20 m`
- `z = 0.10` to `0.50 m`
- A spacing of `0.05 m` between test points

Successful tasks were found within a smaller region: approximately `x = 0.20-0.35 m`, `y = -0.30-0.15 m`, and `z = 0.15-0.40 m`.

This was more useful than checking whether the arm could simply touch each point. A green result meant that the planner found the complete sequence: approach, grasp, lift, transfer, and placement.

It was still a planning result, not a hardware success rate. Real operation also depends on camera accuracy, calibration, motor tracking, contact, and changes in the environment.

<!-- ![7](post_12/img7_1.mp4) -->
<video controls style="display:block; margin:0 auto; width:75%;">
  <source src="img7_1.mp4" type="video/mp4">
</video>

---

## Debugging a Valid Plan That Does Not Execute

When RViz shows a valid path but the arm does not move, I check the system in order:

1. Was the motion executed, or only previewed?
2. Did MoveIt report a successful plan?
3. Is the correct controller running and connected?
4. Do the trajectory joints match the controller joints?
5. Are the measured joint positions and robot frames current?
6. Is the low-level controller enabled and free of faults?

Following the data from one component to the next is usually faster than changing planner settings at random. It also shows whether the problem belongs to planning, communication, feedback, or the motor-control system.

---

## Engineering Tradeoffs & What I Would Improve Next

This project also revealed several useful tradeoffs:

- The custom executor connected quickly to the existing controller, but a standard `ros2_control` connection would simplify feedback, cancellation, and error handling.
- Trying more grasp options improved reliability, but increased planning time.
- Detailed meshes looked better, while simpler shapes made collision checking faster and more stable.
- The reachability map helped choose good working positions, but could not guarantee success in a changing environment.

A future version should combine the planning tests with repeated hardware trials and measured execution results.

---

## Results & Takeaways

- Prepared a custom panda-arm model for MoveIt
- Configured planning groups, poses, joint limits, and controller connections
- Connected MoveIt trajectories to the existing low-level control path
- Added measured completion and timeout checks between motions
- Built a staged pick-and-place task using MTC
- Improved grasp planning with more IK candidates and two palm orientations
- Added the second arm, torso, and head to collision checking
- Created a three-dimensional map of successful pick-and-place positions

The most valuable result was not one successful demonstration. It was learning how to separate the system into clear parts and identify where a failure happened: the robot model, object pose, grasp, collision scene, planner, trajectory connection, feedback, or low-level control.

That structure made the system easier to understand, test, and improve.

---

<!--
AUTHOR CONFIRMATION BEFORE PUBLISHING
1. Confirm which MTC, upper-body, head-URDF, and reachability components you personally implemented versus contributed to by teammates.
2. Confirm whether the custom trajectory path was tested on physical hardware, simulation, or both.
3. Add any measured planning success rate, execution success rate, timing, or repeat-trial count only if you can recover the test method.
4. Confirm whether the public post may name RF_L6, the bamboo object, and the internal package structure.
5. Review the restored images and videos together with the final text before publishing.
-->

## Links
