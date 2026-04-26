import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="Building Systems Architect Dashboard – built by Gesner Deslandes",
    page_icon="🏢",
    layout="wide"
)

# ========== SIMPLE LOGIN (any username/password) ==========
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def check_login():
    if not st.session_state.authenticated:
        st.markdown("## 🔐 Demo Access")
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            username = st.text_input("Username", placeholder="Any username")
            password = st.text_input("Password", type="password", placeholder="Any password")
            if st.button("Login", use_container_width=True):
                if username and password:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Please enter a username and password (any values work)")
        st.stop()

check_login()

# ========== HEADER ==========
st.title("🏢 Building Systems Architect Dashboard")
st.markdown("### *built by Gesner Deslandes*")
st.caption("Professional MEP & BMS Control Suite – Real‑time monitoring, thermal networks, electrical infrastructure, BIM‑ready asset register, decarbonisation tracking, and commissioning reports.")
st.markdown("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.image("https://flagcdn.com/w320/ht.png", width=80)
    st.markdown("### 📊 Dashboard Controls")
    refresh = st.button("🔄 Refresh Real‑Time Data")
    st.markdown("---")
    st.markdown("**Developer:** Gesner Deslandes")
    st.markdown("📞 (509)-47385663")
    st.markdown("✉️ deslandes78@gmail.com")
    st.markdown("---")
    st.markdown("### 💰 Pricing")
    st.markdown("**Full package (one‑time):** $4,500 USD")
    st.markdown("**Monthly subscription:** $299 USD / month")
    st.markdown("---")
    st.markdown("📢 *Live demo – any username/password works*")

# ========== GENERATE SIMULATED REAL-TIME BMS DATA ==========
def generate_bms_data():
    now = datetime.now()
    timestamps = [now - timedelta(minutes=i) for i in range(60, -1, -5)]
    data = {
        "timestamp": timestamps,
        "chw_supply_temp": [22.5 + random.uniform(-1.5, 1.5) for _ in timestamps],
        "chw_return_temp": [15.2 + random.uniform(-1.2, 1.2) for _ in timestamps],
        "lthw_supply_temp": [65.0 + random.uniform(-3, 3) for _ in timestamps],
        "lthw_return_temp": [52.0 + random.uniform(-2, 2) for _ in timestamps],
        "ahu_airflow": [8500 + random.uniform(-500, 500) for _ in timestamps],
        "power_kw": [320 + random.uniform(-30, 30) for _ in timestamps],
        "co2_ppm": [410 + random.uniform(-20, 30) for _ in timestamps],
    }
    return pd.DataFrame(data)

if refresh or "df" not in st.session_state:
    st.session_state.df = generate_bms_data()

df = st.session_state.df

# ========== KPI ROWS ==========
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🌡️ CHW Supply Temp", f"{df['chw_supply_temp'].iloc[-1]:.1f} °C", f"{df['chw_supply_temp'].iloc[-1] - df['chw_supply_temp'].iloc[-2]:+.1f}")
with col2:
    st.metric("🔥 LTHW Supply Temp", f"{df['lthw_supply_temp'].iloc[-1]:.1f} °C", f"{df['lthw_supply_temp'].iloc[-1] - df['lthw_supply_temp'].iloc[-2]:+.1f}")
with col3:
    st.metric("⚡ Power Demand", f"{df['power_kw'].iloc[-1]:.0f} kW", f"{df['power_kw'].iloc[-1] - df['power_kw'].iloc[-2]:+.0f}")
with col4:
    st.metric("🌫️ CO₂ Level", f"{df['co2_ppm'].iloc[-1]:.0f} ppm", f"{df['co2_ppm'].iloc[-1] - df['co2_ppm'].iloc[-2]:+.0f}")

st.markdown("---")

# ========== TABS ==========
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🌡️ Thermal Networks", "⚡ Electrical Infrastructure", "🌬️ AHU & Air Quality", "📊 BIM Asset Register", "📋 Commissioning Reports"])

with tab1:
    st.subheader("CHW & LTHW Thermal Networks")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=df["timestamp"], y=df["chw_supply_temp"], name="CHW Supply", line=dict(color="blue")))
    fig1.add_trace(go.Scatter(x=df["timestamp"], y=df["chw_return_temp"], name="CHW Return", line=dict(color="lightblue")))
    fig1.add_trace(go.Scatter(x=df["timestamp"], y=df["lthw_supply_temp"], name="LTHW Supply", line=dict(color="red")))
    fig1.add_trace(go.Scatter(x=df["timestamp"], y=df["lthw_return_temp"], name="LTHW Return", line=dict(color="orange")))
    fig1.update_layout(title="District Heating & Cooling Loops", xaxis_title="Time", yaxis_title="Temperature (°C)", height=500)
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.subheader("Electrical Infrastructure Monitoring")
    col21, col22 = st.columns(2)
    with col21:
        fig2 = px.line(df, x="timestamp", y="power_kw", title="Real‑Time Power Consumption (kW)", markers=True)
        st.plotly_chart(fig2, use_container_width=True)
    with col22:
        loads = {"HVAC": 42, "Lighting": 18, "Plug Loads": 25, "Elevators": 8, "Other": 7}
        fig_pie = px.pie(values=list(loads.values()), names=list(loads.keys()), title="Load Breakdown (%)")
        st.plotly_chart(fig_pie, use_container_width=True)

