# Recruiter-Impact Portfolio Layout Plan

## Goal

Rework the AG website so recruiters see the strongest robotics evidence first. The site should feel like a portfolio landing page, not a chronological blog. The first screen should quickly communicate: real-time robotics systems, EtherCAT/C++ infrastructure, legged robot control, AMR leadership, and AI vision/manipulation deployment.

## Source Context

- Website workspace: `/Users/andresgaona/Documents/my_website`
- CV workspace: `/Users/andresgaona/Documents/cv`
- Current live local page inspected: `http://127.0.0.1:8123/page/2/`
- Relevant CV project clusters:
  - Real-Time Multi-Vendor EtherCAT Motion Control Platform
  - Quadruped Robot Locomotion & Control Framework
  - Autonomous Mobile Robot for Indoor & Hospital Logistics
  - Deep Learning Robotic Plastic Waste Sorter
  - Vision-Guided Robotic Manipulation & Path Generation
  - Smart Tuning & Optimization for Motion Control
- Important clarification: `Four-Legged Robot Platform` and `Bio-Inspired Robots (Bionic Panda)` are two different projects and should remain separate.

## Intended Final Homepage Layout

| Position | Section or project | Purpose |
|---:|---|---|
| 1 | Hero: Andres Gaona | State the target profile clearly: robotics R&D engineer building real-time robotic systems across EtherCAT motion control, legged robots, AMRs, and AI vision. |
| 2 | Real-Time Multi-Vendor EtherCAT Motion Control (MCCL) | Show production-grade C++/EtherCAT infrastructure, multi-vendor support, deterministic control, and customer impact. |
| 3 | Quadruped Locomotion & Control Platform | Show low-level quadruped platform engineering: torque control, motor communication, PREEMPT-RT, MPC/WBC, latency, and long-duration validation. |
| 4 | Bio-Inspired Bionic Panda Robot | Show advanced behavior work: bio-inspired locomotion, climbing, balance recovery, AI decision-making, simulation-to-real validation. |
| 5 | Autonomous Mobile Robot for Indoor / Hospital Logistics | Show current leadership, ROS2, EtherCAT, navigation, semantic mapping, and end-to-end system integration. |
| 6 | Deep Learning Robotic Plastic Waste Sorter | Show deployed AI robotics in industrial conditions: YOLOv4, GPU inference, conveyor tracking, delta robot picking, throughput, and accuracy. |
| 7 | Robotic Grasping Using Evolutionary Deep Neural Networks | Show AI manipulation research validated on real hardware: custom dataset, CNN, PSO, inference speed, and grasp success rate. |
| 8 | More Robotics Projects | Secondary grid: Robotic Controllers & Vision-Guided Manipulation, Smart Tuning Technology, Robotic Arm Automatic Path Generation, AR/VR Robot Arm Teaching, Automated Satellite Antenna Tracking. |
| 9 | About / Skills Preview | Compact skills strip: ROS2, EtherCAT, C++, Python, MPC/WBC, perception, Isaac Sim/Lab, real-time Linux. |
| 10 | Contact CTA | CV download, GitHub, email, and LinkedIn if available. |

## Task 1 - Audit Current Content and Ordering

Objective: confirm the current source of truth before editing.

Steps:

1. Inspect `hugo.toml` for homepage and menu behavior.
2. Inspect all project Markdown files under `content/posts/post_*/index.md`.
3. Confirm the current homepage ordering and `/page/2/` ordering through the local site.
4. Identify whether Hugo ordering is controlled only by `date`, or whether `weight` / custom front matter can be used cleanly.

Acceptance checks:

- Produce a list of current project titles, source files, current homepage/page-2 visibility, and desired rank.
- Confirm which Hugo mechanism will control recruiter-first ordering.

## Task 2 - Add Recruiter-Focused Homepage Structure

Objective: make the first screen function as a portfolio landing page.

Recommended implementation:

1. Keep the current Hugo theme, but add a dedicated featured-projects layout or homepage partial if the theme makes that cleaner.
2. Rename or supplement the `Posts` navigation with `Projects`.
3. Add a short hero subtitle that matches the CV:
   - `Robotics R&D engineer building real-time robotic systems across EtherCAT motion control, legged robots, AMRs, and AI vision.`
4. Add a `Featured Robotics Projects` section before the normal post list.
5. Keep the normal post archive available below the featured section or under a secondary page.

Acceptance checks:

- A recruiter opening `/` sees the hero and featured project list without needing to click pagination.
- The page still links to all existing project detail pages.
- The site remains directly buildable with the existing Hugo workflow.

## Task 3 - Reorder Featured Projects by Recruiter Impact

Objective: put the strongest interview-conversion projects first.

Target featured order:

