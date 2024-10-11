import streamlit as st
import lang

st.title("Blog Generator")
st.header("Enter the topic and blog title")
content = st.text_input("Topic", )
blog_title = st.text_input("Blog Title",)