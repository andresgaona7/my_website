# Website Color Theme Update Plan

## Summary

- Both existing `.agents` plans are partially finished, but recruiter ordering is out of scope for this theme task.
- The active website styling lives in `assets/css/_custom.scss`.
- `robotics_dark_portfolio.css` and `robotics_light_portfolio.css` are not active site styles. They should be treated as color/style references for this task.

## Implementation Changes

- Update only the active Hugo styling path: `assets/css/_custom.scss`.
- Replace the current teal/amber palette with the selected violet-blue robotics palette from the standalone CSS references:
  - Light: `#f7f8ff`, `#ffffff`, `#f0f2ff`, `#111321`, `#4f5670`, `#6b4cff`, `#5750df`, `#2f5bea`.
  - Dark: `#000000`, `#0b0b0f`, `#14141b`, `#ffffff`, `#cccccc`, `#5f4bdf`, `#5750df`, `#4a58e0`.
- Apply the palette consistently across body, header, homepage hero, project cards, labels, buttons, CTAs, contact band, post/archive surfaces, code blocks, tables, blockquotes, links, and selection color.
- Do not copy `robotics_*_portfolio.css` wholesale. Adapt the palette into the existing Hugo selectors and custom homepage structure.
- Keep the current polished 8px-ish radius scale instead of adopting the standalone files' 14px card radius.
- Use glow effects sparingly on primary CTA, avatar/media frame, and hover states only.
- Keep the theme toggle implementation unchanged: `hugo.toml` loads `assets/js/two-state-theme.js`, which switches `body[theme]`.

## Public Interfaces

- No route, content, project order, navigation, or JavaScript API changes.
- Existing routes stay the same: `/`, `/posts/`, `/about/`, and `/andres-gaona-cv.pdf`.
- The visible change is purely the color theme: violet-blue robotics styling in light and dark modes.

## Test Plan

- Run `hugo --minify`.
- Serve `public/` locally and inspect `/`, `/posts/`, one project detail page, and `/about/`.
- Verify light and dark modes both update all custom surfaces.
- Check desktop and mobile widths for readable contrast, no clipped buttons, no overlap, and working media.
- Run `git diff --check`.

## Assumptions

- Recruiter project ordering is explicitly out of discussion for now.
- The standalone `robotics_light_portfolio.css` and `robotics_dark_portfolio.css` are reference artifacts, not files to import directly.
- Existing modified files should be preserved and edited carefully, not reverted.
