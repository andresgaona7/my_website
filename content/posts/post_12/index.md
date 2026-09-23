---
title: From URDF to Reliable Pick-and-Place with ROS 2 and MoveIt 2
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

Building a manipulation pipeline for a custom bionic panda robot: from URDF and MoveIt configuration to trajectory execution, collision-aware grasping, upper-body planning, and systematic reliability improvements.

<!--more-->

<!--
IMAGE SLOT: cover.webp
Suggested source: Upper Body Pick and Place, page 3, or Head URDF, page 4.
Suggested caption: Full upper-body model and collision-aware manipulation scene in RViz.
-->

## Overview & Challenges

This project explored how to turn a custom robot description into a working manipulation system using **ROS 2 Jazzy**, **MoveIt 2**, and the **MoveIt Task Constructor (MTC)**. The work progressed from configuring and moving one arm to planning pick-and-place tasks with both arms and the complete upper-body collision model.

The main engineering challenges were:

- Converting a custom Xacro/URDF model into a valid MoveIt configuration
- Defining planning groups, end-effector frames, joint limits, and collision geometry correctly
- Connecting planned trajectories to an existing low-level control path
- Distinguishing successful planning from successful execution
- Improving grasp reliability when IK, joint limits, or collision checking rejected candidates
- Extending a single-arm model to an upper-body scene where the arms, torso, and head must remain collision-free
- Measuring the useful task workspace instead of assuming that every geometrically reachable point supported a complete pick-and-place plan

My work in the project focused on the MoveIt setup, robot-model preparation, launch and API integration, and the trajectory path between MoveIt and low-level control. The wider project then extended this foundation with upper-body modeling, MTC task construction, grasp-reliability work, and reachability testing.

---

## From Robot Description to Executable Motion

A useful way to understand the system is to separate its responsibilities:

1. **URDF/Xacro** describes the link and joint tree, joint axes and limits, visual geometry, and collision geometry.
2. **SRDF and MoveIt configuration** define semantic information such as planning groups, named states, virtual joints, end effectors, and justified collision exclusions.
3. **The planning scene** combines the current robot state with the collision environment and attached objects.
4. **The planner and IK solver** search for valid joint configurations and collision-free paths.
5. **Trajectory processing** assigns positions, velocities, and timing to the path.
6. **The execution layer** converts that trajectory into commands for the low-level controller.
7. **Joint-state feedback and TF** close the loop by reporting where the robot is and how its frames relate.

This separation matters because a valid path in RViz proves only that planning succeeded against the model and scene used at that moment. It does not prove that a controller accepted the trajectory, that the hardware moved, or that the measured state reached the goal.

{{< image-pair
  left="post_12/img1_1.webp"
  left_alt="MoveIt Setup Assistant configuration, first view"
  right="post_12/img1_2.webp"
  right_alt="MoveIt Setup Assistant configuration, second view"
>}}

### Preparing the custom URDF

The arm model was organized as a Xacro chain. Each actuated section contained a revolute joint, a link, visual geometry, and simplified collision geometry. A final fixed link represented the tool/end-effector frame.

That final frame was important: planning targets must refer to a meaningful tool frame, not an arbitrary upstream link. A missing or misaligned tool frame can produce motion that is mathematically valid but unintuitive at the gripper. The same applies to incorrect joint axes, parent-child relationships, mesh scales, or frame conventions.

The model was then loaded into the MoveIt Setup Assistant, where I configured:

- The robot-to-world virtual joint
- Self-collision sampling and the semantic collision matrix
- Arm planning groups
- A KDL kinematics solver
- An RRT-family default planner
- Named robot poses
- Joint velocity and acceleration limits
- The controller name, joint list, and `follow_joint_trajectory` action namespace

Two configuration errors demonstrated how planning and execution fail at different boundaries. Missing acceleration limits prevented a usable timed trajectory, while a missing controller action namespace left MoveIt without the correct execution endpoint.

---

## Connecting MoveIt to the Existing Control Stack

