
import streamlit as st
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"

COMPETITORS = ["Salesforce", "HubSpot", "Freshworks", "All Competitors"]

REPORTS = {
    "Scout Report": "scout_report.md",
    "Competitor Analysis": "synthesis_report.md",
    "Strategy Brief": "strategy_report.md",
    "Search Evidence": "search_evidence.md",
}

FOLDERS = {
    "Salesforce": "salesforce",
    "HubSpot": "hubspot",
    "Freshworks": "freshworks",
}

st.set_page_config(
    page_title="Market Intelligence | AI Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #f5f7fb;
    }

    [data-testid="stSidebar"] {
        background-color: #101827;
    }

    [data-testid="stSidebar"] * {
        color: #e5eaf3;
    }

    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
        background-color: #1e293b;
    }

    .hero {
        background: linear-gradient(120deg, #172554, #1d4ed8);
        padding: 28px 30px;
        border-radius: 18px;
        color: white;
        margin-bottom: 22px;
    }

    .hero h1 {
        color: white;
        font-size: 30px;
        margin-bottom: 8px;
    }

    .hero p {
        color: #dbeafe;
        margin-bottom: 0;
        font-size: 15px;
    }

    .section-label {
        color: #64748b;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .info-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 17px;
        min-height: 112px;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.035);
    }

    .info-card h3 {
        color: #64748b;
        font-size: 13px;
        font-weight: 600;
        margin: 0 0 10px 0;
    }

    .info-card p {
        color: #0f172a;
        font-size: 21px;
        font-weight: 700;
        margin: 0;
    }

    .agent-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 15px;
        min-height: 105px;
    }

    .agent-title {
        font-weight: 700;
        color: #0f172a;
        font-size: 15px;
    }

    .agent-description {
        color: #64748b;
        font-size: 12px;
        margin-top: 6px;
    }

    div.stButton > button[kind="primary"] {
        background: #2563eb;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        min-height: 46px;
    }

    div.stButton > button[kind="primary"]:hover {
        background: #1d4ed8;
        border: none;
    }

    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 12px;
        padding: 20px 0 5px 0;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------
def get_report_dir(competitor):
    if competitor == "All Competitors":
        return OUTPUT_DIR

    return OUTPUT_DIR / "comparisons" / FOLDERS[competitor]


def read_report(path):
    if path.exists():
        return path.read_text(encoding="utf-8")
    return None


def report_exists(competitor):
    folder = get_report_dir(competitor)
    return {
        title: (folder / filename).exists()
        for title, filename in REPORTS.items()
    }


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.markdown("## 📊 MarketIntel AI")
    st.caption("Competitive Intelligence Platform")
    st.divider()

    st.markdown("### Research Settings")

    focal_company = st.selectbox(
        "Focal Company",
        ["Zoho CRM"],
        index=0,
        disabled=True,
    )

    competitor = st.selectbox(
        "Compare Against",
        COMPETITORS,
        index=0,
    )

    region = st.selectbox(
        "Research Region",
        ["Global"],
        index=0,
    )

    period = st.selectbox(
        "Research Period",
        ["2026"],
        index=0,
    )

    st.divider()

    st.markdown("### Analysis Workflow")
    st.markdown(
        "🔎 **Scout**  \n"
        "Collects market evidence\n\n"
        "📋 **Synthesis**  \n"
        "Compares competitor findings\n\n"
        "💡 **Strategy**  \n"
        "Creates strategic recommendations"
    )

    st.divider()

    run_button = st.button(
        "▶  Run Analysis",
        type="primary",
        use_container_width=True,
    )

    st.caption("Powered by CrewAI · Ollama · Python")


# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>Competitive Intelligence Dashboard</h1>
    <p>
        AI-powered market scouting, competitor comparison
        and strategic insights for CRM software.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<div class="section-label">Research Overview · {period}</div>',
    unsafe_allow_html=True,
)

