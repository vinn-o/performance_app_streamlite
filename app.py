import streamlit as st
from calculator import calculate_performance, get_results


student_name = st.text_input("Enter student name",
                             placeholder="full names")

attendance= st.number_input("Attendance percentage")

study_time = st.number_input("Study time per day")

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
    
    
st.title("Performance Calculator")