For the real-control launch path, the generated MoveIt configuration was reused without its fake controller. The launch description started:

- `robot_state_publisher`, which used measured joint states to publish the robot transforms
- `move_group`, which exposed the configured planning groups and planning pipeline
- RViz, which visualized the current state, targets, and planned motion

Before starting this layer, the low-level controller had to be active and publishing fresh joint states. Without current feedback, MoveIt could plan from a stale or unknown start state even if the model looked correct in RViz.

The C++ application used `MoveGroupInterface` to load joint targets, request plans, and retrieve the resulting `JointTrajectory`. Instead of relying on a standard `ros2_control` trajectory controller, the trajectory was published to a custom execution component. That component sampled the trajectory with spline interpolation, applied velocity limits, and produced smoother position commands for the existing motor-control path.

After publishing each trajectory, the application monitored the measured joints at 100 Hz. It accepted completion when the maximum joint error fell below a configured tolerance and reported a timeout otherwise. This prevented the application from issuing the next target merely because the previous trajectory had been published.

```cpp
move_group.setJointValueTarget(target.joints);
auto result = move_group.plan(plan);

if (result == moveit::core::MoveItErrorCode::SUCCESS) {
  auto trajectory = plan.trajectory_.joint_trajectory;
  trajectory.header.stamp = node->get_clock()->now();
  trajectory_pub->publish(trajectory);
}
```

The important boundary is that **publication is not execution**. A production implementation should check the planning result, controller acceptance, execution result, feedback freshness, timeout, and fault state independently.

<!-- ![2](post_11/img2_2.mp4) -->
<video controls style="display:block; margin:0 auto; width:75%;">
  <source src="img2_2.mp4" type="video/mp4">
</video>

### Why this was not a hard real-time claim

The custom executor provided interpolation, velocity limiting, and completion monitoring, but these notes do not establish a hard real-time deadline or bounded worst-case latency. The 100 Hz loop described the **monitoring rate**, not proof of deterministic motor control. Planning, logging, memory allocation, ROS callbacks, and collision checking also belong outside a hard real-time actuator loop.

The interface was useful because it connected MoveIt to the existing control stack quickly and made the ownership of each stage visible. For a more standard and scalable architecture, I would use a `ros2_control` hardware interface and a `joint_trajectory_controller`, preserve the low-level safety layer, and report controller results through the normal action interface.

---

## Building the Pick-and-Place Task with MTC

The manipulation pipeline was decomposed into explicit stages rather than treated as one opaque planning request:

1. A pose subscriber received the perceived object pose.
2. A scene manager inserted the bamboo object into the planning scene.
3. The MTC task builder generated grasp poses, solved IK, planned approach and transfer motions, and updated the scene.
4. The task executor ran the selected solution.
5. An orchestrator coordinated perception, scene updates, planning, and execution.

This structure made failures easier to localize. A task could fail because perception supplied a pose in the wrong frame, the goal was outside the workspace, IK found no acceptable branch, a candidate violated a joint limit, collision checking rejected the grasp, or execution failed after planning had succeeded.

<!--
IMAGE SLOT: img3.webp
Suggested source: Upper Body Pick and Place, page 3.
Suggested caption: MTC pipeline from object-pose input through scene management, task construction, and execution.
Add later as: ![MoveIt Task Constructor pipeline](post_12/img3.webp)
-->

### Improving `ComputeIK` reliability

The original task often failed at the grasp-pose/`ComputeIK` stage. The problem was not simply that the object was unreachable. The solver had too few opportunities to explore a redundant arm, and the task offered only one fixed palm orientation.

The reliability changes were:

- Increase the maximum number of accepted IK candidates to 32
- Sample 32 grasp poses around the bamboo axis using an angle step of `pi / 16`
- Enforce a minimum distance between IK solutions to avoid nearly identical candidates
- Add a second, flipped palm orientation inside an MTC `Alternatives` container
- Refine collision geometry so complex meshes did not create unnecessary planning cost or misleading contacts

