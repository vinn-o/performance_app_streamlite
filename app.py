import streamlit as st
from calculator import calculate_performance, get_results




st.set_page_config(
    page_title="Performance evaluator",
    page_icon = "📚",
)



st.title("Performance Calculator")


student_name = st.text_input("Enter student name",
                             placeholder="full names")

attendance= st.number_input("Attendance percentage",
                            min_value=1,
                            max_value=10,
                            value=1
                            )

study_time = st.number_input("Study time per day",
                            min_value=1,
                            max_value=10,
                            value=1
                            )
                

assignment = st.number_input("Enter assignment score",
                            min_value=1,
                            max_value=100,
                            value=1
                            )



with st.sidebar:
    st.header("Dashbard")
    st.selectbox("Semester under review",
                 (1, 2),
                 index=None,
                 placeholder="Semester")
    
    
button = st.button("Compute")

