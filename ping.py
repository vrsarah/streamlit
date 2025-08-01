import streamlit as st
import time
from datetime import datetime

st.title("Self-Pinging Streamlit App")
st.write("This app will stay awake by periodically refreshing itself.")

# JavaScript auto-refresh
st.markdown(
    """
    <script>
    setTimeout(function(){
        window.location.reload(1);
    }, 60000); // 60 seconds
    </script>
    """,
    unsafe_allow_html=True
)

# Show last update time
if "last_update" not in st.session_state:
    st.session_state.last_update = datetime.now()

st.write(f"App started/refreshed at: {st.session_state.last_update.strftime('%Y-%m-%d %H:%M:%S')}")
st.write(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Update timestamp on each run
st.session_state.last_update = datetime.now()
