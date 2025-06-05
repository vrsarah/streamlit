import streamlit as st
import locale
import os
from datetime import datetime

st.set_page_config(page_title="European Characters Test", layout="wide")

st.title("European Characters Test")

st.header("Locale Test")

# Display locale information
col1, col2 = st.columns(2)

with col1:
    st.subheader("System Locale Information")
    current_locale = locale.getlocale()
    st.code(f"Current locale: {current_locale}")
    st.code(f"Default encoding: {locale.getpreferredencoding()}")

    # Try to set locale to UTF-8
    try:
        # Try different locale formats that might be available on the Linux system
        for loc in ['en_US.UTF-8', 'C.UTF-8', 'UTF-8']:
            try:
                locale.setlocale(locale.LC_ALL, loc)
                st.success(f"Successfully set locale to: {loc}")
                break
            except locale.Error:
                continue
    except Exception as e:
        st.error(f"Error setting locale: {e}")

    st.code(f"Locale after setting: {locale.getlocale()}")

with col2:
    st.subheader("Environment Variables")
    env_vars = {
        "LANG": os.environ.get("LANG", "Not set"),
        "LC_ALL": os.environ.get("LC_ALL", "Not set"),
        "LC_CTYPE": os.environ.get("LC_CTYPE", "Not set")
    }
    for key, value in env_vars.items():
        st.code(f"{key}: {value}")

# Display European characters
st.header("European Characters")

price = "€10.50"
st.write(f"The price is {price}")

french = "éèêëç"
st.write(f"French characters: {french}")

# Alternative with Unicode escape sequences
price_unicode = "\u20AC10.50"  # Euro symbol
st.write(f"Price with Unicode escape: {price_unicode}")

# Compare representations
st.header("Character Representations")
characters = {
    "Euro Symbol (direct)": "€",
    "Euro Symbol (unicode)": "\u20AC",
    "French accents": "éèêëç",
    "German umlauts": "äöüß",
    "Nordic characters": "åøæ"
}

for name, chars in characters.items():
    st.text(f"{name}: {chars}")
