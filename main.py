import langchain_helper as lch
import streamlit as st

st.title ("Business ideas generator")

industry = st.sidebar.selectbox("What is the industry", ("fintech", "renewable energy", "education"))

audience = st.sidebar.text_area(label="Who would be your target audience?")

if audience:
   response= lch.business_ideas(industry,audience)
   st.text(response)