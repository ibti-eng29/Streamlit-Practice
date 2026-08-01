import streamlit as st

st.set_page_config(page_title="Login Page", page_icon="🔐", layout="wide")

st.title("Streamlit Practice")

st.sidebar.title("Menu")
st.sidebar.header("Login Pages")
st.sidebar.write("Please login to continue.")

st.header(" Login Page")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("✅ Login Successful!")
        st.write(f"Welcome, {username}")
    else:
        st.error("❌ Invalid Username or Password")