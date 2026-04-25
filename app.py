import streamlit as st
import pandas as pd
import numpy as np
import datetime
import random

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="Building Systems Architect Dashboard - Gesner Deslandes",
    page_icon="🏢",
    layout="wide"
)

# ========== SESSION STATE ==========
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""

# ========== LOGIN PAGE ==========
def login_page():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="color: #1e3c72;">🏢 Building Systems Architect Dashboard</h1>
            <h3 style="color: #2a5298;">MEP & BMS Control Suite</h3>
            <p>built by <strong>Gesner Deslandes</strong> – GlobalInternet.py</p>
        </div>
        """, unsafe_allow_html=True)
        with st.form("login"):
            username = st.text_input("👤 Username")
            password = st.text_input("🔒 Password", type="password")
            if st.form_submit_button("🚀 Sign In", use_container_width=True) and username and password:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            elif st.form_submit_button:
                st.error("Please enter username and password.")
        st.markdown("""
        <p style='text-align:center;'>✨ Demo credentials: any username / any password</p>
        <p style='text-align:center;'>📞 (509) 4738-5663 | ✉️ deslandes78@gmail.com</p>
        """, unsafe_allow_html=True)

# ========== MAIN DASHBOARD ==========
def main_app():
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/2905/2905715.png", width=80)
        st.markdown(f"**Welcome, {st.session_state.username}**")
        st.markdown("---")
        st.markdown("### 💰 Pricing")
        st.markdown("**One‑time license:** **$4,500 USD**")
        st.markdown("**Monthly subscription:** **$350 USD / month**")
        st.markdown("---")
        st.markdown("**Contact:**")
        st.markdown("📞 (509) 4738-5663")
        st.markdown("✉️ deslandes78@gmail.com")
        st.markdown("---")
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()
        st.caption("© 2026 GlobalInternet.py – built by Gesner Deslandes")
    
    st.markdown("""
    <div style="background: linear-gradient(90deg, #1e3c72, #2a5298); padding: 1rem; border-radius: 20px; color: white; text-align: center; margin-bottom: 2rem;">
        <h1>🏢 Building Systems Architect Dashboard</h1>
        <p>MEP & BMS Control Suite – Real‑time monitoring, asset management, thermal networks & decarbonisation</p>
    </div>
    """, unsafe_allow_html=True)
    
    tabs = st.tabs(["📊 BMS Overview", "🌡️ Thermal Networks", "⚡ Electrical Infrastructure", "📁 Asset Register", "🌱 Decarbonisation", "📋 Reports"])
    
    with tabs[0]:
        st.subheader("BMS Real‑time Performance")
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.metric("AHU-1 Supply Temp", f"{random.uniform(18.5,22.5):.1f} °C")
        with col2: st.metric("Chiller Efficiency", f"{random.uniform(0.65,0.85):.2f} kW/kW")
        with col3: st.metric("CO₂ Level", f"{random.randint(380,450)} ppm")
        with col4: st.metric("BMS Uptime", "99.98%")
        st.subheader("Supply Air Temperature Trend")
        # Fixed: use '60min' instead of 'H' to avoid pandas frequency error
        end_time = datetime.datetime.now()
        time_index = pd.date_range(end=end_time, periods=24, freq='60min')
        temp_values = [20.5 + 0.8 * np.sin(i/3) for i in range(24)]
        df_temp = pd.DataFrame({"Temp": temp_values}, index=time_index)
        st.line_chart(df_temp)
    
    with tabs[1]:
        st.subheader("CHW & LTHW Networks")
        c1, c2 = st.columns(2)
        with c1:
            st.metric("CHW Supply", "6.2 °C")
            st.metric("CHW Return", "12.8 °C")
        with c2:
            st.metric("LTHW Supply", "45.5 °C")
            st.metric("LTHW Return", "38.2 °C")
        st.success("✅ Heat‑network‑ready: Electric heat pumps planned for 2027")
    
    with tabs[2]:
        st.subheader("Electrical Distribution")
        col1, col2, col3 = st.columns(3)
        with col1: st.metric("HV Intake", "11 kV")
        with col2: st.metric("Transformer 1 Load", "82%")
        with col3: st.metric("Power Factor", "0.95")
        st.dataframe(pd.DataFrame({"Board": ["MCC-1","MCC-2"], "Current (A)": [280,315]}))
    
    with tabs[3]:
        st.subheader("Asset Register")
        st.dataframe(pd.DataFrame({
            "Asset ID": ["MEP-1001","MEP-1002"], "Equipment": ["Chiller","AHU-1"], "Status": ["Operational","Operational"]
        }))
    
    with tabs[4]:
        st.subheader("Energy & Carbon")
        st.metric("Annual Energy", "12.4 MWh", delta="-8%")
        st.metric("Carbon Intensity", "42 kgCO₂/m²", delta="-11%")
        st.success("Target: Net zero by 2035")
    
    with tabs[5]:
        st.subheader("Generate Report")
        if st.button("Download CSV"):
            st.success("Report ready")
    
    st.caption("Built by Gesner Deslandes – GlobalInternet.py")

if not st.session_state.authenticated:
    login_page()
else:
    main_app()
