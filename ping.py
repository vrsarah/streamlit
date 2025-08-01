import streamlit as st
import requests
import threading
import time
from datetime import datetime

st.title("Self-Pinging Streamlit App")


def ping_self():
    """Background thread that pings the app URL with browser-like behavior"""
    session = requests.Session()

    # Browser-like headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache'
    }

    while True:
        try:
            app_url = "https://connect.posit.cloud/vrsarah/content/019866d5-3931-b4d7-68dd-7e56ea9d588a"
            response = session.get(app_url, headers=headers, timeout=15, allow_redirects=True)

            st.session_state.last_ping = datetime.now()
            st.session_state.ping_error = None
            st.session_state.ping_count = st.session_state.get("ping_count", 0) + 1
            st.session_state.response_code = response.status_code

            time.sleep(60)  # Ping every 60 seconds

        except Exception as e:
            st.session_state.ping_error = str(e)
            st.session_state.last_error_time = datetime.now()
            time.sleep(30)


# Initialize session state
if "ping_started" not in st.session_state:
    st.session_state.ping_started = False
    st.session_state.last_ping = None
    st.session_state.ping_error = None
    st.session_state.ping_count = 0
    st.session_state.response_code = None
    st.session_state.last_error_time = None

# Start background pinging
if not st.session_state.ping_started:
    thread = threading.Thread(target=ping_self, daemon=True)
    thread.start()
    st.session_state.ping_started = True

# Display status
st.write(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.write(f"Total pings sent: {st.session_state.ping_count}")

if st.session_state.last_ping:
    time_since_ping = (datetime.now() - st.session_state.last_ping).total_seconds()
    st.write(
        f"Last successful ping: {st.session_state.last_ping.strftime('%Y-%m-%d %H:%M:%S')} ({time_since_ping:.0f}s ago)")
    if st.session_state.response_code:
        st.write(f"Response code: {st.session_state.response_code}")

if st.session_state.ping_error:
    st.error(f"Last ping error: {st.session_state.ping_error}")
    if st.session_state.last_error_time:
        st.write(f"Error occurred at: {st.session_state.last_error_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Auto-refresh every 60 seconds to show live status
time.sleep(60)
st.rerun()
