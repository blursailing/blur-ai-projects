# BLUR AI Projects — Changelog

All notable changes to the project portfolio. Updated each session.

Format: date, what changed, and why.

---

## 2026-02-27 — Session 3: Repo & Identity

### Added
- **Pixel** crew member spec — voice, communication style, three operating modes
- Streamlit dashboard (`dashboard/app.py`) with scatter plot, filters, project cards
- GitHub repo structure (scoring/, pixel/, expedition/, docs/)
- `projects.yaml` — single source of truth for all project data
- This changelog

### Changed
- Restructured AI crew from 5 role-based positions to 3-layer pipeline model
  (Foundation → Strategist → Co-Pilot) based on deep Expedition analysis
- Project #15 renamed to "Autonomous Expedition Co-Pilot (Pixel)"
- Project #15 status: idea → in-progress (Pixel spec is first deliverable)

### Scores unchanged
- No re-scoring this session. All edge/complexity values carry from Session 2.

---

## 2026-02-27 — Session 2: Project Portfolio

### Added
- 15 projects defined with edge scores, complexity scores, tech stacks
- Navigator insights from Campbell Field, Will Oxley, Justin Shaffer, Nick White, Stan Honey
- Expedition DLL integration points mapped per project
- Dependency graph between projects
- React dashboard (precursor to Streamlit version)

### Project scoring methodology
- Edge (0–10): How much competitive advantage during a race
- Complexity (0–10): How hard to build and maintain
- Ratio: edge ÷ complexity = bang for buck

---

## 2026-02-26 — Session 1: Foundation

### Added
- Weather model landscape (ECMWF, GFS, ICON, HARMONIE, AROME)
- Model scoring methodology (RMSE, circular RMSE, cross-correlation, trend)
- SMHI/ViVa station mapping for Gotland Runt course
- Nudging concept (time offset, speed scaling, direction bias)
- Race phase timeline (D-7 → D-1 → Race → Post-race)
- System architecture (Claude.ai Projects + Conversations + Claude Code)

### Built
- Weather Model Scoring Engine (Project #1) — Python prototype
- Tested against synthetic data, ready for live API testing in Claude Code

---

## How to update this file

After each working session, add a new entry at the top with:
- Date and session description
- **Added**: New projects or capabilities
- **Changed**: Score adjustments, status changes, re-prioritization
- **Removed**: Anything dropped or merged
- **Rationale**: Why scores changed (important for traceability)

Convention: Claude will propose changelog entries at the end of each session.
You review, adjust, and commit.
