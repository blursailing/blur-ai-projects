"""
BLUR AI Projects — Edge vs Complexity
Interactive Streamlit dashboard for J/99 BLUR offshore racing.

Data lives in projects.yaml — edit that file, not this one.
Run: streamlit run app.py
"""

import streamlit as st
import plotly.graph_objects as go
import yaml
from pathlib import Path

# ─── Page config ───
st.set_page_config(
    page_title="BLUR AI Projects",
    page_icon="⛵",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Load data ───
@st.cache_data
def load_projects():
    yaml_path = Path(__file__).parent / "projects.yaml"
    with open(yaml_path, "r") as f:
        return yaml.safe_load(f)

PROJECTS = load_projects()

# ─── Status config ───
STATUS_CONFIG = {
    "idea":        {"icon": "💭", "color": "#4a5a6a", "label": "Idea"},
    "planned":     {"icon": "📋", "color": "#7c4dff", "label": "Planned"},
    "in-progress": {"icon": "🔨", "color": "#00bcd4", "label": "In Progress"},
    "testing":     {"icon": "🧪", "color": "#ffd740", "label": "Testing"},
    "complete":    {"icon": "✅", "color": "#00e5a0", "label": "Complete"},
    "on-hold":     {"icon": "⏸️",  "color": "#ff5252", "label": "On Hold"},
}

# ─── Custom CSS ───
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;700&display=swap');

    .stApp { background-color: #06080f; }
    .main .block-container { padding-top: 2rem; max-width: 1100px; }

    h1, h2, h3 { font-family: 'DM Sans', sans-serif !important; }
    p, li, span, div { font-family: 'DM Sans', sans-serif; }
    code { font-family: 'DM Mono', monospace !important; }

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

    .tag {
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-family: 'DM Mono', monospace;
        display: inline-block;
        margin-right: 6px;
    }
    .tag-radical {
        background: rgba(255,107,53,0.1);
        color: #ff6b35;
    }
    .tag-status {
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 11px;
        font-family: 'DM Mono', monospace;
        display: inline-block;
    }
    .tag-phase {
        color: #4a6a8a;
        font-size: 12px;
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

    .dep-tag {
        background: rgba(124,77,255,0.1);
        color: #7c4dff;
        padding: 1px 6px;
        border-radius: 3px;
        font-size: 10px;
        font-family: 'DM Mono', monospace;
        margin-right: 4px;
    }

    .notes-box {
        background: #080b14;
        border: 1px solid #1a1a2e;
        border-radius: 6px;
        padding: 10px 14px;
        margin-top: 8px;
        color: #6b7280;
        font-size: 12px;
        line-height: 1.5;
    }

    .build-sequence {
        background: #0a0e1a;
        border: 1px solid #1a1a2e;
        border-radius: 8px;
        padding: 20px;
        line-height: 1.9;
        font-size: 14px;
    }

    section[data-testid="stSidebar"] {
        background-color: #080b14;
    }

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


# ─── Sidebar ───
with st.sidebar:
    st.markdown("### ⛵ BLUR × Expedition × AI")
    st.caption("J/99 BLUR · SWE-53435 · [blur.se](https://www.blur.se)")
    st.markdown("---")

    category_filter = st.radio(
        "Category",
        ["All (15)", "Best Practice (10)", "Radical (5)"],
        index=0,
    )

    st.markdown("---")

    all_statuses = sorted(set(p.get("status", "planned") for p in PROJECTS))
    status_filter = st.multiselect(
        "Status",
        options=all_statuses,
        default=all_statuses,
        format_func=lambda s: f"{STATUS_CONFIG.get(s, {}).get('icon', '•')} {STATUS_CONFIG.get(s, {}).get('label', s)}",
    )

    st.markdown("---")

    sort_option = st.radio(
        "Sort by",
        ["Ratio (bang for buck)", "Competitive Edge", "Easiest first", "Status"],
        index=0,
    )

    st.markdown("---")

    min_edge = st.slider("Minimum edge score", 0.0, 10.0, 0.0, 0.5)
    max_complexity = st.slider("Maximum complexity", 1, 10, 10)

    st.markdown("---")

    st.markdown(
        """
        <div style="font-size: 11px; color: #4a5a6a; line-height: 1.8;">
        <strong style="color: #00e5a0;">Edge</strong> = competitive advantage<br>
        <strong style="color: #ff9800;">Complexity</strong> = effort to build<br>
        <strong>Ratio</strong> = edge ÷ complexity<br><br>
        <strong>Status:</strong><br>
        💭 Idea · 📋 Planned · 🔨 In Progress<br>
        🧪 Testing · ✅ Complete · ⏸️ On Hold
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.caption("Data: `projects.yaml`")


# ─── Filter & sort ───
filtered = PROJECTS.copy()

if "Best Practice" in category_filter:
    filtered = [p for p in filtered if p["category"] == "best-practice"]
elif "Radical" in category_filter:
    filtered = [p for p in filtered if p["category"] == "radical"]

filtered = [p for p in filtered if p.get("status", "planned") in status_filter]
filtered = [p for p in filtered if p["edge"] >= min_edge and p["complexity"] <= max_complexity]

STATUS_ORDER = {"complete": 0, "testing": 1, "in-progress": 2, "planned": 3, "idea": 4, "on-hold": 5}

if "Ratio" in sort_option:
    filtered.sort(key=lambda p: p["edge"] / max(p["complexity"], 0.1), reverse=True)
elif "Edge" in sort_option:
    filtered.sort(key=lambda p: p["edge"], reverse=True)
elif "Easiest" in sort_option:
    filtered.sort(key=lambda p: p["complexity"])
elif "Status" in sort_option:
    filtered.sort(key=lambda p: STATUS_ORDER.get(p.get("status", "planned"), 99))


# ─── Header ───
st.markdown("# BLUR AI Projects — Edge vs Complexity")

total = len(PROJECTS)
complete = sum(1 for p in PROJECTS if p.get("status") == "complete")
testing = sum(1 for p in PROJECTS if p.get("status") == "testing")
in_progress = sum(1 for p in PROJECTS if p.get("status") == "in-progress")

st.markdown(
    f"**{total}** projects · "
    f"**{complete}** complete · "
    f"**{testing}** testing · "
    f"**{in_progress}** in progress · "
    f"**{total - complete - testing - in_progress}** planned/idea"
)


# ─── Scatter plot ───
st.markdown("### Edge vs Complexity")

fig = go.Figure()

for cat, color, symbol in [
    ("best-practice", "#00e5a0", "circle"),
    ("radical", "#ff6b35", "diamond"),
]:
    cat_projects = [p for p in filtered if p["category"] == cat]
    if not cat_projects:
        continue

    ratios = [p["edge"] / max(p["complexity"], 0.1) for p in cat_projects]
    statuses = [p.get("status", "planned") for p in cat_projects]
    opacities = [1.0 if s in ("complete", "testing", "in-progress") else 0.6 for s in statuses]

    fig.add_trace(go.Scatter(
        x=[p["complexity"] for p in cat_projects],
        y=[p["edge"] for p in cat_projects],
        mode="markers+text",
        marker=dict(
            size=[r * 12 for r in ratios],
            color=color,
            opacity=opacities,
            line=dict(width=1, color="#1a1a2e"),
            symbol=symbol,
        ),
        text=[f"#{p['id']}" for p in cat_projects],
        textposition="top center",
        textfont=dict(size=10, color="#8a8aa0", family="DM Mono, monospace"),
        customdata=[
            [
                p["title"],
                p["edge"],
                p["complexity"],
                round(p["edge"] / max(p["complexity"], 0.1), 2),
                STATUS_CONFIG.get(p.get("status", "planned"), {}).get("label", "Planned"),
            ]
            for p in cat_projects
        ],
        hovertemplate=(
            "<b>%{customdata[0]}</b><br>"
            "Edge: %{customdata[1]} · Complexity: %{customdata[2]}<br>"
            "Ratio: %{customdata[3]}× · Status: %{customdata[4]}"
            "<extra></extra>"
        ),
        name="Best Practice" if cat == "best-practice" else "Radical",
    ))

fig.add_shape(
    type="rect", x0=0, y0=7.5, x1=5.5, y1=10,
    fillcolor="rgba(0,229,160,0.04)", line=dict(width=0),
    layer="below",
)
fig.add_annotation(
    x=2.75, y=9.8, text="sweet spot", showarrow=False,
    font=dict(size=10, color="rgba(0,229,160,0.25)", family="DM Mono"),
)

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

title_by_id = {p["id"]: p["title"] for p in PROJECTS}

for rank, p in enumerate(filtered, 1):
    ratio = p["edge"] / max(p["complexity"], 0.1)
    is_radical = p["category"] == "radical"
    status = p.get("status", "planned")
    status_cfg = STATUS_CONFIG.get(status, STATUS_CONFIG["planned"])

    ratio_color = "#00e5a0" if ratio >= 2.0 else "#00bcd4" if ratio >= 1.5 else "#ffd740" if ratio >= 1.0 else "#ff9800"
    edge_color = "#00e5a0" if p["edge"] >= 9 else "#00bcd4" if p["edge"] >= 8 else "#7c4dff" if p["edge"] >= 7 else "#ff9800"
    cx_color = "#ff5252" if p["complexity"] >= 8 else "#ff9800" if p["complexity"] >= 6 else "#ffd740" if p["complexity"] >= 4 else "#00e5a0"

    status_icon = status_cfg["icon"]
    expander_label = f"**#{p['id']}** {p['title']}  ·  {ratio:.1f}× {status_icon}"

    with st.expander(expander_label):
        cols = st.columns([1, 1, 1, 3])
        with cols[0]:
            st.markdown(f'<div class="metric-label">Edge</div><div class="metric-value" style="color:{edge_color}">{p["edge"]}</div>', unsafe_allow_html=True)
        with cols[1]:
            st.markdown(f'<div class="metric-label">Complexity</div><div class="metric-value" style="color:{cx_color}">{p["complexity"]}</div>', unsafe_allow_html=True)
        with cols[2]:
            st.markdown(f'<div class="metric-label">Ratio</div><div class="metric-value" style="color:{ratio_color}">{ratio:.1f}×</div>', unsafe_allow_html=True)
        with cols[3]:
            tags_html = ""
            if is_radical:
                tags_html += '<span class="tag tag-radical">radical</span>'
            tags_html += f'<span class="tag-status" style="background:{status_cfg["color"]}22; color:{status_cfg["color"]}">{status_cfg["icon"]} {status_cfg["label"]}</span>'
            st.markdown(tags_html, unsafe_allow_html=True)
            st.markdown(f'<span class="tag-phase">{p.get("phase", "")}</span>', unsafe_allow_html=True)
            st.markdown(f'<div style="color:#8a8aa0; font-size:13px; margin-top:4px;">{p["description"]}</div>', unsafe_allow_html=True)

        st.markdown("---")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Tech Stack**")
            st.caption(p.get("tech", ""))
        with c2:
            st.markdown("**Expedition Features**")
            st.caption(p.get("exp_features", ""))

        deps = p.get("depends_on", [])
        if deps:
            deps_html = "<strong>Depends on:</strong> "
            for dep_id in deps:
                dep_title = title_by_id.get(dep_id, f"#{dep_id}")
                deps_html += f'<span class="dep-tag">#{dep_id} {dep_title}</span>'
            st.markdown(deps_html, unsafe_allow_html=True)

        if p.get("insight"):
            st.markdown(f'<div class="insight-box">💡 {p["insight"]}</div>', unsafe_allow_html=True)

        if p.get("notes"):
            st.markdown(f'<div class="notes-box">📝 {p["notes"]}</div>', unsafe_allow_html=True)

        last_updated = p.get("last_updated", "")
        if last_updated:
            st.caption(f"Last updated: {last_updated}")


# ─── Build sequence ───
st.markdown("---")
st.markdown("### Recommended Build Sequence")
st.markdown(
    """
    <div class="build-sequence">
    <strong style="color:#00e5a0">Now →</strong> #1 Weather Model Scoring Engine (testing)<br>
    <strong style="color:#00bcd4">Next →</strong> #2 Live GRIB Nudging (highest edge, uses scoring output)<br>
    <strong style="color:#7c4dff">Then →</strong> #4 Polar Validation + #6 Historical Weather Analysis (off-season prep)<br>
    <strong style="color:#ffd740">Race week →</strong> #3 Ensemble Divergence + #9 Sensitivity Budget + #5 Sail Changes<br>
    <strong style="color:#ff6b35">Long term →</strong> #11 Regime Classifier → #13 Probabilistic Routing → #15 Pixel
    </div>
    """,
    unsafe_allow_html=True,
)

# ─── Dependency map ───
st.markdown("---")
st.markdown("### Dependency Map")

dep_projects = [p for p in PROJECTS if p.get("depends_on")]
if dep_projects:
    for p in dep_projects:
        deps = p.get("depends_on", [])
        dep_names = [f"#{d} {title_by_id.get(d, '?')}" for d in deps]
        st.caption(f"#{p['id']} {p['title']} ← depends on {', '.join(dep_names)}")

# ─── Footer ───
st.markdown("---")
st.caption("BLUR Weather Intelligence · Pixel v1.0 · J/99 SWE-53435 · [blur.se](https://www.blur.se) · Data: `projects.yaml`")
