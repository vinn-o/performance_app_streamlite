import streamlit as st
from calculator import calculate_performance, get_results




st.set_page_config(
    page_title="Performance evaluator",
    page_icon = "📚",
)



st.title("Performance Calculator")
st.divider()

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
    st.image("jet_logo.jpeg",
             width=90,
             )
    st.selectbox("Semester under review",
                 (1, 2),
                 index=None,
                 placeholder="Semester")
    
    
if st.button("Compute"):
    if student_name == "":
        st.warning("Enter name")
    else:

        st.write(f"Results for {student_name}")
        score = calculate_performance(assignment, study_time, attendance)
        results = get_results(score)
        st.metric(f"Scores",
                  f"{score}")

        if results == "PASS":
            st.success(f"Great job 🎉 {student_name}")
        else:
            st.warning(f"Improve more ⚠️⚠️ {student_name}")

        

