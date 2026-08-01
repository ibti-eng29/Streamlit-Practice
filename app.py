import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Login Page",
    page_icon="🔐",
    layout="centered"
)

# ---------------- Sidebar ----------------
st.sidebar.title("📌 Menu")
st.sidebar.write("### Welcome!")
st.sidebar.info("Please login to access the dashboard.")

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.login-box{
    background-color: white;
    padding: 35px;
    border-radius: 15px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
}
h1{
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.title("🔐 Streamlit Login System")
st.write("### Welcome Back 👋")
st.write("Please enter your username and password.")

# ---------------- Login Form ----------------
with st.container():
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    username = st.text_input("👤 Username", placeholder="Enter Username")
    password = st.text_input(
        "🔑 Password",
        type="password",
        placeholder="Enter Password"
    )

    login = st.button("🚀 Login", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Login Logic ----------------
if login:
    if username == "admin" and password == "1234":
        st.success("✅ Login Successful!")
        st.balloons()
        st.write(f"## 🎉 Welcome, **{username}**")
    else:
        st.error("❌ Invalid Username or Password")