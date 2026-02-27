# BLUR AI Projects — Dashboard

Interactive Streamlit app for navigating the 15 AI crew projects.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Cloud

1. On [share.streamlit.io](https://share.streamlit.io), connect the GitHub repo
2. Set the main file path to `dashboard/app.py`
3. Done — public URL in ~2 minutes

## Features

- Plotly scatter plot (edge vs complexity, ratio isolines, hover details)
- Sidebar filters (category, sort order, edge/complexity thresholds)
- Expandable project cards with tech stack, Expedition features, navigator insights
- Recommended build sequence
