# Documentation & Research

## Key references

### Expedition
- [Expedition Marine](https://www.expeditionmarine.com/) — navigation software
- [Expedition-Python (GitHub)](https://github.com/TTCMarine/Expedition-Python) — Python DLL wrapper
- Expedition.pdf — comprehensive software documentation (not in repo, load into Claude Project)

### Weather data APIs
- [Open-Meteo](https://open-meteo.com/) — free multi-model forecast API
- [Open-Meteo Historical Forecast API](https://open-meteo.com/en/docs/historical-forecast-api) — archived model runs for backtesting
- [SMHI Open Data](https://opendata.smhi.se/) — Swedish observations API
- [smhi-open-data (Python)](https://github.com/LasseRegin/smhi-open-data) — Python package for SMHI
- [ViVa Sjöfartsverket](https://viva.sjofartsverket.se/) — real-time coastal observations

### Navigator best practices
- Model Accuracy workflow (Campbell Field) — score models against observations after each race
- Ensemble divergence analysis (Will Oxley) — routes cluster = commit, routes diverge = hedge
- GRIB nudging (Justin Shaffer) — apply bias corrections before routing
- Polar refinement (Nick White / Expedition) — continuous validation against race data

### Races
- [Gotland Runt](https://gotlandrunt.se/) — 350 NM, late June, ~200 boats
- [KSSS](https://www.ksss.se/) — Royal Swedish Yacht Club (organizing club)

## Project history

| Date | Session | What was built |
|------|---------|---------------|
| 2026-02-26 | Session 1 | Weather model landscape, scoring methodology, system architecture |
| 2026-02-27 | Session 2 | Weather model scoring engine (Python), tested against synthetic data |
| 2026-02-27 | Session 3 | 15 project portfolio with edge/complexity scoring, Pixel spec, Streamlit dashboard, repo structure |