The key lesson is that an IK failure is a category, not a diagnosis. A pose can be geometrically reachable yet rejected because of the seed, orientation constraint, joint limits, self-collision, environmental collision, or the allowed attempt budget.

{{< image-pair
  left="post_12/img4_1.webp"
  left_alt="Alternative grasp orientation, first view"
  right="post_12/img4_2.webp"
  right_alt="Alternative grasp orientation, second view"
>}}

### IK, Jacobians, and singularities

Locally, the Jacobian maps joint velocity to end-effector velocity: `xdot = J(q) qdot`. If the Jacobian loses rank at a singularity, the robot loses instantaneous motion capability in at least one task-space direction. Near a singularity, small Cartesian commands can demand very large joint velocities.

Damped least-squares IK reduces that sensitivity by trading exact task tracking for better numerical behavior. It does not make unreachable poses reachable, remove collisions, or override joint limits. In this project, the documented reliability work expanded the candidate set and grasp orientations; it did **not** document a custom damped-IK implementation. That distinction is important when explaining what was built versus what could be added next.

---

## Planned Contact Is Not Compliant Contact

The custom gripper required part of link `RF_L6`, together with the hand links, to approach or touch the bamboo. MoveIt rejected these configurations until the task explicitly allowed collision between the object and the links that were intended to participate in grasping. This allowance was needed during approach and after attachment so the carried object remained represented correctly in the scene.

The allowed-collision matrix encodes **planning semantics**: which geometric contacts should or should not invalidate a state. It is not a force controller and does not make physical contact safe.

For unexpected shelf contact on hardware, I would use a separate response based on the available sensors and command interface: stop or retreat thresholds, wrench bias and gravity compensation, frame-correct force estimation, velocity/force limits, and a defined transition into a compliant mode. Impedance control would command motion from a desired force-motion relationship; admittance control would convert measured force into a motion command for a position-controlled inner loop. Neither behavior was validated by the MoveIt collision configuration described here.

{{< image-pair
  left="post_12/img5_1.webp"
  left_alt="Gripper collision geometry, first view"
  right="post_12/img5_2.webp"
  right_alt="Gripper collision geometry, second view"
>}}

---

## Extending Planning to the Full Upper Body

The single-arm setup was later extended to an upper-body model with separate left-arm, left-hand, right-arm, and right-hand groups. The head was decomposed into a short link chain with dedicated collision geometry, allowing the planning scene to represent more than the active arm.

This matters because a hand pose can be valid while the elbow, opposite arm, head, torso, or attached object collides along the path. Planning against the full body exposed constraints that a single-arm model could not see.

The full model also revealed a tooling problem unrelated to the robot itself: the MoveIt Setup Assistant crashed while loading valid URDF/Xacro files because of an `rviz-common` regression. Reproducing the failure with standard robot descriptions helped separate a binary-package problem from a model problem; using a known-good package snapshot restored the setup workflow.

{{< image-pair
  left="post_12/img6_1.webp"
  left_alt="Upper-body collision model, first view"
  right="post_12/img6_2.webp"
  right_alt="Upper-body collision model, second view"
>}}

---

## Reachability as a Task-Level Test

A dedicated test node sampled bamboo positions on a three-dimensional grid. For every position it inserted the object into the scene and ran the same complete MTC pick-and-place pipeline used by the application. Successful positions were visualized as green voxels and failures as red voxels in RViz.

The scan covered:

- `x = 0.20` to `0.40 m`
- `y = -0.30` to `0.20 m`
- `z = 0.10` to `0.50 m`
- A grid step of `0.05 m`

The reported region in which at least one complete task succeeded extended over `x = 0.20-0.35 m`, `y = -0.30-0.15 m`, and `z = 0.15-0.40 m`. This is more informative than checking IK alone: every green voxel represents a position for which the full staged plan succeeded under the model, scene, constraints, and planning settings used in the test.

It is still not a hardware success rate. A plan found in simulation does not account for calibration error, perception latency, actuator tracking, object uncertainty, contact forces, or scene changes after planning.

