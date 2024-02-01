import streamlit as st

start = st.date_input('Start Date')
end = st.date_input('End Date')
if start and end:
    st.write(end-start)
