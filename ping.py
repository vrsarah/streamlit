import streamlit as st
import time
from datetime import datetime

st.title("Self-Pinging Streamlit App")
st.write("This app will stay awake by periodically refreshing itself.")

# Auto-refresh using meta tag
st.markdown(
    """
    <meta http-equiv="refresh" content="60">
    """,
    unsafe_allow_html=True
)

# Display current time to show it's working
st.write(f"Last refresh: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Optional: Add a manual refresh button
if st.button("Manual Refresh"):
    st.rerun()