<!-- ![7](post_11/img7_1.mp4) -->
<video controls style="display:block; margin:0 auto; width:75%;">
  <source src="img7_1.mp4" type="video/mp4">
</video>


---

## Debugging a Valid Plan That Does Not Execute

When RViz displays a valid trajectory but the robot does not move, I trace the system boundary by boundary:

1. Confirm that execution was requested, not only planned or previewed.
2. Check the planning result before reading or publishing the trajectory.
3. Verify that the expected controller or custom executor is running.
4. Confirm the action or topic name, namespace, and message type.
5. Compare trajectory joint names and ordering with the controller configuration.
6. Check that joint-state feedback is fresh and uses the expected units and signs.
7. Inspect TF and the target frame for stale or incorrect transforms.
8. Check joint limits, timing, and trajectory timestamps.
9. Inspect low-level enable state, drive faults, communication state, and whether commands change.
10. Monitor execution error and define timeout, cancellation, and recovery behavior.

This method avoids guessing. The first boundary with missing evidence usually identifies whether the failure belongs to planning, controller integration, feedback, or hardware.

---

## Engineering Tradeoffs & What I Would Improve Next

### Custom trajectory bridge vs. standard control integration

The custom publisher and spline executor integrated quickly with the existing low-level controller and made trajectory processing easy to inspect. The tradeoff was that it also required custom handling for acceptance, convergence, timeout, cancellation, and faults. A standard `FollowJointTrajectory` action through `ros2_control` would reduce custom orchestration and improve interoperability.

### More IK candidates vs. planning cost

Increasing the candidate budget and adding an alternative palm orientation improved the chance of finding a valid grasp, but each added candidate consumes planning and collision-checking time. The better long-term approach is to combine deliberate grasp generation, good seeds, meaningful orientation alternatives, and measured planning budgets.

### Detailed meshes vs. robust collision checking

High-detail visual meshes are useful for rendering but can be expensive or brittle for collision checking. Simple primitives and purpose-built convex geometry are often better for planning, provided they conservatively represent the occupied space.

### Offline reachability vs. online guarantees

The voxel scan is valuable for workspace design, object placement, and regression testing. It does not guarantee that a dynamic scene will remain valid at execution time. I would add automated scenario tests, repeat trials with fixed random seeds where appropriate, planning-time statistics, execution outcomes, and hardware validation with calibrated scene geometry.

---

## Results & Takeaways

- Built a MoveIt configuration for a custom panda arm from its Xacro/URDF model
- Defined semantic planning groups, named states, collision settings, joint limits, and controller mapping
- Connected `MoveGroupInterface` planning to a custom trajectory interpolation and low-level control path
- Separated plan generation, trajectory publication, measured completion, and timeout handling
- Extended the scene from a single arm to a dual-arm upper-body model with head and body collision geometry
- Built an MTC pick-and-place pipeline driven by an external object pose
- Improved grasp planning by expanding IK candidates, adding palm-orientation alternatives, and refining collision semantics
- Mapped the region where a complete staged pick-and-place plan could be found
- Documented the limits clearly: planned contact is not compliant control, an RViz plan is not hardware execution, and a 100 Hz monitor is not proof of hard real-time behavior

The most important outcome was not a single successful plan. It was a manipulation stack whose failures could be classified and investigated at the correct layer: model, frames, IK, collision scene, planner, trajectory interface, feedback, or hardware.

---

<!--
AUTHOR CONFIRMATION BEFORE PUBLISHING
1. Confirm which MTC, upper-body, head-URDF, and reachability components you personally implemented versus contributed to by teammates.
2. Confirm whether the custom trajectory path was tested on physical hardware, simulation, or both.
3. Add any measured planning success rate, execution success rate, timing, or repeat-trial count only if you can recover the test method.
4. Confirm whether the public post may name RF_L6, the bamboo object, and the internal package structure.
5. Add cover.webp and the numbered images above, then uncomment featuredImage.
-->

## Links
