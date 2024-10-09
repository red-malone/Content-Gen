import streamlit as st
import lang

st.title("Website Generator")
st.header("Enter the content of the website")
content = st.text_area("Content", height=200)