# Design QA — Software Editorial

final result: passed

## Visual truth and evidence

- Selected option 1: `C:/Users/ammar/.codex/generated_images/01a187f6-d0c8-70b0-a753-e9d97188b54b/exec-98a751d4-3505-4ed5-b56b-5d4f012e7932.png` (1402 × 1122).
- Local implementation: `http://127.0.0.1:4182/`.
- Evidence directory: `C:/Users/ammar/OneDrive/Desktop/AmmarBots/output/portfolio-redesign-2026-10-29/`.
- Full desktop screenshot: `desktop-full.png` (1384 × 2759), from a 1400 × 1120 CSS viewport. Browser capture omits scrollbar pixels.
- Full-view comparison: `comparison-final.png`, with reference and actual top viewport combined. Source normalized to 1400 × 1120; actual scaled uniformly by width and then cropped to the same top viewport. No independent vertical stretching.
- Focused comparison: `comparison-detail.png` (identity and first featured project); final typography and card detail also inspected at native scale in `desktop-final.png` and `compact-cards-final.png`.
- Phone evidence: `mobile-features.png`, captured at a 390 × 844 CSS viewport.
- State: page top and static selected work, with fresh GitHub data loaded. Additional About navigation, compact cards, and keyboard skip-link states were exercised.

## Findings and comparison history

1. [P2, fixed] Initial name line spacing caused visual overlap. Adjusted display font sizing and line height; final comparison shows separate, readable lines while retaining the oversized condensed name.
2. [P2, fixed] Concurrent Robotics title overflowed its narrow mobile column. Added a mobile font scale and verified no text or page overflow at 320, 390, and 820 CSS pixels.
3. [P2, fixed] Initial featured title hierarchy and row proportions differed from the concept. Increased the first project title, set explicit image slots, and reduced secondary chapter numerals. Final comparison restores three clear editorial rows and balanced image/text columns.

No actionable P0/P1/P2 findings remain.

## Required fidelity surfaces

- **Typography:** locally hosted Anton for the condensed name, project titles, and chapter numerals; Arial/system sans for body and navigation. Intentional equivalent to the unnamed concept fonts. Distinct display/body hierarchy, no clipped text, and no title overflow at tested widths.
- **Spacing:** preserved split introduction, ruled three-column project rows, generous page gutters, and wide right-hand images. Compact cards below are an explicit user-requested extension to the mock. The first project begins about 386 CSS pixels from page top, prioritizing work.
- **Colors:** warm paper #f4f2ed, dark ink #141411, red #ee302c for prominent numbering. Small red labels use a darker #b92320 for readability. No gradients, glass panels, or neon decoration.
- **Images:** three individual 1600 × 600 WebP concept covers, inspected before use. Chess photography, robotic sensor imagery, and handwritten Scheme match the reference's monochrome editorial treatment. Images are conceptual, not fabricated app screenshots; alt text and repository documentation state their role.
- **Copy:** replaced the mock's invented location and placeholder teacher caption with verified personal information. Chess copy accurately describes supervised training and evaluation rather than claiming PUCT/self-play. The current README is the basis for that editorial override.

## Functional verification

- Exactly 3 featured projects, exactly 3 featured images, and 6 smaller project cards.
- All 3 images loaded at full source width; no broken image state.
- All 9 curated projects receive descriptions, languages, canonical links, and dates from the built GitHub snapshot; 3 recent public repository rows render.
- Navigation to About works. Keyboard Tab exposes the skip link; Enter navigates to selected work. Selected work has a programmatic focus target.
- Repository, email, LinkedIn, recent commits, and back-to-top URLs inspected.
- No horizontal page overflow or overflowing headings/body text at 320, 390, 820, and 1400 CSS pixels.
- Browser console: no errors or warnings in the final preview.
- Reduced-motion CSS disables transitions and smooth scrolling. This was checked in source; full assistive-technology and contrast certification are outside this pass.
- Three automated public-data build tests pass, including pagination/filtering, selected export fields, description overrides, curated order, and stopping a build for unavailable public projects.
- JavaScript syntax check and whitespace check pass.

## Implementation checklist

- [x] Recreate the selected composition and color system.
- [x] Install and license the display font locally.
- [x] Generate, inspect, optimize, and place three individual project covers.
- [x] Use compact cards for the remaining projects.
- [x] Preserve hourly GitHub synchronization and static fallback.
- [x] Correct inaccurate generated copy.
- [x] Fix mobile overflow and test core navigation.
- [x] Compare the selected image and implementation in one combined input.

## Follow-up polish

No blocking polish items. Real project screenshots could replace concept covers later if desired, while keeping the same layout. External GitHub descriptions can change text lengths on future hourly refreshes; layouts use wrapping rather than fixed-height text boxes.
