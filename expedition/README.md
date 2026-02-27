# Expedition Integration

Python interface to Expedition navigation software via the ExpDLL.

## Status: 📋 Planned

## Dependencies

- [Expedition-Python](https://github.com/TTCMarine/Expedition-Python) — Python wrapper for ExpDLL.dll
- Expedition must be running on the same Windows machine

## Key capabilities

- **Read** all 200+ instrument channels (BSP, TWS, TWD, TWA, AWA, Lat, Lon, etc.)
- **Write** corrected values via SetExpVar (nudged wind data, adjusted polar %)
- **Route manipulation** — read/write waypoints, trigger re-routing
- **System variables** — access routing results, laylines, mark data

## Integration points with other modules

| Module | Reads from Expedition | Writes to Expedition |
|--------|----------------------|---------------------|
| Scoring | Log files (post-race) | — |
| Nudging | Current routing settings | Nudged GRIB params, Wind Time Shift |
| Polar validation | Log files | Updated polar tables |
| Sail optimizer | Routing results table | — |
| Co-Pilot (Pixel) | All channels (live) | Alerts, re-routing triggers |
