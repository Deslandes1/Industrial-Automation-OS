import streamlit as st
from datetime import datetime
import time

st.set_page_config(
    page_title="Industrial Automation OS | Factory 4.0",
    page_icon="🏭",
    layout="wide"
)

# ---------- CUSTOM CSS (futuristic, readable) ----------
st.markdown("""
<style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #0a0f1a 0%, #0d1b2a 100%);
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0b1c2c 0%, #07121f 100%);
        border-right: 2px solid #00d4ff;
    }
    [data-testid="stSidebar"] .stMarkdown, 
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stCaption {
        color: #e0e0e0 !important;
    }
    /* Buttons */
    .stButton button {
        background-color: #00d4ff !important;
        color: #0a0f1a !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #ffaa33 !important;
        color: #0a0f1a !important;
        transform: scale(1.02);
    }
    /* Cards */
    .feature-card {
        background: rgba(0,212,255,0.1);
        border-radius: 20px;
        padding: 1.5rem;
        border: 1px solid rgba(0,212,255,0.3);
        backdrop-filter: blur(5px);
        transition: 0.2s;
    }
    .feature-card:hover {
        border-color: #ffaa33;
        transform: translateY(-5px);
    }
    /* Headers */
    h1, h2, h3 {
        color: #00d4ff !important;
        text-shadow: 0 0 5px rgba(0,212,255,0.3);
    }
    h4, h5, h6 {
        color: #ffaa33 !important;
    }
    p, li, .stMarkdown {
        color: #d0d0d0 !important;
    }
    /* Status badge */
    .status-pill {
        background-color: #ffaa33;
        color: #0a0f1a;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    /* Live clock */
    .live-clock {
        background: rgba(0,0,0,0.5);
        padding: 5px 10px;
        border-radius: 12px;
        font-family: monospace;
        font-size: 1rem;
        color: #00d4ff;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        border-top: 1px solid #00d4ff;
    }
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR (spinning globe, contact, pricing) ----------
st.sidebar.markdown("""
<style>
.spin-globe {
    font-size: 80px;
    animation: spin 4s linear infinite;
    display: inline-block;
    text-align: center;
}
@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
</style>
<div style="text-align: center;">
    <div class="spin-globe">🌍</div>
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("## **GlobalInternet.py**")
st.sidebar.markdown("### Industrial Automation OS")
st.sidebar.markdown("---")
st.sidebar.markdown("**Lead Engineer:** Gesner Deslandes")
st.sidebar.markdown("---")
st.sidebar.markdown("📞 **Phone:** (509)-47385663")
st.sidebar.markdown("✉️ **Email:** deslandes78@gmail.com")
st.sidebar.markdown("---")
st.sidebar.markdown("**🌐 Website:**")
st.sidebar.markdown("[https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
st.sidebar.markdown("---")

# Pricing table
st.sidebar.markdown("### 💰 Licensing (Industrial OS)")
st.sidebar.markdown("""
| Plan | Price (USD/year) |
|------|------------------|
| **Single Factory** | $4,999 |
| **Multi‑Site (5 factories)** | $19,999 |
| **Enterprise (unlimited)** | $49,999 |
| **Source + OEM License** | $99,999 |
""")
st.sidebar.info("✅ Includes 24/7 support, updates, and AI model training.")
st.sidebar.caption("© GlobalInternet.py – Industry 4.0 ready")

# ---------- MAIN CONTENT ----------
# Live clock
live_time = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
st.markdown(f'<div style="text-align: right;"><span class="live-clock">🕒 {live_time}</span></div>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🏭 Industrial Automation OS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Complete operating system for factories – orchestrating humanoid robots, conveyor belts, and quality inspection AI.</p>", unsafe_allow_html=True)

# Status and key tech
col_status, col_tech = st.columns(2)
with col_status:
    st.markdown('<div class="status-pill">📅 Status: Planning – Q4 2026</div>', unsafe_allow_html=True)
with col_tech:
    st.markdown('<div class="status-pill">⚡ Key technology: Industry 4.0 ready</div>', unsafe_allow_html=True)

st.markdown("---")

# Feature cards
st.markdown("## 🚀 Core Modules")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
    <h3>🤖 Humanoid Robot Orchestrator</h3>
    <p>Real‑time task allocation, path planning, and collaborative safety. Supports ROS 2, OpenCR, and custom firmware.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    <h3>📦 Smart Conveyor Control</h3>
    <p>Adaptive speed, load balancing, predictive maintenance. Integrates with Siemens, Allen‑Bradley, and OPC UA.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
    <h3>🔍 Quality Inspection AI</h3>
    <p>Computer vision defect detection, real‑time alerts, and root‑cause analysis. Edge or cloud deployment.</p>
    </div>
    """, unsafe_allow_html=True)

# Technical specifications
st.markdown("---")
st.markdown("## ⚙️ Technical Highlights")

tech_col1, tech_col2 = st.columns(2)
with tech_col1:
    st.markdown("""
    - **Orchestration engine:** Kubernetes + custom scheduler
    - **Robot APIs:** REST, gRPC, WebSocket
    - **Security:** Zero‑trust architecture, TLS 1.3, ISO 27001 ready
    - **Edge AI:** TensorFlow Lite, OpenVINO, NVIDIA Jetson
    """)
with tech_col2:
    st.markdown("""
    - **Dashboard:** Real‑time 3D factory twin (Three.js)
    - **Data pipeline:** MQTT, Kafka, TimescaleDB
    - **Compliance:** CE, UL, IEC 62443
    - **Languages:** Python, C++, Go for extensions
    """)

# Timeline / roadmap
st.markdown("---")
st.markdown("## 🗓️ Roadmap")

timeline = """
| Milestone | Estimated Completion |
|-----------|----------------------|
| Prototype (single robot + conveyor) | Q1 2025 |
| Alpha release (3 robots, basic AI) | Q3 2025 |
| Beta – 5 factories | Q2 2026 |
| General availability (Industry 4.0 certified) | Q4 2026 |
"""
st.markdown(timeline)

# Contact / CTA
st.markdown("---")
st.markdown("## 📢 Partner with us")
st.markdown("""
We are looking for **early adopters** and **integration partners** to pilot Industrial Automation OS.  
Contact us for a demo or to discuss custom features.

📞 (509)-47385663  |  ✉️ deslandes78@gmail.com  
🌐 [https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)
""")

# Footer
st.markdown('<div class="footer">© GlobalInternet.py – Building the future of factory automation with a Haitian touch.</div>', unsafe_allow_html=True)

# Auto-refresh clock every second (just for demo)
# We can use a small JavaScript to update the live clock – but for simplicity we keep the static timestamp
# Adding a simple rerun every 60 seconds to update the clock? Not necessary, but user can refresh.