with tab3:
    st.subheader("AHU Performance & Indoor Air Quality")
    col31, col32 = st.columns(2)
    with col31:
        fig3 = px.line(df, x="timestamp", y="ahu_airflow", title="AHU Airflow (m³/h)", markers=True)
        st.plotly_chart(fig3, use_container_width=True)
    with col32:
        fig4 = px.line(df, x="timestamp", y="co2_ppm", title="CO₂ Concentration (ppm)", markers=True, color_discrete_sequence=["green"])
        st.plotly_chart(fig4, use_container_width=True)

with tab4:
    st.subheader("BIM‑Ready Asset Register")
    assets = pd.DataFrame({
        "Asset ID": ["AHU-01", "CHW-P-101", "LTHW-B-202", "MCC-3", "VAV-5A", "BMS-GW"],
        "Category": ["Air Handler", "Pump", "Boiler", "Switchgear", "VAV Box", "Gateway"],
        "Location": ["Level 3 MCR", "Basement Plant", "Roof", "Level 1 Elec RM", "Zone 5", "IT Closet"],
        "Last Maintenance": ["2026-03-15", "2026-04-01", "2026-02-28", "2026-04-10", "2026-03-20", "2026-04-05"],
        "Status": ["Normal", "Normal", "Alert", "Normal", "Normal", "Normal"]
    })
    st.dataframe(assets, use_container_width=True, hide_index=True)
    st.caption("Full BIM asset register with maintenance history and live status – exportable to CSV/IFC.")

with tab5:
    st.subheader("Commissioning Reports & Decarbonisation Tracking")
    st.markdown("#### ✅ Commissioning Status")
    comm_status = pd.DataFrame({
        "System": ["HVAC", "Electrical", "BMS", "Lighting", "Plumbing"],
        "Progress (%)": [100, 95, 88, 100, 92],
        "Sign-off Date": ["2026-04-20", "Pending", "Pending", "2026-04-18", "Pending"]
    })
    st.dataframe(comm_status, use_container_width=True, hide_index=True)
    
    st.markdown("#### 🌱 Decarbonisation Tracker")
    years = [2023, 2024, 2025, 2026]
    emissions = [1250, 1180, 1090, 980]  # tonnes CO2e
    fig_decarb = px.bar(x=years, y=emissions, labels={"x":"Year", "y":"tCO₂e"}, title="Carbon Emissions Reduction Pathway")
    st.plotly_chart(fig_decarb, use_container_width=True)
    st.success("Target: Net Zero by 2035 – On track with current efficiency measures.")

# ========== EXPORT REPORTS ==========
st.markdown("---")
st.subheader("📎 Export Reports")
col_export1, col_export2 = st.columns(2)
with col_export1:
    if st.button("📥 Download BMS Data (CSV)", use_container_width=True):
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Click to download", data=csv, file_name=f"bms_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv", mime="text/csv", use_container_width=True)
with col_export2:
    st.info("Full commissioning reports, BIM asset register, and decarbonisation plans available upon request.")

# ========== FOOTER ==========
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; padding: 1rem; background-color: #f0f2f6; border-radius: 12px;">
        <p>🏢 Building Systems Architect Dashboard – Built by <strong>Gesner Deslandes</strong></p>
        <p>📞 (509)-47385663 | ✉️ deslandes78@gmail.com</p>
        <p>© 2026 – Professional MEP & BMS Control Suite</p>
    </div>
    """,
    unsafe_allow_html=True
)
