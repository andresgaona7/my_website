# About Page Recruiter Refresh

## Summary

Rework `/about/` into a polished recruiter-facing bridge between the CV and project portfolio. The page should present Andres as a robotics R&D engineer focused on real-time control software, robotic hardware integration, quadruped robots, AMRs, and vision-guided manipulation, while keeping wording conservative around AI vision and EtherCAT.

## Key Changes

- Rewrite the opening around this positioning:
  `Robotics R&D engineer focused on real-time control software, robotic hardware integration, quadruped robots, autonomous mobile robots, and vision-guided manipulation.`
- Use EtherCAT carefully:
  - Highlight it as the core of the MCCL project.
  - Mention it elsewhere only as supporting industrial communication/device integration.
- Avoid claiming broad `AI vision systems` expertise. Use safer terms like `vision-guided manipulation`, `robotic perception`, or `computer-vision-assisted robotics`.
- Replace the current raw CV-style Markdown with a structured page:
  - Intro + portrait
  - CTA row: `Download CV`, `View Projects`, `Email`
  - `What I Do`
  - `Selected Project Evidence`
  - Skills
  - Experience
  - Education and languages
  - Bottom `Let's talk robotics` contact box
- Fix indented Markdown lists so they render as normal content, not code blocks.
- Add scoped About-page styling in `assets/css/_custom.scss`, matching the current violet-blue theme.

## Content Structure

### What I Do

- Real-time control software
- Robotic hardware integration
- Legged robotics and torque control
- AMR and autonomous systems
- Vision-guided manipulation

### Selected Project Evidence

- Real-Time Multi-Vendor EtherCAT Motion Control
- Quadruped Locomotion & Control Platform
- Bio-Inspired Bionic Panda Robot
- Autonomous Mobile Robot for Indoor Environments
- Deep Learning-Driven Robotic Plastic Waste Sorter
- Robotic Grasping Using Evolutionary Deep Neural Networks

### Bottom CTA Box

- Keep `Let's talk robotics`.
- Use recruiter-focused copy:
  `Interested in robotics R&D, real-time control, robotic hardware integration, or autonomous systems? Reach me directly or review my CV and project portfolio.`
- Include actions:
  - `Email me`
  - `Download CV`
  - `LinkedIn`
  - `GitHub`
  - `All projects`

## Test Plan

- Run `hugo --minify`.
- Inspect `/about/`, `/`, `/posts/`, and one project page.
- Verify desktop and mobile layout.
- Check all links: CV, Projects, email, GitHub, LinkedIn, and selected project links.
- Run `git diff --check`.

## Assumptions

- The About page should complement the CV, not duplicate it.
- The public CV remains `static/andres-gaona-cv.pdf`.
- The homepage remains the main portfolio landing page.
- The wording should stay truthful and conservative: robotics systems first, AI/perception and EtherCAT as supporting strengths except where they are the actual project focus.
