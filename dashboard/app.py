"""
BLUR AI Projects — Edge vs Complexity
Interactive Streamlit dashboard for navigating the 15 AI crew projects
for J/99 BLUR offshore racing.

Run: streamlit run app.py
"""

import streamlit as st
import plotly.graph_objects as go

# ─── Page config ───
st.set_page_config(
    page_title="BLUR AI Projects",
    page_icon="⛵",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ───
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;700&display=swap');

    .stApp { background-color: #06080f; }
    .main .block-container { padding-top: 2rem; max-width: 1100px; }

    h1, h2, h3 { font-family: 'DM Sans', sans-serif !important; }
    p, li, span, div { font-family: 'DM Sans', sans-serif; }
    code { font-family: 'DM Mono', monospace !important; }

    /* Card styling */
    .project-card {
        background: #0a0e1a;
        border: 1px solid #1a1a2e;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 12px;
        transition: border-color 0.2s;
    }
    .project-card:hover { border-color: #2a2a4e; }
    .project-card.best-practice { border-left: 3px solid #00e5a0; }
    .project-card.radical { border-left: 3px solid #ff6b35; }

    .tag-radical {
        background: rgba(255,107,53,0.1);
        color: #ff6b35;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-family: 'DM Mono', monospace;
    }
    .tag-phase {
        color: #4a6a8a;
        font-size: 12px;
        font-family: 'DM Mono', monospace;
    }

    .metric-label {
        color: #6b7280;
        font-size: 11px;
        font-family: 'DM Mono', monospace;
    }
    .metric-value {
        font-size: 22px;
        font-weight: 800;
        font-family: 'DM Mono', monospace;
    }

    .insight-box {
        background: #0d1220;
        border-left: 2px solid #2a4a6a;
        border-radius: 6px;
        padding: 12px 16px;
        margin-top: 8px;
        font-style: italic;
        color: #8aa0b8;
        font-size: 13px;
        line-height: 1.6;
    }

    .build-sequence {
        background: #0a0e1a;
        border: 1px solid #1a1a2e;
        border-radius: 8px;
        padding: 20px;
        line-height: 1.9;
        font-size: 14px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #080b14;
    }

    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stExpander {
        background: #0a0e1a;
        border: 1px solid #1a1a2e;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)


# ─── Project data ───
PROJECTS = [
    {
        "id": 1,
        "title": "Weather Model Scoring Engine",
        "category": "best-practice",
        "edge": 9.5,
        "complexity": 5,
        "description": "Score GRIB forecasts against SMHI/ViVa observations and Expedition logs. Rank models, detect bias, output calibration recommendations. Model Accuracy approach, automated and continuous.",
        "tech": "Python · Open-Meteo API · SMHI API · Expedition logs",
        "exp_features": "Expedition log parsing · GRIB weather display",
        "insight": 'Campbell Field: "I run Model Accuracy after every distance race to get a feel for which models I should favour."',
        "phase": "✅ Built — ready for Claude Code testing",
    },
    {
        "id": 2,
        "title": "Live GRIB Nudging for Routing",
        "category": "best-practice",
        "edge": 9.0,
        "complexity": 6,
        "description": "Apply scoring engine's bias corrections to GRIBs before routing. Auto-adjust TWS scale, TWD rotation, and time offset in Expedition's routing via the Python DLL.",
        "tech": "Expedition-Python DLL · Python · GRIB manipulation",
        "exp_features": "Optimal routing settings (Wind Time Shift, polar scaling) · SetExpVar() · Ensemble routing",
        "insight": 'Justin Shaffer: "I was able to apply those past forecast trends as optimal routing calibrations in Expedition. The result was a perfectly calibrated optimal route on the best GRIB."',
        "phase": "Next — requires scoring engine output",
    },
    {
        "id": 3,
        "title": "Ensemble Route Divergence Alerting",
        "category": "best-practice",
        "edge": 8.5,
        "complexity": 4,
        "description": "Run Expedition's ensemble routing across all loaded models, then analyze where routes converge (safe) vs diverge (critical). Flag decision points with time windows.",
        "tech": "Expedition-Python DLL · Expedition ensemble routing",
        "exp_features": "Ensemble routing · Reverse isochrones · Sensitivity shading · Multiple optimal routes",
        "insight": "Will Oxley uses ensemble spread as primary decision tool. When routes cluster = commit. When routes diverge = hedge toward the middle.",
        "phase": "D-3 to race day tool",
    },
    {
        "id": 4,
        "title": "Automated Polar Validation & Refinement",
        "category": "best-practice",
        "edge": 8.0,
        "complexity": 6,
        "description": "Parse Expedition race logs, compare actual BSP vs polar target across all TWA/TWS combinations. Identify consistent over/under-performance. Generate polar patch files automatically.",
        "tech": "Python · Expedition logs · Polar parser · Stripchart data",
        "exp_features": "Polar edit · Sail test analysis · Stripchart wand tests · Nav vs Performance polar",
        "insight": 'Nick White (Expedition creator): "Your polars are an extremely valuable input. Garbage in = garbage out." Every top nav team does polar refinement after every race. Most J/99 teams don\'t.',
        "phase": "Off-season project, updates before each race",
    },
    {
        "id": 5,
        "title": "Strategic Sail Change Optimizer",
        "category": "best-practice",
        "edge": 7.5,
        "complexity": 5,
        "description": "Combine routing output (predicted TWA/TWS along the course) with your sail crossover chart to pre-plan every sail change. Calculate exact positions, account for doublehanded change time penalty.",
        "tech": "Python · Expedition routing CSV export · Sailchart data",
        "exp_features": "Sail chart · Optimal route results table · Sail polars",
        "insight": "On a J/99 doublehanded, a bad sail change costs 3-5 minutes. Knowing exactly when to change and pre-staging the right sail is worth more than most tactical decisions.",
        "phase": "Pre-race (D-1) and during race",
    },
    {
        "id": 6,
        "title": "Pre-Race Historical Weather Analysis",
        "category": "best-practice",
        "edge": 7.5,
        "complexity": 3,
        "description": 'For a specific race course and date range, pull historical SMHI data to understand typical wind patterns, sea breeze timing, diurnal shifts. Build a "course weather playbook."',
        "tech": "Python · SMHI historical API · Data visualization",
        "exp_features": "Expedition weather display · Meteograms",
        "insight": "Stan Honey pre-analyzes years of historical data for every major race. The blur.se blog already shows SMHI historical work — this automates it.",
        "phase": "Weeks before race, one-time per course",
    },
    {
        "id": 7,
        "title": "Instrument Calibration Assistant",
        "category": "best-practice",
        "edge": 7.0,
        "complexity": 5,
        "description": "Analyze Expedition logs to detect instrument calibration drift: compare TWD port vs starboard (upwash), BSP vs SOG (speed cal), current set changes tack-to-tack (heading cal).",
        "tech": "Python · Expedition-Python DLL · Expedition logs",
        "exp_features": "Calibration tables (TWA, TWS, BSP, Heading, Leeway) · Stripchart · B&G cal exchange",
        "insight": 'Expedition docs: "If you have inaccurate data, then any calculations and decisions will reflect those errors." Bad cal = bad TWD = bad routing.',
        "phase": "After every sail, continuous improvement",
    },
    {
        "id": 8,
        "title": "Race Debrief Report Generator",
        "category": "best-practice",
        "edge": 6.5,
        "complexity": 4,
        "description": "Auto-generate post-race analysis from Expedition logs: actual vs polar per leg, tactical decisions, model accuracy during race, and competitor analysis from YB/AIS data.",
        "tech": "Python · Expedition logs · Claude AI for narrative",
        "exp_features": "Log replay · Track display · AIS tracking · YB Tracking · Stripchart",
        "insight": "Every Volvo Ocean Race team does structured debriefs. Most club racers learn almost nothing between races because the data stays in a log file nobody opens.",
        "phase": "Post-race (within 24h)",
    },
    {
        "id": 9,
        "title": "Routing Sensitivity Time Budget",
        "category": "best-practice",
        "edge": 8.0,
        "complexity": 4,
        "description": "Use Expedition's reverse isochrones and sensitivity shading to quantify WHERE time is won/lost on the course. Convert to a \"time budget\" per decision point.",
        "tech": "Expedition-Python DLL · Expedition routing",
        "exp_features": "Reverse isochrones · Sensitivity shading · Optimal route Polar% runs (90-110%)",
        "insight": 'Expedition docs: "If forward and reverse isochrones are close together over a small distance, the optimal route is much more critical."',
        "phase": "D-1 planning and during race",
    },
    {
        "id": 10,
        "title": "Fleet Position & Competitor Tracker",
        "category": "best-practice",
        "edge": 6.0,
        "complexity": 5,
        "description": "Ingest YB Tracking and AIS data for competitors. Calculate who's ahead/behind on corrected time (SRS handicap). Detect when competitors are on a different strategic option.",
        "tech": "Python · YB Tracking API · AIS data · Expedition-Python DLL",
        "exp_features": 'YB Tracking · AIS target tracking · Fleet routing · "Ahead of" channel',
        "insight": "In Gotland Runt with 200 boats, knowing where your direct SRS competitors are is crucial for mid-race tactical adjustments.",
        "phase": "Race day, continuous",
    },
    {
        "id": 11,
        "title": "AI Weather Regime Classifier",
        "category": "radical",
        "edge": 9.0,
        "complexity": 8,
        "description": 'Train a classifier on historical Baltic weather to identify the current regime (frontal, gradient, thermal, post-frontal NW) and auto-select model weighting. "In frontal situations, trust ECMWF. In thermal patterns, trust ICON-EU."',
        "tech": "Python · ML (scikit-learn/XGBoost) · SMHI historical · Open-Meteo archive",
        "exp_features": "Ensemble routing weights based on regime",
        "insight": "No sailing team does this yet. Meteorologists know models have regime-dependent skill, but the connection to routing is manual and intuitive. This codifies what the best weather routers do by instinct.",
        "phase": "Off-season R&D, long-term advantage",
    },
    {
        "id": 12,
        "title": "Dynamic Polar Adjustment (Fatigue + Sea State)",
        "category": "radical",
        "edge": 8.5,
        "complexity": 7,
        "description": "Your polar assumes peak performance. But doublehanded at 3 AM in 1.5m swell, you're not hitting 100%. Build a dynamic polar scaling model: time of day, sea state, hours into race, and recent BSP-vs-target ratio.",
        "tech": "Python · Expedition-Python DLL · GRIB wave data · Expedition logs",
        "exp_features": "Nav polar scaling · Polar% runs · Wave corrections · SetExpVar() for live polar %",
        "insight": "Expedition already has Polar% routing (90-110%). The radical part is making it DYNAMIC. No amateur team does this; some Volvo Ocean Race teams estimated crew fatigue manually.",
        "phase": "Race day, automatic background process",
    },
    {
        "id": 13,
        "title": "Probabilistic Routing with Confidence Intervals",
        "category": "radical",
        "edge": 9.0,
        "complexity": 9,
        "description": 'Instead of routing on one model, generate a probability distribution of arrival times via Monte Carlo. Output: "78% chance of arriving 14:00-16:00, but 15% chance of >20:00 if the front stalls."',
        "tech": "Python · Monte Carlo simulation · Expedition routing via DLL · Scoring engine stats",
        "exp_features": "Ensemble routing · Multiple optimal routes · Sensitivity shading",
        "insight": "This is what the ECMWF ensemble (51 members) is designed for, but nobody applies it to individual boat routing. You'd be the first J/99 team doing probabilistic strategy.",
        "phase": "D-2 to race, computationally intensive",
    },
    {
        "id": 14,
        "title": "Real-Time Land Effect Correction Model",
        "category": "radical",
        "edge": 8.0,
        "complexity": 8,
        "description": "The Stockholm archipelago and Gotland's coastline create massive land effects no global model captures. Build a correction layer using historical SMHI station data for wind shadow, acceleration, thermal effects.",
        "tech": "Python · SMHI multi-station analysis · GRIB modification · Spatial interpolation",
        "exp_features": "GRIB weather display · Scale currents (analogous for wind patches)",
        "insight": "The 2019 blur.se blog noted ICON-EU and Météo-France differ by 9-16° in TWD near land — exactly this problem. The archipelago exit and Gotland's southern tip are notorious.",
        "phase": "Course-specific R&D, applied during race",
    },
    {
        "id": 15,
        "title": "Autonomous Expedition Co-Pilot (Pixel)",
        "category": "radical",
        "edge": 9.5,
        "complexity": 10,
        "description": 'A Python process connected to Expedition via DLL that acts as AI crew: monitors all instrument channels, detects wind shifts, triggers re-routing, manages sail change timing, watches competitors. The "always-on navigator" for doublehanded racing.',
        "tech": "Python · Expedition-Python DLL (200+ channels) · Claude API · WebSocket to phone",
        "exp_features": "Full DLL access · Alarms · SetSysBool for custom flags · What-if functionality",
        "insight": "This is the endgame — where all other projects converge. Every individual project becomes a module in this system. No doublehanded team has anything close.",
        "phase": "Long-term vision, built incrementally",
    },
]


# ─── Sidebar ───
with st.sidebar:
    st.markdown("### ⛵ BLUR × Expedition × AI")
    st.caption("J/99 BLUR · SWE-53435 · [blur.se](https://www.blur.se)")
    st.markdown("---")

    category_filter = st.radio(
        "Filter by category",
        ["All (15)", "Best Practice (10)", "Radical (5)"],
        index=0,
    )

    st.markdown("---")

    sort_option = st.radio(
        "Sort by",
        ["Ratio (edge ÷ complexity)", "Competitive Edge", "Easiest first"],
        index=0,
    )

    st.markdown("---")

    min_edge = st.slider("Minimum edge score", 0.0, 10.0, 0.0, 0.5)
    max_complexity = st.slider("Maximum complexity", 1, 10, 10)

    st.markdown("---")
    st.markdown(
        """
        <div style="font-size: 11px; color: #4a5a6a; line-height: 1.6;">
        <strong style="color: #00e5a0;">Edge</strong> = competitive advantage during a race<br>
        <strong style="color: #ff9800;">Complexity</strong> = effort to build<br>
        <strong>Ratio</strong> = edge ÷ complexity (bang for buck)
        </div>
        """,
        unsafe_allow_html=True,
    )


# ─── Filter & sort ───
filtered = PROJECTS.copy()

if "Best Practice" in category_filter:
    filtered = [p for p in filtered if p["category"] == "best-practice"]
elif "Radical" in category_filter:
    filtered = [p for p in filtered if p["category"] == "radical"]

filtered = [p for p in filtered if p["edge"] >= min_edge and p["complexity"] <= max_complexity]

if "Ratio" in sort_option:
    filtered.sort(key=lambda p: p["edge"] / max(p["complexity"], 0.1), reverse=True)
elif "Edge" in sort_option:
    filtered.sort(key=lambda p: p["edge"], reverse=True)
else:
    filtered.sort(key=lambda p: p["complexity"])


# ─── Header ───
st.markdown("# BLUR AI Projects — Edge vs Complexity")
st.markdown(
    "15 projects scored on **:green[competitive edge]** (how much faster you'll be) "
    "vs **:orange[complexity]** (how hard to build). Built for J/99 BLUR doublehanded offshore racing "
    "with Expedition navigation software."
)


# ─── Scatter plot ───
st.markdown("### Scatter: Edge vs Complexity")

fig = go.Figure()

for cat, color, symbol in [
    ("best-practice", "#00e5a0", "circle"),
    ("radical", "#ff6b35", "diamond"),
]:
    cat_projects = [p for p in filtered if p["category"] == cat]
    if not cat_projects:
        continue

    ratios = [p["edge"] / max(p["complexity"], 0.1) for p in cat_projects]

    fig.add_trace(go.Scatter(
        x=[p["complexity"] for p in cat_projects],
        y=[p["edge"] for p in cat_projects],
        mode="markers+text",
        marker=dict(
            size=[r * 12 for r in ratios],
            color=color,
            opacity=0.85,
            line=dict(width=1, color="#1a1a2e"),
            symbol=symbol,
        ),
        text=[f"#{p['id']}" for p in cat_projects],
        textposition="top center",
        textfont=dict(size=10, color="#8a8aa0", family="DM Mono, monospace"),
        customdata=[
            [p["title"], p["edge"], p["complexity"], round(p["edge"] / max(p["complexity"], 0.1), 2)]
            for p in cat_projects
        ],
        hovertemplate=(
            "<b>%{customdata[0]}</b><br>"
            "Edge: %{customdata[1]}<br>"
            "Complexity: %{customdata[2]}<br>"
            "Ratio: %{customdata[3]}×"
            "<extra></extra>"
        ),
        name="Best Practice" if cat == "best-practice" else "Radical",
    ))

# Add "ideal" zone shading — high edge, low complexity
fig.add_shape(
    type="rect", x0=0, y0=7.5, x1=5.5, y1=10,
    fillcolor="rgba(0,229,160,0.04)", line=dict(width=0),
    layer="below",
)
fig.add_annotation(
    x=2.75, y=9.8, text="sweet spot", showarrow=False,
    font=dict(size=10, color="#00e5a040", family="DM Mono"),
)

# Ratio isolines
for ratio in [1.0, 1.5, 2.0]:
    x_vals = [i * 0.5 for i in range(2, 21)]
    y_vals = [x * ratio for x in x_vals]
    fig.add_trace(go.Scatter(
        x=x_vals, y=y_vals,
        mode="lines",
        line=dict(color="#1a2a3a", width=1, dash="dot"),
        showlegend=False,
        hoverinfo="skip",
    ))
    fig.add_annotation(
        x=10.2, y=min(10, 10.2 * ratio),
        text=f"{ratio}×",
        showarrow=False,
        font=dict(size=9, color="#2a3a4a", family="DM Mono"),
    )

fig.update_layout(
    plot_bgcolor="#06080f",
    paper_bgcolor="#06080f",
    font=dict(family="DM Sans, sans-serif", color="#8a8aa0"),
    xaxis=dict(
        title="Complexity →",
        range=[0.5, 11],
        gridcolor="#0f1525",
        zerolinecolor="#0f1525",
        dtick=1,
    ),
    yaxis=dict(
        title="Competitive Edge →",
        range=[5, 10.2],
        gridcolor="#0f1525",
        zerolinecolor="#0f1525",
        dtick=0.5,
    ),
    legend=dict(
        orientation="h", yanchor="bottom", y=1.02,
        xanchor="left", x=0,
        font=dict(size=12),
    ),
    margin=dict(l=50, r=20, t=40, b=50),
    height=480,
)

st.plotly_chart(fig, use_container_width=True)


# ─── Project cards ───
st.markdown(f"### Projects ({len(filtered)} shown)")

for rank, p in enumerate(filtered, 1):
    ratio = p["edge"] / max(p["complexity"], 0.1)
    is_radical = p["category"] == "radical"

    # Ratio color
    if ratio >= 2.0:
        ratio_color = "#00e5a0"
    elif ratio >= 1.5:
        ratio_color = "#00bcd4"
    elif ratio >= 1.0:
        ratio_color = "#ffd740"
    else:
        ratio_color = "#ff9800"

    # Edge color
    if p["edge"] >= 9:
        edge_color = "#00e5a0"
    elif p["edge"] >= 8:
        edge_color = "#00bcd4"
    elif p["edge"] >= 7:
        edge_color = "#7c4dff"
    else:
        edge_color = "#ff9800"

    # Complexity color
    if p["complexity"] >= 8:
        cx_color = "#ff5252"
    elif p["complexity"] >= 6:
        cx_color = "#ff9800"
    elif p["complexity"] >= 4:
        cx_color = "#ffd740"
    else:
        cx_color = "#00e5a0"

    cat_tag = '<span class="tag-radical">radical</span> ' if is_radical else ""
    phase_tag = f'<span class="tag-phase">{p["phase"]}</span>'

    with st.expander(f"**#{rank}** — {p['title']}  ·  ratio **{ratio:.1f}×**"):
        cols = st.columns([1, 1, 1, 3])
        with cols[0]:
            st.markdown(f'<div class="metric-label">Edge</div><div class="metric-value" style="color:{edge_color}">{p["edge"]}</div>', unsafe_allow_html=True)
        with cols[1]:
            st.markdown(f'<div class="metric-label">Complexity</div><div class="metric-value" style="color:{cx_color}">{p["complexity"]}</div>', unsafe_allow_html=True)
        with cols[2]:
            st.markdown(f'<div class="metric-label">Ratio</div><div class="metric-value" style="color:{ratio_color}">{ratio:.1f}×</div>', unsafe_allow_html=True)
        with cols[3]:
            st.markdown(f'{cat_tag}{phase_tag}', unsafe_allow_html=True)
            st.markdown(f'<div style="color:#8a8aa0; font-size:13px; margin-top:4px;">{p["description"]}</div>', unsafe_allow_html=True)

        st.markdown("---")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"**Tech Stack**")
            st.caption(p["tech"])
        with c2:
            st.markdown(f"**Expedition Features**")
            st.caption(p["exp_features"])

        if p.get("insight"):
            st.markdown(f'<div class="insight-box">💡 {p["insight"]}</div>', unsafe_allow_html=True)


# ─── Build sequence ───
st.markdown("---")
st.markdown("### Recommended Build Sequence")
st.markdown(
    """
    <div class="build-sequence">
    <strong style="color:#00e5a0">Now →</strong> #1 Weather Model Scoring Engine (already built, test in Claude Code)<br>
    <strong style="color:#00bcd4">Next →</strong> #2 Live GRIB Nudging (highest edge, uses scoring output)<br>
    <strong style="color:#7c4dff">Then →</strong> #4 Polar Validation + #6 Historical Weather Analysis (off-season prep)<br>
    <strong style="color:#ffd740">Race week →</strong> #3 Ensemble Divergence + #9 Sensitivity Budget + #5 Sail Changes<br>
    <strong style="color:#ff6b35">Long term →</strong> #11 Regime Classifier → #13 Probabilistic Routing → #15 Autonomous Co-Pilot (Pixel)
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")
st.caption("BLUR Weather Intelligence · J/99 SWE-53435 · blur.se · Pixel v1.0")
