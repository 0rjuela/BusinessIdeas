import langchain_helper as lch
import streamlit as st

st.title ("Business ideas generator")

industry = st.sidebar.selectbox("What is the industry", ("fintech", "renewable energy", "educaytion"))
