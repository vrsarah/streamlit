import streamlit as st
import requests
import threading
import time
from datetime import datetime

st.title("Self-Pinging Streamlit App")

def ping_self():
    """Background thread that pings the app URL"""
    while True:
        try:
            # Get the current URL (you'll need to replace with your actual deployed URL)
            app_url = "https://connect.posit.cloud/vrsarah/content/019866d5-3931-b4d7-68dd-7e56ea9d588a"
            response = requests.get(app_url, timeout=10)
            st.session_state.last_ping = datetime.now()
            time.sleep(300)  # Ping every 5 minutes
        except Exception as e:
            st.session_state.ping_error = str(e)
            time.sleep(60)  # Retry after 1 minute on error

# Initialize session state
if "ping_started" not in st.session_state:
    st.session_state.ping_started = False
    st.session_state.last_ping = None
    st.session_state.ping_error = None

# Start background pinging
if not st.session_state.ping_started:
    thread = threading.Thread(target=ping_self, daemon=True)
    thread.start()
    st.session_state.ping_started = True

st.write(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
if st.session_state.last_ping:
    st.write(f"Last self-ping: {st.session_state.last_ping.strftime('%Y-%m-%d %H:%M:%S')}")
if st.session_state.ping_error:
    st.error(f"Ping error: {st.session_state.ping_error}")

if st.button("Refresh Status"):
    st.rerun()
