# CLAUDE.md — BLUR AI Projects / Pixel

## Project Overview

AI-powered navigation and weather intelligence for J/99 BLUR (SWE-53435), a doublehanded offshore racing campaign. This repo contains tools that integrate with Expedition navigation software to provide competitive advantage through better weather model selection, instrument calibration, performance analysis, and race decision support.

The AI crew member is called **Pixel**. See `pixel/PIXEL-spec.md` for voice, personality, and communication standards.

## Pixel Communication Style

When generating output that Pixel would deliver to the skipper:
- Lead with conclusion, then reasoning
- Use sailing terminology naturally (TWS, TWD, TWA, VMG, BSP)
- Numbers over adjectives: "14-16 kt veering 250→280" not "moderate winds shifting"
- Be confident when model scores are high, explicit about uncertainty when they're not
- Never use filler phrases ("Great question!", "I'd be happy to help")
- Reference race time and positions, not abstract time

## Repo Structure

```
dashboard/          Streamlit app — interactive project overview
scoring/            Weather model scoring engine
pixel/              Pixel spec & core modules
expedition/         Expedition DLL integration
docs/               Documentation & research
```

## Key Technical Details

### Weather Data Sources
- **Open-Meteo API** — Multi-model forecasts (ECMWF, GFS, ICON-EU, Météo-France, KNMI Harmonie). Free, JSON, no GRIB parsing needed. Use for model scoring.
- **SMHI Open Data API** — Swedish coastal observations. Free, Python package available (smhi-open-data). Ground truth for scoring.
- **PredictWind GRIBs** — What's actually loaded in Expedition for routing. GRIB1 format, 50 km resolution.
- **ViVa (Sjöfartsverket)** — Coastal stations, near-real-time. No public API, needs scraping.

### Expedition Integration
- **Expedition-Python DLL** (TTCMarine/Expedition-Python on GitHub)
- `GetExpVar(channel)` / `SetExpVar(channel, value)` for 200+ instrument channels
- Key channels: BSP(1), AWA(2), AWS(3), TWA(4), TWS(5), TWD(6), Lat(48), Lon(49), COG(50), SOG(51), Heel(18)
- Route and waypoint manipulation via the DLL
- Expedition runs on Windows; use mock implementation for development on other platforms

### Boat Data
- **Polar:** Expedition format, v8, doublehanded 160 kg crew weight. File: `J99_blur_2025_v8.txt`
- **Sails:** J1.5, J3.5, C0, A3, S2 (North Sails 3Di RAW + Incidence)
- **Instruments:** B&G system feeding Expedition
- **Log format:** Expedition CSV with numbered channel keys (211 columns)

### Model Scoring Methodology
- Wind Speed Error: RMSE, weight 35%
- Wind Direction Error: Circular RMSE, weight 30%
- Timing Error: Cross-correlation lag, weight 20%
- Trend Accuracy: Correlation of change direction, weight 15%
- Nudge parameters: time offset (hours), speed scaling (multiplier), direction bias (degrees)

### Key SMHI Stations
- **Gotland Runt:** Svenska Högarna, Landsort, Gotska Sandön, Fårösund, Visby, Hoburg, Östergarnsholm, Huvudskär
- **Kattegat/Skagerrak:** Vinga, Nordkoster, Måseskär, Nidingen

## Development Conventions

- Python 3.10+
- Use type hints
- Docstrings on public functions
- Tests in `tests/` subdirectories
- Config via environment variables or YAML (no hardcoded API keys)
- Commit messages: `[module] description` (e.g., `[scoring] add circular RMSE calculation`)

## Current Status

- ✅ Weather Model Scoring Engine — built, needs Claude Code testing with live API
- ⏳ Live GRIB Nudging — next priority
- 📋 13 more projects defined — see `dashboard/app.py` for full list with scores
