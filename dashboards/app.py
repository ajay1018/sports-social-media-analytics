import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sports Social Analytics", layout="wide")
st.title("🏟️ Sports Social Media Analytics")

team = pd.read_csv("data/processed/team_metrics.csv")
league = pd.read_csv("data/processed/league_metrics.csv")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Engagement by Team")
    st.bar_chart(team.set_index("team")["engagement"])
with col2:
    st.subheader("Engagement by League")
    st.bar_chart(league.set_index("league")["engagement"])

st.caption("Demo data. Replace extract step with API ingestion later.")
