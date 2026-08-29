import streamlit as st
from calculator import calculate_performance, get_results

st.set_page_config(
    page_title="Performance evaluator",
    page_icon = "📚",
)

with st.sidebar:
    st.header("Dashbard")
    st.selectbox("Semester under review",
                 (1, 2),
                 index=None,
                 placeholder="Semester")
    
    


