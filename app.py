import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Modern Login",
    page_icon="🔐",
    layout="centered"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#4F46E5,#06B6D4,#3B82F6);
    background-size: 400% 400%;
}

/* Hide Streamlit Menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Login Card */
.login-card{
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(18px);
    padding:40px;
    border-radius:20px;
    box-shadow:0px 8px 30px rgba(0,0,0,0.3);
    border:1px solid rgba(255,255,255,0.2);
}

/* Title */
.title{
    text-align:center;
    color:white;
    font-size:42px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:white;
    margin-bottom:25px;
    font-size:18px;
}

/* Input Box */
.stTextInput>div>div>input{
    border-radius:10px;
    border:2px solid #ffffff;
    padding:12px;
    background:rgba(255,255,255,0.9);
}

/* Login Button */
.stButton>button{
    width:100%;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
    background:#00E676;
    color:black;
    border:none;
}

.stButton>button:hover{
    background:#00C853;
    color:white;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#111827;
}

section[data-testid="stSidebar"] *{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Sidebar ----------------
st.sidebar.title("📋 MENU")
st.sidebar.write("### Login Demo")
st.sidebar.info("Username: admin\n\nPassword: 1234")

# ---------------- Title ----------------
st.markdown('<h1 class="title">🔐 Secure Login</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Welcome Back! Please Login</p>', unsafe_allow_html=True)

# ---------------- Login Card ----------------
st.markdown('<div class="login-card">', unsafe_allow_html=True)

username = st.text_input("👤 Username")
password = st.text_input("🔑 Password", type="password")

login = st.button("🚀 LOGIN")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Login Logic ----------------
if login:
    if username == "admin" and password == "1234":
        st.success("✅ Login Successful!")
        st.balloons()
        st.markdown("## 🎉 Welcome Admin")
    else:
        st.error("❌ Invalid Username or Password")