# --------------------------------------------------
# OVERVIEW CARDS
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>Focal Company</h3>
        <p>Zoho CRM</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    competitor_count = 3 if competitor == "All Competitors" else 1
    st.markdown(f"""
    <div class="info-card">
        <h3>Competitors Selected</h3>
        <p>{competitor_count}</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>Research Region</h3>
        <p>Global</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="info-card">
        <h3>AI Agents</h3>
        <p>3 Agents</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# --------------------------------------------------
# SELECTED COMPARISON
# --------------------------------------------------
st.markdown("### 🎯 Selected Comparison")

if competitor == "All Competitors":
    st.info(
        "The workflow will analyze Zoho CRM against Salesforce, "
        "HubSpot and Freshworks."
    )
else:
    st.info(f"Your selected analysis is **Zoho CRM vs {competitor}**.")

# --------------------------------------------------
# EXECUTION
# --------------------------------------------------
if run_button:
    st.warning(
        "The full workflow can use significant memory. "
        "Avoid running it if your laptop is overheating."
    )

    command = [
        sys.executable,
        "main.py",
        "--competitor",
        competitor,
    ]

    try:
        with st.spinner(
            f"Running the research and AI agents for {competitor}..."
        ):
            result = subprocess.run(
                command,
                cwd=BASE_DIR,
                capture_output=True,
                text=True,
                timeout=1200,
            )

        st.session_state["last_competitor"] = competitor
        st.session_state["last_run_time"] = datetime.now().strftime(
            "%d %b %Y, %I:%M %p"
        )
        st.session_state["run_output"] = result.stdout or ""
        st.session_state["run_errors"] = result.stderr or ""
        st.session_state["run_success"] = result.returncode == 0

    except subprocess.TimeoutExpired:
        st.session_state["last_competitor"] = competitor
        st.session_state["run_success"] = False
        st.session_state["run_output"] = ""
        st.session_state["run_errors"] = (
            "The analysis exceeded the 20-minute timeout."
        )

    except Exception as error:
        st.session_state["last_competitor"] = competitor
        st.session_state["run_success"] = False
        st.session_state["run_output"] = ""
        st.session_state["run_errors"] = str(error)

# --------------------------------------------------
# EXECUTION STATUS
# --------------------------------------------------
st.markdown("### ⚙️ Agent Execution Status")

last_competitor = st.session_state.get("last_competitor")
last_success = st.session_state.get("run_success", False)
same_selection = last_competitor == competitor

status = report_exists(competitor)

if same_selection and last_success:
    status_text = "Completed this session"
    status_icon = "🟢"
elif any(status.values()):
    status_text = "Existing reports available"
    status_icon = "🟡"
else:
    status_text = "Not yet executed"
    status_icon = "⚪"

agent_cols = st.columns(3)

agents = [
    ("🔎 Scout Agent", "Market research and evidence"),
    ("📋 Synthesis Agent", "Competitor comparison"),
    ("💡 Strategy Agent", "SWOT and GTM options"),
]

for index, (name, description) in enumerate(agents):
    with agent_cols[index]:
        st.markdown(f"""
        <div class="agent-card">
            <div class="agent-title">{name}</div>
            <div class="agent-description">{description}</div>
            <div style="margin-top:12px;font-size:12px;">
                {status_icon} {status_text}
            </div>
        </div>
        """, unsafe_allow_html=True)

if same_selection and st.session_state.get("last_run_time"):
    st.caption(f"Last run: {st.session_state['last_run_time']}")

if same_selection and not last_success:
    st.error("The latest analysis did not complete successfully.")

    with st.expander("View execution logs"):
        st.code(
            st.session_state.get("run_output", "")[-15000:],
            language="text",
        )
        if st.session_state.get("run_errors"):
            st.code(
                st.session_state["run_errors"][-10000:],
                language="text",
            )

elif same_selection and last_success:
    st.success("The workflow completed successfully.")

    with st.expander("View execution logs"):
        st.code(
            st.session_state.get("run_output", "")[-15000:],
            language="text",
        )
        if st.session_state.get("run_errors"):
            st.code(
                st.session_state["run_errors"][-10000:],
                language="text",
            )

st.divider()

# --------------------------------------------------
# REPORTS
# --------------------------------------------------
st.markdown("### 📑 Intelligence Reports")

report_dir = get_report_dir(competitor)

tabs = st.tabs([
    "🔎 Scout",
    "📋 Comparison",
    "💡 Strategy",
    "📚 Evidence",
])

report_keys = list(REPORTS.keys())

for tab, report_key in zip(tabs, report_keys):
    with tab:
        filename = REPORTS[report_key]
        path = report_dir / filename
        content = read_report(path)

        if content:
            st.markdown(f"#### {report_key}")
            st.caption(f"Source file: {filename}")
            st.download_button(
                "⬇ Download Report",
                data=content,
                file_name=filename,
                mime="text/markdown",
                key=f"download_{competitor}_{filename}",
            )
            st.divider()
            st.markdown(content)
        else:
            st.info(
                "No report is available for this selection yet. "
                "Select a competitor and run the analysis."
            )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<div class="footer">
    B2B Competitive Intelligence · Built with Streamlit and CrewAI
</div>
""", unsafe_allow_html=True)