1. `Real-Time Multi-Vendor EtherCAT Motion Control (MCCL)`
2. `Four-Legged Robot Platform`
3. `Bio-Inspired Robots (Bionic Panda)`
4. `Autonomous Mobile Robot (AMR) for Indoor Environments`
5. `Deep Learning-Driven Robotic Plastic Waste Sorter`
6. `Robotic Grasping Using Evolutionary Deep Neural Networks`

Secondary order:

1. `Robotic Controllers & Vision-Guided Manipulation`
2. `Smart Tuning Technology`
3. `Robotic Arm Automatic Path Generation Technology`
4. `Intelligent AR/VR Robot Arm Teaching Technology`
5. `Automated Satellite Antenna Tracking System`

Acceptance checks:

- `Robotic Grasping Using Evolutionary Deep Neural Networks` is no longer buried behind `/page/2/`.
- `Automated Satellite Antenna Tracking System` is moved below the core robotics projects.
- The two legged projects remain separate and are not merged.

## Task 4 - Make the Two Legged Robot Projects Clearly Different

Objective: prevent recruiters from thinking the two legged robot entries are duplicates.

Suggested card positioning:

| Project | Card title | Recruiter-facing summary |
|---|---|---|
| Four-Legged Robot Platform | Quadruped Locomotion & Control Platform | Torque-controlled quadruped platform with EtherCAT/RS485/LCM motor communication, PREEMPT-RT tuning, MPC/WBC locomotion, sub-ms latency, and 6+ hour validation. |
| Bio-Inspired Robots (Bionic Panda) | Bio-Inspired Bionic Panda Robot | Bio-inspired quadruped focused on adaptive behaviors, climbing, balance recovery, autonomous decision-making, simulation-to-real control, and long-duration behavior validation. |

Acceptance checks:

- The project cards communicate different engineering scopes.
- Each detail page opens with a distinct first paragraph.
- Shared terms like torque control, MPC, WBC, and simulation are used carefully so they reinforce depth without making the pages sound identical.

## Task 5 - Strengthen Project Card Summaries

Objective: make every featured card answer "why should I interview this person?" in one glance.

Use these impact hooks:

| Project | Impact hook to surface |
|---|---|
| MCCL | 84+ EtherCAT devices, real-time C++, ~20% broader compatibility, 100% customer-request growth. |
| Four-Legged Robot Platform | Sub-millisecond latency, <10 ms communication, 6+ hours continuous operation, 90% real-world success. |
| Bionic Panda | Adaptive behaviors, climbing, balance recovery, ~90% real-world success, simulation-to-real validation. |
| AMR | ROS/ROS2, EtherCAT, navigation, odometry, semantic mapping, current team leadership and system integration. |
| Plastic Waste Sorter | YOLOv4, ~97% detection/classification accuracy, ~21 FPS, ~60 cycles/min, real industrial deployment. |
| Robotic Grasping | 1.5M+ augmented samples, 91.5% classification accuracy, 94% physical grasp success, ~10x faster inference. |

Acceptance checks:

- Each featured card includes at least one concrete metric or deployment signal.
- Card text is concise enough to scan.
- Claims remain consistent with the existing CV and project pages.

## Task 6 - Add Recruiter Navigation and Calls to Action

Objective: make it easy for a recruiter to move from portfolio proof to contact.

Recommended changes:

1. Add or rename top navigation to include `Projects`.
2. Keep `About me` visible.
3. Add a clear `Download CV` link if a public PDF is available or can be added to `static/`.
4. Keep GitHub visible.
5. Add email/contact CTA near the end of the homepage.

Acceptance checks:

- A recruiter can reach projects, about, GitHub, and contact in one click.
- The navigation labels are professional and direct.

## Task 7 - Build and Visual Verification

Objective: verify the final result as a user would see it.

Steps:

1. Build the Hugo site with the repo's existing Hugo workflow.
2. Serve the generated site locally.
3. Inspect `/`, `/posts/`, and `/page/2/` if pagination remains.
4. Confirm mobile and desktop readability.
5. Check that image/video media still loads for featured projects.

Acceptance checks:

- Homepage first viewport shows the recruiter-focused hero and at least the start of the featured project section.
- Featured ordering matches this plan.
- All project links work.
- No obvious layout overlap, clipped text, or broken media in the first screen.

## Suggested Implementation Sequence

1. Audit current Hugo ordering and source files.
2. Choose the least invasive ordering mechanism.
3. Add a featured projects section on the homepage.
4. Update card titles/summaries for the six featured projects.
5. Adjust navigation labels and CTA links.
6. Build and verify locally.

## Non-Goals

- Do not rewrite all project detail pages in the first pass.
- Do not remove the satellite tracking project.
- Do not merge `Four-Legged Robot Platform` and `Bio-Inspired Robots (Bionic Panda)`.
- Do not change CV source files unless a later task explicitly asks to align CV wording with the website.
