import streamlit as st

st.set_page_config(
    page_title="Login System",
    page_icon="🔐",
    layout="wide"
)

# -------------------------
# Session State
# -------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------------
# Title
# -------------------------
st.title("🔐 Streamlit Login System")

# -------------------------
# Sidebar
# -------------------------
st.sidebar.title("📋 Menu")

menu = st.sidebar.radio(
    "Select Option",
    ["🔑 Login", "🚪 Logout"]
)

# =========================
# LOGIN PAGE
# =========================
if menu == "🔑 Login":

    st.header("🔑 Login Form")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "1234":

            st.session_state.logged_in = True

            st.success("✅ Login Successful!")
            st.balloons()

        else:
            st.error("❌ Invalid Username or Password")

    if st.session_state.logged_in:
        st.info("👋 Welcome Admin!")
        st.write("You are currently logged in.")

# =========================
# LOGOUT PAGE
# =========================
elif menu == "🚪 Logout":

    st.header("🚪 Logout")

    if st.session_state.logged_in:

        st.success("✅ You are currently logged in.")

        if st.button("Logout"):

            st.session_state.logged_in = False

            st.warning("👋 Logged Out Successfully!")

    else:
        st.info("ℹ️ You are already logged out.")