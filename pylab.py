import streamlit as st

st.title("Welcome to My Streamlit App!")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello, **{name}**!")
