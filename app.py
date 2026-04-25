import streamlit as st
import pandas as pd
import numpy as np
import datetime
import random
import plotly.graph_objects as go
import plotly.express as px

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
if "language" not in st.session_state:
    st.session_state.language = "en"

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
            username = st.text_input("👤 Username", placeholder="any username")
            password = st.text_input("🔒 Password", type="password", placeholder="any password")
            if st.form_submit_button("🚀 Sign In", use_container_width=True) and username and password:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            elif st.form_submit_button:
                st.error("Please enter username and password.")
        st.markdown("""
        <p style='text-align:center;'>✨ Demo credentials: any username / any password</p>
        <p style='text-align:center;'>📞 (509) 4738-5663 | ✉️ deslandes78@gmail.com</p>
        <p style='text-align:center;'>🌐 https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/</p>
        """, unsafe_allow_html=True)

# ========== MAIN DASHBOARD ==========
def main_app():
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/2905/2905715.png", width=80)
        st.markdown(f"**Welcome, {st.session_state.username}**")
        st.markdown("---")
        st.markdown("### 💰 Pricing")
        st.markdown("**One‑time license:** **$4,500 USD**  \n*Full source code, 1 year support, lifetime updates*")
        st.markdown("")
        st.markdown("**Monthly subscription:** **$350 USD / month**  \n*All features + priority support*")
        st.markdown("---")
        st.markdown("**Contact:**")
        st.markdown("📞 (509) 4738-5663")
        st.markdown("✉️ deslandes78@gmail.com")
        st.markdown("🌐 [GlobalInternet.py](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
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
    
    tabs = st.tabs([
        "📊 BMS Overview",
        "🌡️ Thermal Networks",
        "⚡ Electrical Infrastructure",
        "📁 Asset Register (BIM)",
        "🌱 Decarbonisation & Energy",
        "📋 Commissioning & Reports"
    ])
    
    with tabs[0]:
        st.subheader("Building Management System (BMS) Real‑time Performance")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("AHU-1 Supply Temp", f"{random.uniform(18.5, 22.5):.1f} °C", delta="+0.3")
        with col2:
            st.metric("Chiller Plant Efficiency", f"{random.uniform(0.65, 0.85):.2f} kW/kW", delta="-0.02")
        with col3:
            st.metric("Space CO₂ (Main Hall)", f"{random.randint(380, 450)} ppm", delta="-12")
        with col4:
            st.metric("BMS Uptime", "99.98%", delta="+0.01%")
        
        alarms = pd.DataFrame({
            "Time": [datetime.datetime.now().strftime("%H:%M:%S"), "08:23:15", "07:45:00"],
            "Equipment": ["AHU-3", "Chiller #2", "VAV Box 12"],
            "Message": ["High supply air temp", "Low refrigerant pressure", "Damper stuck"],
            "Severity": ["Warning", "Critical", "Info"]
        })
        st.dataframe(alarms, use_container_width=True)
        
        st.subheader("Supply Air Temperature (Last 24h)")
        time_series = pd.DataFrame({
            "Time": pd.date_range(end=datetime.datetime.now(), periods=24, freq="H"),
            "Temp": [20.5 + 0.8 * np.sin(i/3) + random.uniform(-0.5,0.5) for i in range(24)]
        })
        fig = px.line(time_series, x="Time", y="Temp", title="AHU-1 Supply Air Temperature")
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with tabs[1]:
        st.subheader("Chilled Water (CHW) & Low Temperature Hot Water (LTHW) Networks")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("CHW Supply Temp", "6.2 °C", delta="-0.3")
            st.metric("CHW Return Temp", "12.8 °C", delta="+0.2")
            st.metric("CHW Flow Rate", "245 m³/h", delta="+5")
        with col2:
            st.metric("LTHW Supply", "45.5 °C", delta="-0.5")
            st.metric("LTHW Return", "38.2 °C", delta="-0.2")
            st.metric("LTHW Pressure", "2.8 bar", delta="0.0")
        
        st.markdown("**Thermal Network Schematic**")
        st.image("https://via.placeholder.com/800x300?text=CHW+LTHW+Network+Diagram", use_column_width=True)
        
        st.success("✅ Heat‑network‑ready: Electric heat pumps planned for 2027")
        st.info("💡 Recommendation: Upgrade CHW plant to magnetic bearing chillers (estimated 22% efficiency gain)")
    
    with tabs[2]:
        st.subheader("Primary Electrical Distribution")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Main HV Intake", "11 kV", delta="Normal")
            st.metric("Transformer 1 Load", "82%", delta="+3%")
        with col2:
            st.metric("Transformer 2 Load", "76%", delta="-1%")
            st.metric("Power Factor", "0.95", delta="+0.01")
        with col3:
            st.metric("UPS Load (Data Centre)", "43%", delta="-2%")
            st.metric("Standby Generator", "Ready", delta="Last test: OK")
        
        switch_data = pd.DataFrame({
            "Board": ["MCC-1", "MCC-2", "Lighting Panel A", "BMS Panel"],
            "Current (A)": [280, 315, 45, 12],
            "Voltage (V)": [415, 415, 230, 230],
            "Status": ["Normal", "Normal", "Warning", "Normal"]
        })
        st.dataframe(switch_data, use_container_width=True)
        st.caption("All circuits comply with BS 7671 (18th Edition)")
    
    with tabs[3]:
        st.subheader("MEP Asset Register & BIM Integration")
        assets = pd.DataFrame({
            "Asset ID": ["MEP-1001", "MEP-1002", "MEP-1003", "MEP-1004"],
            "Equipment": ["Centrifugal Chiller", "AHU-1", "VSD Pump", "LV Switchgear"],
            "Location": ["Plant Room B2", "Roof Level 3", "Basement", "Main Substation"],
            "Install Date": ["2018-06-01", "2019-02-15", "2020-08-22", "2015-11-30"],
            "Last Maintained": ["2026-04-10", "2026-03-05", "2026-04-18", "2026-02-20"],
            "Status": ["Operational", "Operational", "Review", "Operational"]
        })
        st.dataframe(assets, use_container_width=True)
        st.info("🔗 BIM model available via COBie export – Revit 2025 compatible. Asset data synchronised with BIM 360.")
        st.subheader("Infrastructure Record Updates")
        st.write("Last change: 2026-04-24 – Updated CHW pipework schematics (drawing M-401 Rev B)")
    
    with tabs[4]:
        st.subheader("Energy Performance & Carbon Reduction Tracker")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Annual Energy Consumption", "12.4 MWh", delta="-8% vs 2025")
            st.metric("Carbon Intensity", "42 kgCO₂/m²", delta="-11%")
        with col2:
            st.metric("Renewable Generation (PV)", "345 MWh", delta="+12%")
            st.metric("Heat Pump Contribution", "38%", delta="+5%")
        
        energy_data = pd.DataFrame({
            "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
            "HVAC": [320, 305, 290, 275, 280],
            "Lighting": [145, 138, 132, 125, 128],
            "Other": [95, 88, 82, 79, 81]
        })
        fig2 = px.bar(energy_data, x="Month", y=["HVAC", "Lighting", "Other"], title="Energy Usage (MWh)")
        st.plotly_chart(fig2, use_container_width=True)
        st.success("✅ Target: Net zero carbon by 2035 – On track. Electrification of CHW plant scheduled for 2028.")
    
    with tabs[5]:
        st.subheader("Commissioning Witness & Project Delivery")
        comm_log = pd.DataFrame({
            "Date": ["2026-04-22", "2026-04-15", "2026-04-10"],
            "System": ["AHU-5 VAV Boxes", "CHW Pump #4", "BMS Upgrade"],
            "Result": ["Pass", "Pass w/ comments", "Pass"],
            "Witnessed By": ["Gesner Deslandes", "External Consultant", "Estate Team"]
        })
        st.dataframe(comm_log, use_container_width=True)
        
        report_type = st.selectbox("Select Report Type", ["Monthly BMS Summary", "Commissioning Log", "Asset Condition Report", "Carbon Reduction Plan"])
        if st.button("📥 Generate & Download CSV"):
            df_report = pd.DataFrame({"Sample Data": [report_type, datetime.datetime.now().isoformat()]})
            csv = df_report.to_csv(index=False)
            st.download_button("Download CSV", csv, f"{report_type.replace(' ', '_')}.csv", "text/csv")
            st.success("Report generated successfully")
        
        st.info("📌 All capital projects are supported through the soft‑landings framework. Post‑occupancy evaluations scheduled for Q3 2026.")
    
    st.markdown("---")
    st.caption("Built with 💖 by Gesner Deslandes – GlobalInternet.py")

if not st.session_state.authenticated:
    login_page()
else:
    main_app()
