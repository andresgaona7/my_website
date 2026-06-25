# Professional Charming Website Redesign Plan

## Context

The current homepage at `http://127.0.0.1:8123/` is a Hugo site using the LoveIt theme with a custom homepage layer. The content is strong: clear robotics positioning, real project media, and a solid project inventory. The main opportunity is presentation. The site currently reads more like a themed blog with project cards added than a deliberate robotics R&D portfolio.

The redesign should make the site look more professional while preserving the personal charm of the panda identity and robotics imagery.

## Primary Direction

Keep the panda charm, but give the page a more confident editorial hierarchy:

- A stronger hero that immediately communicates who Andrés is and what robotics systems he builds.
- A professional color system with restrained technical accents.
- A curated project hierarchy rather than a flat grid of similarly weighted cards.
- Better mobile first-screen impact.
- More scannable technical proof points for recruiters, engineers, and collaborators.

## Recommended Changes

### 1. Stronger Hero

The current hero places the image first on mobile and gives it a large amount of early-screen space. On desktop, the composition is pleasant, but it still feels closer to a profile block than a portfolio landing section.

Recommended changes:

- Lead with `Andrés Gaona` and the robotics positioning.
- Keep the portrait/panda image as a supporting visual.
- On mobile, show the name and value proposition before or alongside the image so visitors understand the site immediately.
- Add a compact role/discipline label such as `Robotics R&D Engineer` above the headline.
- Keep the social links, but style them as deliberate actions rather than plain inline theme links.

### 2. Professional Color System

The current palette is mostly white, black, and gray. It is clean, but it lacks a distinctive professional identity.

Recommended light palette:

- Page background: `#F7F8F6` or `#FAFAF7`
- Main text: `#111827`
- Secondary text: `#56616A`
- Primary accent: `#16697A`
- Secondary accent: `#C58A1A`
- Card background: `#FFFFFF`
- Border: `#E3E7E4`

Recommended dark palette:

- Page background: `#101820`
- Surface: `#16212B`
- Main text: `#F2F5F3`
- Secondary text: `#A8B3B0`
- Primary accent: `#4CB3C4`
- Secondary accent: `#D6A642`
- Border: `#26333D`

This keeps the site technical and mature, while the warm amber and panda identity preserve charm.

### 3. Restructure Project Hierarchy

The six featured projects currently compete equally. The portfolio would feel more curated if the strongest project receives more visual weight.

Recommended changes:

- Make the MCCL / EtherCAT project a flagship feature card or wide horizontal project row.
- Present the next four or five featured projects in a tighter grid.
- Keep `More Robotics Projects`, but make it more compact than the featured section.
- Use consistent image ratios and tighter copy so the page feels intentional.

### 4. Add Technical Proof Chips

The site has strong technical content, but visitors have to read paragraphs to extract the signal.

Recommended chips:

- `EtherCAT`
- `ROS2`
- `C++`
- `Real-time Control`
- `AI Vision`
- `AMRs`
- `Legged Robots`
- `Industrial Robotics`

Possible placements:

- Under the hero subtitle.
- At the top of the featured project section.
- Inside project cards as small technology labels.

### 5. Improve Project Cards

Current cards are functional, but they feel like default blog cards.

Recommended changes:

- Use softer borders and reduced shadow.
- Add a small project category or technology label.
- Make title, summary, and action spacing more consistent.
- Use a clearer action style for `View project`.
- Consider an accent line or small corner detail using the teal accent.
- Keep card radius at or below `8px` for a polished technical feel.

### 6. Refine Header

The panda-only brand is charming, but it does not clearly identify whose site this is.

Recommended changes:

- Change the brand from only `🐼` to `🐼 Andrés Gaona`.
- Keep navigation simple: `Home`, `About`, `Projects`, `CV`.
- Use a subtle bottom border.
- Give the active nav item a restrained teal accent.
- Keep the theme switch, but visually align it with the rest of the header.

### 7. Strengthen Contact Section

The current `Let's talk robotics` section works, but it feels like another card.

Recommended changes:

- Turn it into a stronger closing band.
- Use a dark navy or teal-tinted surface.
- Keep copy concise.
- Make `Email me` the primary action.
- Keep secondary actions: `Download CV`, `LinkedIn`, `GitHub`, `All projects`.

## Implementation Targets

Most of the visual work should be concentrated in:

- `assets/css/_custom.scss`
- `layouts/index.html`

Supporting content/data changes may touch:

- `data/home_projects.toml`
- `hugo.toml`

Avoid large theme edits unless necessary. The current custom homepage layer is already separated from the LoveIt theme and is the right place to implement the redesign.

## Suggested First Implementation Pass

1. Update the color tokens and homepage custom styles in `assets/css/_custom.scss`.
2. Adjust the homepage structure in `layouts/index.html`:
   - hero eyebrow/role label
   - technical chips
   - flagship project card treatment
3. Update header branding in `hugo.toml` from panda-only to panda plus name.
4. Verify desktop and mobile at `http://127.0.0.1:8123/`.
5. Check dark mode manually after the light theme looks correct.

## Design Guardrails

- Keep the panda as a charming identity mark, but avoid making the whole page playful.
- Avoid heavy gradients, decorative blobs, or generic tech wallpaper.
- Keep the palette restrained: teal for technical confidence, amber for warmth.
- Prefer dense, scannable project evidence over marketing-style sections.
- Make mobile first-screen content communicate the value proposition before the image consumes the viewport.
