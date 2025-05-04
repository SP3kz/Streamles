import streamlit as st
import pandas as pd
import json
import requests

# Set page config
st.set_page_config(page_title="OMEGA-Surge Dashboard", layout="wide")

# Load CSV files
@st.cache_data
def load_data():
    drop_schedule = pd.read_csv("monthly_drop_schedule.csv")
    licensing_kit = pd.read_csv("white_label_licensing_kit.csv")
    multipliers = pd.read_csv("multipliers_dashboard.csv")
    return drop_schedule, licensing_kit, multipliers

drop_schedule, licensing_kit, multipliers = load_data()

# Display Sections
st.title("🚀 OMEGA-Surge 100X Dashboard")

st.header("📆 Monthly Drop Schedule")
st.dataframe(drop_schedule)

st.header("🏷️ White-Label Licensing Kit")
st.dataframe(licensing_kit)

st.header("♾️ Multipliers Dashboard")
st.dataframe(multipliers)

# Simulated Flowly Webhook Test
st.subheader("🔗 Flowly Trigger")
if st.button("Ping Flowly Webhook"):
    try:
        with open("flowly_config.json") as f:
            config = json.load(f)
        webhook_url = config["webhook_url"]
        payload = {"status": "manual-ping", "source": "streamlit-app"}
        r = requests.post(webhook_url, json=payload)
        if r.status_code == 200:
            st.success("Webhook sent successfully!")
        else:
            st.warning(f"Webhook failed with status code: {r.status_code}")
    except Exception as e:
        st.error(f"Error sending webhook: {e}")
