import streamlit as st
from datetime import datetime
import random

st.set_page_config(
    page_title="Industrial Automation OS | Factory 4.0",
    page_icon="🏭",
    layout="wide"
)

# ---------- CUSTOM CSS (futuristic, readable, log white) ----------
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
    .metric-card {
        background: rgba(0,0,0,0.5);
        border-radius: 15px;
        padding: 1rem;
        text-align: center;
        border-left: 4px solid #00d4ff;
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
    /* Force all text inside the event log area to white */
    .event-log, .event-log p, .event-log div, .event-log span {
        color: white !important;
        font-family: monospace;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------- AUTHENTICATION STATE ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ---------- LOGOUT FUNCTION ----------
def logout():
    st.session_state.authenticated = False
    st.rerun()

# ---------- LOGIN PAGE (colorful, with spinning globe symbols) ----------
def show_login():
    st.markdown("""
    <style>
    .login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 80vh;
    }
    .login-card {
        background: rgba(15, 52, 96, 0.8);
        backdrop-filter: blur(12px);
        border-radius: 30px;
        padding: 2.5rem;
        text-align: center;
        border: 1px solid rgba(0,212,255,0.5);
        box-shadow: 0 0 40px rgba(0,212,255,0.2);
        width: 100%;
        max-width: 450px;
    }
    .spinning-globe {
        font-size: 80px;
        animation: spin 4s linear infinite;
        display: inline-block;
        margin-bottom: 1rem;
    }
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    .login-title {
        color: #00d4ff;
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    </style>
    <div class="login-container">
        <div class="login-card">
            <div class="spinning-globe">🌍</div>
            <div class="login-title">Industrial Automation OS</div>
            <p style="color: #d0d0d0;">Enter secure password to access the factory control system</p>
    """, unsafe_allow_html=True)
    
    password = st.text_input("Password", type="password", key="login_pass")
    if st.button("🔐 Login", use_container_width=True):
        if password == "20082010":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password. Access denied.")
    
    st.markdown("</div></div>", unsafe_allow_html=True)

# ---------- SIDEBAR (common to both modes after login) ----------
def show_sidebar():
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
    
    # Mode selection (only after login)
    mode = st.sidebar.radio("🔧 Operating Mode", ["📘 Demo Mode", "🏭 Real‑World Mode"], index=0)
    
    # Pricing (visible in both modes)
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
    
    # Logout button
    if st.sidebar.button("🔓 Logout", use_container_width=True):
        logout()
    
    return mode

# ---------- DEMO MODE ----------
def demo_mode():
    st.markdown("<h1 style='text-align: center;'>🏭 Industrial Automation OS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Complete operating system for factories – orchestrating humanoid robots, conveyor belts, and quality inspection AI.</p>", unsafe_allow_html=True)
    
    col_status, col_tech = st.columns(2)
    with col_status:
        st.markdown('<div class="status-pill">📅 Status: Planning – Q4 2026</div>', unsafe_allow_html=True)
    with col_tech:
        st.markdown('<div class="status-pill">⚡ Key technology: Industry 4.0 ready</div>', unsafe_allow_html=True)
    
    st.markdown("---")
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
    
    st.markdown("---")
    st.markdown("## 📢 Partner with us")
    st.markdown("""
    We are looking for **early adopters** and **integration partners** to pilot Industrial Automation OS.  
    Contact us for a demo or to discuss custom features.

    📞 (509)-47385663  |  ✉️ deslandes78@gmail.com  
    🌐 [https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)
    """)

# ---------- REAL‑WORLD MODE (with white log text) ----------
def real_world_mode():
    st.markdown("<h1 style='text-align: center;'>🏭 REAL‑TIME FACTORY FLOOR</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Live controls – robot speed, conveyor status, AI inspection</p>", unsafe_allow_html=True)
    
    # Session state for simulation
    if "robot_speed" not in st.session_state:
        st.session_state.robot_speed = 50
    if "conveyor_running" not in st.session_state:
        st.session_state.conveyor_running = True
    if "defect_rate" not in st.session_state:
        st.session_state.defect_rate = 0
    if "last_defect" not in st.session_state:
        st.session_state.last_defect = "No defects detected"
    
    col_speed, col_conveyor, col_inspect = st.columns(3)
    with col_speed:
        st.markdown("### 🤖 Robot Speed")
        speed = st.slider("Speed (0–100%)", 0, 100, st.session_state.robot_speed, key="speed_slider")
        if speed != st.session_state.robot_speed:
            st.session_state.robot_speed = speed
            st.success(f"Robot speed set to {speed}%")
        st.metric("Current Speed", f"{st.session_state.robot_speed}%")
    with col_conveyor:
        st.markdown("### 📦 Conveyor Belt")
        running = st.toggle("Conveyor Running", value=st.session_state.conveyor_running)
        if running != st.session_state.conveyor_running:
            st.session_state.conveyor_running = running
            state = "RUNNING" if running else "STOPPED"
            st.warning(f"Conveyor {state}")
        st.metric("Status", "Active" if st.session_state.conveyor_running else "Idle")
    with col_inspect:
        st.markdown("### 🔍 AI Inspection")
        if st.button("Run Quality Check"):
            defect = random.random() < 0.15
            if defect:
                st.session_state.defect_rate += 1
                st.session_state.last_defect = f"Defect found at {datetime.now().strftime('%H:%M:%S')}"
                st.error(st.session_state.last_defect)
            else:
                st.success(f"Inspection passed – {datetime.now().strftime('%H:%M:%S')}")
        st.metric("Total Defects Today", st.session_state.defect_rate)
        st.caption(st.session_state.last_defect if st.session_state.defect_rate > 0 else "No defects yet")
    
    st.markdown("---")
    st.markdown("## 📊 Live Factory Metrics")
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    throughput = round((st.session_state.robot_speed / 100) * (1 if st.session_state.conveyor_running else 0) * 120, 1)
    with metric_col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Throughput (units/hour)", f"{throughput}")
        st.markdown('</div>', unsafe_allow_html=True)
    energy = round(throughput * 0.8 + 50, 1)
    with metric_col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Energy (kWh)", f"{energy}")
        st.markdown('</div>', unsafe_allow_html=True)
    confidence = random.randint(85, 99)
    with metric_col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("AI Detection Confidence", f"{confidence}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("## 📝 Event Log")
    if st.button("Reset Simulation"):
        st.session_state.robot_speed = 50
        st.session_state.conveyor_running = True
        st.session_state.defect_rate = 0
        st.session_state.last_defect = "No defects detected"
        st.rerun()
    
    # Build log entries with bright white inline CSS
    log_entries = [
        f"{datetime.now().strftime('%H:%M:%S')} - System ready. Robot speed: {st.session_state.robot_speed}%",
        f"{datetime.now().strftime('%H:%M:%S')} - Conveyor {'running' if st.session_state.conveyor_running else 'stopped'}",
        f"{datetime.now().strftime('%H:%M:%S')} - AI model loaded (confidence {confidence}%)",
    ]
    st.markdown('<div class="event-log">', unsafe_allow_html=True)
    for log in log_entries:
        st.markdown(f'<p style="color: white; font-family: monospace; margin: 0;">{log}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.info("💡 Real‑world mode simulates a factory control panel. Actual hardware integration available upon request.")

# ---------- MAIN APP ----------
if not st.session_state.authenticated:
    show_login()
else:
    selected_mode = show_sidebar()
    
    # Live clock (top right)
    live_time = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
    st.markdown(f'<div style="text-align: right;"><span class="live-clock">🕒 {live_time}</span></div>', unsafe_allow_html=True)
    
    if selected_mode == "📘 Demo Mode":
        demo_mode()
    else:
        real_world_mode()
    
    st.markdown('<div class="footer">© GlobalInternet.py – Building the future of factory automation with a Haitian touch.</div>', unsafe_allow_html=True)
