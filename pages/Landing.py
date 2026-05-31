import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Enterprise Change Intelligence",
    layout="wide"
)

# ---------------- HIDE SIDEBAR ----------------
st.markdown("""
<style>

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

section[data-testid="stSidebarNav"] {
    display: none;
}

.stApp {
    background-color: white;
}

.hero-title {
    font-size: 40px;
    font-weight: 700;
    color: #111827;
    text-align: center;
    margin-top: 30px;
}

.hero-subtitle {
    font-size: 22px;
    color: #4B5563;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 50px;
}

.feature-card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    text-align: center;
    min-height: 220px;
}

.feature-title {
    font-size: 22px;
    font-weight: 700;
    color: #111827;
    margin-top: 10px;
}

.feature-desc {
    color: #6B7280;
    font-size: 15px;
    margin-top: 10px;
}

.stats {
    text-align: center;
    padding: 20px;
}

.stat-number {
    font-size: 38px;
    font-weight: 800;
    color: #111827;
}

.stat-text {
    color: #6B7280;
}
/* BUTTON */

.stButton > button{
    background:#0F172A !important;
    color:white !important;
    border:none !important;
    border-radius:14px !important;
    height:55px !important;
    font-size:22px !important;
    font-weight:700 !important;
}

.stButton > button *{
    color:white !important;
}

/* HOVER FIX */

.stButton > button:hover{
    background:#0F172A !important;
    color:white !important;
    border:none !important;
}

.stButton > button:hover *{
    color:white !important;
}

/* FOCUS FIX */

.stButton > button:focus{
    background:#0F172A !important;
    color:white !important;
    box-shadow:none !important;
}

.stButton > button:active{
    background:#0F172A !important;
    color:white !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero-title">
ImpactIQ - Multi-Agent AI-Driven Enterprise Change Intelligence and Decision Support System
</div>

<div class="hero-subtitle">
Analyze Business Impact • Predict Risks • Generate Enterprise Reports • Understand System Dependencies
</div>
""", unsafe_allow_html=True)

# ---------------- FEATURES ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h1>🧠</h1>
        <div class="feature-title">
            Multi-Agent AI
        </div>
        <div class="feature-desc">
            Specialized AI agents collaborate to perform enterprise change analysis.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h1>📊</h1>
        <div class="feature-title">
            Risk Assessment
        </div>
        <div class="feature-desc">
            Predict operational, technical, security and business risks.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h1>🔗</h1>
        <div class="feature-title">
            Dependency Analysis
        </div>
        <div class="feature-desc">
            Identify impacted systems and enterprise dependencies automatically.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <h1>📄</h1>
        <div class="feature-title">
            PDF Reports
        </div>
        <div class="feature-desc">
            Generate executive-ready reports for decision makers instantly.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- STATS ----------------
s1, s2, s3 = st.columns(3)

with s1:
    st.markdown("""
    <div class="stats">
        <div class="stat-number">4</div>
        <div class="stat-text">AI Agents</div>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class="stats">
        <div class="stat-number">100+</div>
        <div class="stat-text">Enterprise Scenarios</div>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class="stats">
        <div class="stat-number">1 Click</div>
        <div class="stat-text">Impact Analysis</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- BUTTON ----------------
c1, c2, c3 = st.columns([2, 2, 2])

with c2:

    if st.button(
        "🚀 Launch Platform",
        use_container_width=True
    ):
        st.switch_page("pages/Login.py")