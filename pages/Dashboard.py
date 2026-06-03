import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="AI Enterprise Change Intelligence Platform",
    layout="wide"
)

# ---------------- LOGIN CHECK ----------------

if not st.session_state.get(
    "logged_in",
    False
):
    st.switch_page("pages/Login.py")
    st.stop()

# ---------------- IMPORTS ----------------

from backend.pdf_generator import generate_pdf

from agents import (
    impact_agent,
    risk_agent,
    training_agent,
    scoring_agent
)

from backend.llm_client import call_llm
from backend.risk_engine import compute_risk
from backend.rag_store import add_to_memory, search_memory
from backend.graph_engine import generate_dependency_graph

st.markdown("""
<style>

/* ---------------- HIDE SIDEBAR ---------------- */

[data-testid="stSidebar"]{
    display:none;
}

[data-testid="collapsedControl"]{
    display:none;
}

section[data-testid="stSidebarNav"]{
    display:none;
}

/* ---------------- PAGE ---------------- */

.stApp{
    background:#F8FAFC;
}

/* ---------------- HEADER ---------------- */

.main-title{
    font-size:42px;
    font-weight:800;
    color:#111827 !important;
    margin-bottom:5px;
}

.sub-title{
    font-size:18px;
    color:#64748B !important;
}

/* Normal text only */

.stMarkdown p,
.stMarkdown li,
.stMarkdown ul,
.stMarkdown ol,
label{
    color:#111827 !important;
}

h1,h2,h3,h4,h5,h6{
    color:#111827 !important;
}

/* ---------------- BUTTONS ---------------- */

.stButton > button{
    background:#0F172A !important;
    color:white !important;
    border:none !important;
    border-radius:12px !important;
    height:50px !important;
    font-weight:600 !important;
}

.stButton > button *{
    color:white !important;
}

.stButton > button:hover{
    background:#1E293B !important;
}

.stButton > button:hover *{
    color:white !important;
}

/* ---------------- DOWNLOAD BUTTON ---------------- */

.stDownloadButton > button{
    background:#0F172A !important;
    color:white !important;
    border:none !important;
    border-radius:12px !important;
    height:50px !important;
    font-weight:600 !important;
}

.stDownloadButton > button *{
    color:white !important;
}

/* ---------------- INPUT BOX ---------------- */

.stTextInput input{
    background:#1E1E2F !important;
    color:white !important;
}

.stTextInput input::placeholder{
    color:#CBD5E1 !important;
}

/* ---------------- TEXT AREA ---------------- */

.stTextArea textarea{
    background:#1E1E2F !important;
    color:white !important;
}

.stTextArea textarea::placeholder{
    color:#CBD5E1 !important;
}

/* ---------------- SELECT BOX ---------------- */

div[data-baseweb="select"]{
    background:#1E1E2F !important;
    border-radius:12px !important;
}

div[data-baseweb="select"] *{
    color:white !important;
}

/* Dropdown menu */

div[role="listbox"]{
    background:#1E1E2F !important;
}

div[role="option"]{
    background:#1E1E2F !important;
    color:white !important;
}

div[role="option"] *{
    color:white !important;
}

/* ---------------- METRIC CARDS ---------------- */

[data-testid="metric-container"]{
    background:white !important;
    border:1px solid #E5E7EB !important;
    border-radius:18px !important;
    padding:20px !important;
    box-shadow:0px 6px 20px rgba(0,0,0,0.05);
}

[data-testid="stMetricLabel"]{
    color:#64748B !important;
}

[data-testid="stMetricValue"]{
    color:#111827 !important;
    font-weight:700 !important;
}

/* ---------------- TABS ---------------- */

.stTabs [data-baseweb="tab"]{
    color:#111827 !important;
    font-weight:700 !important;
}

/* ---------------- JSON VIEWER ---------------- */

[data-testid="stJson"]{
    background:#0F172A !important;
    border-radius:15px !important;
}

[data-testid="stJson"] *{
    color:white !important;
}

/* ---------------- CODE BLOCK ---------------- */

pre{
    background:#0F172A !important;
    color:white !important;
    border-radius:15px !important;
}

code{
    color:white !important;
}

/* ---------------- ALERTS ---------------- */

[data-testid="stAlert"]{
    border-radius:12px !important;
}
            [data-testid="stJson"]{
    background:#0F172A !important;
}

[data-testid="stJson"] *,
[data-testid="stJson"] span,
[data-testid="stJson"] div{
    color:white !important;
}

            .stDownloadButton button{
    color:white !important;
}

.stDownloadButton button *{
    color:white !important;
}
/* WARNING */

div[data-baseweb="notification"]{
    color:#111827 !important;
}

div[data-baseweb="notification"] *{
    color:#111827 !important;
}

/* SUCCESS */

div[data-baseweb="notification"][kind="positive"] *{
    color:#111827 !important;
}

/* ERROR */

div[data-baseweb="notification"][kind="negative"] *{
    color:#111827 !important;
}

/* STREAMLIT ALERTS */

[data-testid="stAlert"]{
    color:#111827 !important;
}

[data-testid="stAlert"] *{
    color:#111827 !important;
}       
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(f"""
<div style="
background:white;
padding:25px;
border-radius:20px;
border:1px solid #E5E7EB;
box-shadow:0px 6px 20px rgba(0,0,0,0.05);
margin-bottom:20px;
">

<h1 style="
margin:0;
color:#111827;
font-size:42px;
font-weight:800;
">
🏢 Enterprise Change Intelligence Platform
</h1>

<p style="
margin-top:10px;
color:#64748B;
font-size:18px;
">
Multi-Agent AI • Risk Analysis • Dependency Mapping • Enterprise Reporting
</p>

<div style="
margin-top:20px;
padding:12px;
background:#F8FAFC;
border-radius:12px;
border:1px solid #E5E7EB;
font-size:16px;
font-weight:600;
color:#111827;
">
👋 Welcome, {st.session_state.user}
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- LOGOUT ----------------

col1, col2, col3 = st.columns([8,1,1])

with col3:

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.switch_page("pages/Login.py")

# ---------------- INPUT SECTION ----------------

samples = [
    "Migrate monolith to microservices",
    "Move system to AWS cloud",
    "Adopt Kubernetes enterprise-wide",
    "Replace legacy CRM with Salesforce",
    "Implement Zero Trust Security Architecture",
    "Changing UI colours"
]

st.markdown("### 📝 Enterprise Change Analysis")

product_url = st.text_input(
    "🌐 Product / Company Website URL",
    placeholder="https://www.company.com"
)

product_details = st.text_area(
    "📋 Additional Product Details (Optional)",
    placeholder="""
Frontend: React
Backend: Node.js
Database: MySQL
Modules: Payment, Inventory, Notifications
""",
    height=120
)

choice = st.selectbox(
    "Choose Sample Change Request",
    ["Custom"] + samples
)

change = st.text_area(
    "🔄 Proposed Change",
    value="" if choice == "Custom" else choice,
    height=150
)
# ---------------- ANALYZE ----------------

if st.button(
    "🚀 Analyze Change",
    use_container_width=True
):

    if not product_url.strip():

        st.warning(
            "Please enter a Product URL."
        )

        st.stop()

    if not change.strip():

        st.warning(
            "Please enter a proposed change."
        )

        st.stop()

    # LOADING STARTS HERE (outside the above if)

    progress = st.progress(0)

    status = st.empty()

    status.info("🔍 Searching Similar Changes...")
    progress.progress(10)

    memory_context = search_memory(change)

    context_block = "\n".join(memory_context)

    full_input = f"""
    Previous Similar Changes:
    {context_block}

    Product Website:
    {product_url}

    Additional Product Details:
    {product_details}

    Proposed Change:
    {change}

    Analyze:

    1. Business Impact
    2. Technical Impact
    3. Risks
    4. Dependency Analysis
    5. Training Requirements
    6. Executive Recommendation
    """

    status.info("📊 Impact Agent Running...")
    progress.progress(30)

    impact = call_llm(
        impact_agent(full_input)
    )

    status.success("✅ Impact Agent Completed")

    status.info("⚠️ Risk Agent Running...")
    progress.progress(50)

    risk = call_llm(
        risk_agent(full_input)
    )

    status.success("✅ Risk Agent Completed")

    status.info("🎓 Training Agent Running...")
    progress.progress(70)

    training = call_llm(
        training_agent(full_input)
    )

    status.success("✅ Training Agent Completed")

    status.info("🧠 Scoring Agent Running...")
    progress.progress(85)

    score_raw = call_llm(
        scoring_agent(full_input)
    )

    risk_data = compute_risk(score_raw)

    status.success("✅ Scoring Agent Completed")

    status.info("🔗 Building Dependency Graph...")
    progress.progress(95)

    graph_data = generate_dependency_graph(change)

    progress.progress(100)

    status.success("🎉 Analysis Completed Successfully")

    add_to_memory(change)

    progress.empty()
    status.empty()

    

    st.divider()

    st.markdown(f"""
    <div style="
    background:white;
    padding:20px;
    border-radius:18px;
    border:1px solid #E5E7EB;
    box-shadow:0px 6px 20px rgba(0,0,0,0.05);
    margin-bottom:20px;
    ">

    <h3 style="color:#111827;">
    📋 Executive Summary
    </h3>

    <p style="color:#111827;">
    <strong>Product:</strong> {product_url}<br>
    <strong>Risk Level:</strong> {risk_data["risk_level"]}<br>

    <strong>Risk Score:</strong> {risk_data["risk_score"]}/100<br>

    <strong>Systems Impacted:</strong> {len(graph_data.get("nodes", []))}<br>

    <strong>Agents Used:</strong> 4<br>

    <strong>Recommendation:</strong>
    {"Executive Approval Recommended" if risk_data["risk_level"]=="High" else "Proceed With Review"}
    </p>

    </div>
    """, unsafe_allow_html=True)
    # ---------------- METRICS ----------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📈 Risk Score",
            f"{risk_data['risk_score']}/100"
        )

    with col2:

        st.metric(
            "🔗 Systems Impacted",
            len(
                graph_data.get(
                    "nodes",
                    []
                )
            )
        )

    with col3:

        st.metric(
            "🤖 Agents Active",
            "4"
        )

    # ---------------- RISK LEVEL ----------------

    if risk_data["risk_level"] == "High":

        st.error(
            "🚨 High Risk - Executive Approval Recommended"
        )

    elif risk_data["risk_level"] == "Medium":

        st.warning(
            "⚠️ Medium Risk - Additional Review Required"
        )

    else:

        st.success(
            "✅ Low Risk"
        )

    st.progress(
        risk_data["risk_score"] / 100
    )

    st.divider()

    # ---------------- TABS ----------------

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Impact",
        "⚠️ Risk",
        "🎓 Training",
        "🔗 Dependencies",
        "🧠 Raw Data"
    ])

    # ---------------- IMPACT ----------------

    with tab1:

        st.subheader(
            "Business & Technical Impact"
        )

        st.write(
            impact
        )

    # ---------------- RISK ----------------

    with tab2:

        st.subheader(
            "Risk Assessment"
        )

        st.write(
            risk
        )

    # ---------------- TRAINING ----------------

    with tab3:

        st.subheader(
            "Training Recommendations"
        )

        st.write(
            training
        )

    # ---------------- DEPENDENCY GRAPH ----------------

    with tab4:

        st.subheader(
            "AI Generated Dependency Graph"
        )

        st.write(
            "### Systems"
        )

        for node in graph_data.get(
            "nodes",
            []
        ):

            st.write(
                f"• {node}"
            )

        st.write(
            "### Relationships"
        )

        relationships = graph_data.get(
            "relationships",
            []
        )

        if relationships:

            G = nx.DiGraph()

            # Add all edges first
            for rel in relationships:

                if len(rel) >= 2:

                    G.add_edge(rel[0], rel[1])

            # Draw graph only once
            fig = plt.figure(figsize=(12,7))

            pos = nx.spring_layout(
                G,
                k=2,
                iterations=100,
                seed=42
            )

            nx.draw_networkx_nodes(
                G,
                pos,
                node_size=5000
            )

            nx.draw_networkx_edges(
                G,
                pos,
                arrows=True,
                arrowsize=20
            )

            nx.draw_networkx_labels(
                G,
                pos,
                font_size=11,
                font_weight="bold"
            )

            plt.axis("off")

            st.pyplot(fig)

            st.write("### Relationships")

            for rel in relationships:

                if len(rel) >= 2:

                    st.write(
                        f"{rel[0]} ➜ {rel[1]}"
                    )

        else:

            st.info(
                "No relationships identified."
            )

    # ---------------- JSON ----------------

    with tab5:

        st.json(
            risk_data
        )

    # ---------------- AI OUTPUT ----------------

    st.subheader(
        "🧠 AI Risk Scoring Output"
    )

    st.markdown(
    f"""
    <div style="
    background:#0F172A;
    color:white;
    padding:20px;
    border-radius:15px;
    overflow-x:auto;
    white-space:pre-wrap;
    ">
    {score_raw}
    </div>
    """,
    unsafe_allow_html=True
)

    # ---------------- PDF REPORT ----------------

    pdf_file = generate_pdf(
        change,
        impact,
        risk,
        training,
        risk_data["risk_score"]
    )

    with open(
        pdf_file,
        "rb"
    ) as file:
        st.write("")
        st.write("")
        st.download_button(
            label="📄 Download PDF Report",
            data=file,
            file_name="enterprise_change_report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    st.success(
        "✅ Analysis Completed Successfully"
    )