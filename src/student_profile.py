import streamlit as st
from db.connection import get_students_df, get_attendance_df

def show_profile(student_name, student_class) :
    column, column2 = st.columns(2)
    with column:
        st.markdown(f'### {student_name}')
    with column2:
        st.markdown(f'### {student_class}')