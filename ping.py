import streamlit as st
import threading

st.title("Self-Pinging Streamlit App")
st.write("This app will stay awake by periodically refreshing itself.")

def self_refresh():
    threading.Timer(60, self_refresh).start()  # Refresh every 60 seconds
    st.experimental_rerun()

if "self_refresh_started" not in st.session_state:
    st.session_state.self_refresh_started = True
    self_refresh()

st.write("Self-refreshing mechanism started.")
