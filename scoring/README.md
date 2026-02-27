# Weather Model Scoring Engine

Compares weather model forecasts against actual observations (SMHI stations, ViVa, onboard instruments) to determine which model to trust for routing decisions.

## Status: ✅ Designed, needs Claude Code testing with live APIs

## How it works

1. Pull historical/live forecasts from Open-Meteo (ECMWF, GFS, ICON-EU, Harmonie, etc.)
2. Pull observations from SMHI Open Data API for the same time/location
3. Calculate per-model accuracy scores:
   - Wind speed RMSE (35% weight)
   - Wind direction circular RMSE (30%)
   - Timing lag via cross-correlation (20%)
   - Trend accuracy (15%)
4. Detect systematic bias → generate nudge parameters (time offset, speed scale, direction rotation)
5. Output: ranked model list with confidence scores and recommended nudge values

## Next: move scoring engine code here from Claude Code session
