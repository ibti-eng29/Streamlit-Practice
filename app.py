import streamlit as st

st.set_page_config(
    page_title="Login System",
    page_icon="🔐",
    layout="centered"
)

# ------------------ Custom CSS Theme ------------------
st.markdown("""
    <style>
        /* App background */
        .stApp {
            background: linear-gradient(135deg, #1f1c2c 0%, #928dab 100%);
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f0c29, #302b63, #24243e);
        }
        section[data-testid="stSidebar"] * {
            color: #f5f5f5 !important;
        }

        /* Card container */
        .login-card {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 18px;
            padding: 2.2rem 2.5rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
            margin-top: 1rem;
        }

        /* Titles */
        h1, h2, h3 {
            color: #ffffff !important;
            text-align: center;
        }

        /* Text inputs */
        .stTextInput input {
            background-color: rgba(255,255,255,0.12) !important;
            color: #ffffff !important;
            border-radius: 10px !important;
            border: 1px solid rgba(255,255,255,0.25) !important;
            padding: 0.6rem !important;
        }
        .stTextInput input::placeholder {
            color: #dddddd !important;
        }
        .stTextInput label {
            color: #f0f0f0 !important;
            font-weight: 500;
        }

        /* Buttons */
        div.stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #ff512f, #dd2476);
            color: white;
            font-weight: 600;
            border: none;
            border-radius: 10px;
            padding: 0.6rem 0;
            margin-top: 0.5rem;
            transition: all 0.25s ease-in-out;
        }
        div.stButton > button:hover {
            transform: scale(1.03);
            box-shadow: 0 0 15px rgba(221, 36, 118, 0.6);
        }

        /* Radio buttons in sidebar */
        div[role="radiogroup"] label {
            font-size: 1.05rem;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ Session State ------------------
if "users" not in st.session_state:
    st.session_state.users = {
        "admin": "1234"
    }

# ------------------ Title ------------------
st.markdown("<h1>🔐 Streamlit Login System</h1>", unsafe_allow_html=True)

# ------------------ Sidebar ------------------
st.sidebar.markdown("## 📋 Menu")
page = st.sidebar.radio(
    "Choose Option",
    ["Sign In", "Sign Up"]
)

st.sidebar.markdown("---")
st.sidebar.info("Demo login: **admin** / **1234**")

# ==================================================
# SIGN IN PAGE
# ==================================================
if page == "Sign In":

    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown("<h2>👋 Welcome Back</h2>", unsafe_allow_html=True)

    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    if st.button("Sign In 🚀"):

        if username in st.session_state.users:

            if st.session_state.users[username] == password:
                st.success("✅ Login Successful")
                st.markdown(f"### Welcome, **{username}**! 🎉")
                st.balloons()

            else:
                st.error("❌ Incorrect Password")

        else:
            st.error("⚠️ User Not Found")

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# SIGN UP PAGE
# ==================================================
elif page == "Sign Up":

    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown("<h2>📝 Create Account</h2>", unsafe_allow_html=True)

    new_username = st.text_input("Create Username", placeholder="Choose a username")
    new_password = st.text_input(
        "Create Password",
        type="password",
        placeholder="Choose a password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password",
        placeholder="Re-enter your password"
    )

    if st.button("Create Account ✨"):

        if new_username == "":
            st.warning("⚠️ Please enter username.")

        elif new_username in st.session_state.users:
            st.error("❌ Username already exists.")

        elif new_password != confirm_password:
            st.error("❌ Passwords do not match.")

        else:
            st.session_state.users[new_username] = new_password
            st.success("✅ Account Created Successfully!")
            st.write("Now go to **Sign In** and login. 🔑")

    st.markdown('</div>', unsafe_allow_html=True)