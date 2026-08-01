import streamlit as st

st.set_page_config(
    page_title="Login System",
    page_icon="🔐",
    layout="wide"
)

# ------------------ Session State ------------------
if "users" not in st.session_state:
    st.session_state.users = {
        "admin": "1234"
    }

# ------------------ Title ------------------
st.title("🔐 Streamlit Practice")

# ------------------ Sidebar ------------------
st.sidebar.title("📋 Menu")
page = st.sidebar.radio(
    "Choose Option",
    ["🔑 Sign In", "📝 Sign Up"]
)

# ==================================================
# SIGN IN PAGE
# ==================================================
if page == "🔑 Sign In":

    st.header("🔑 Sign In")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):

        if username in st.session_state.users:

            if st.session_state.users[username] == password:
                st.success("✅ Login Successful")
                st.write(f"### Welcome, {username} 👋")
                st.balloons()

            else:
                st.error("❌ Incorrect Password")

        else:
            st.error("❌ User Not Found")

# ==================================================
# SIGN UP PAGE
# ==================================================
elif page == "📝 Sign Up":

    st.header("📝 Sign Up")

    new_username = st.text_input("Create Username")
    new_password = st.text_input(
        "Create Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("Create Account"):

        if new_username == "":
            st.warning("Please enter username.")

        elif new_username in st.session_state.users:
            st.error("Username already exists.")

        elif new_password != confirm_password:
            st.error("Passwords do not match.")

        else:
            st.session_state.users[new_username] = new_password
            st.success("✅ Account Created Successfully!")
            st.write("Now go to **Sign In** and login.")