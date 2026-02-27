# BLUR AI Projects — Pixel

AI-powered navigation, weather intelligence, and performance analysis for **J/99 BLUR** (SWE-53435), a doublehanded offshore racing campaign based in Stockholm.

**Pixel** is BLUR's AI third crew member — a navigator who never sleeps, never guesses, and never wastes your time.

→ [blur.se](https://www.blur.se)

---

## What is this?

A collection of 15 projects that integrate AI with [Expedition](https://www.expeditionmarine.com/) navigation software to gain competitive advantage in offshore races like Gotland Runt (350 NM, ~200 boats), Skagen Race, and Fastnet Race.

The projects range from proven best practices (weather model scoring, polar validation) to radical experiments (AI weather regime classification, probabilistic routing, fatigue-adjusted polars). All are designed for a doublehanded J/99 with limited crew bandwidth and maximum need for smart automation.

## Repo structure

```
blur-ai-projects/
├── dashboard/          Streamlit app — interactive project overview
├── scoring/            Weather model scoring engine
├── pixel/              Pixel crew member spec & core modules
├── expedition/         Expedition DLL integration
├── docs/               Project documentation & research
└── CLAUDE.md           Context file for Claude Code sessions
```

## Quick start — Dashboard

```bash
cd dashboard
pip install -r requirements.txt
streamlit run app.py
```

Or view it live: *(add Streamlit Cloud URL after deployment)*

## Technology

- **Navigation software:** Expedition (Windows) with Python DLL integration
- **Weather data:** Open-Meteo API, SMHI Open Data, PredictWind GRIBs
- **Observations:** SMHI coastal stations, Sjöfartsverket ViVa network
- **Boat data:** B&G instruments → Expedition → Python via ExpDLL
- **AI/ML:** Python (scikit-learn, XGBoost for weather regime classification)
- **Development:** Claude Code for AI-assisted development

## Project ranking (by bang-for-buck)

| # | Project | Edge | Complexity | Ratio |
|---|---------|------|-----------|-------|
| 6 | Historical Weather Analysis | 7.5 | 3 | 2.5× |
| 3 | Ensemble Route Divergence | 8.5 | 4 | 2.1× |
| 9 | Routing Sensitivity Budget | 8.0 | 4 | 2.0× |
| 1 | Weather Model Scoring ✅ | 9.5 | 5 | 1.9× |
| 8 | Race Debrief Generator | 6.5 | 4 | 1.6× |
| 2 | Live GRIB Nudging | 9.0 | 6 | 1.5× |
| 5 | Sail Change Optimizer | 7.5 | 5 | 1.5× |
| 7 | Instrument Calibration | 7.0 | 5 | 1.4× |
| 4 | Polar Validation | 8.0 | 6 | 1.3× |
| 10 | Fleet Tracker | 6.0 | 5 | 1.2× |
| 12 | Dynamic Polar (Fatigue) | 8.5 | 7 | 1.2× |
| 11 | Weather Regime Classifier | 9.0 | 8 | 1.1× |
| 13 | Probabilistic Routing | 9.0 | 9 | 1.0× |
| 14 | Land Effect Correction | 8.0 | 8 | 1.0× |
| 15 | Autonomous Co-Pilot (Pixel) | 9.5 | 10 | 0.95× |

## License

This project is shared openly for the sailing community. Use it, learn from it, improve it. Attribution appreciated.

## Contact

→ [blur.se](https://www.blur.se)
