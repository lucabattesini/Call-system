import streamlit as st
from student_profile import show_profile
from db.connection import get_students_df

def student_search(id) :
    df  = get_students_df()
    for _, row in df.iterrows():
            student_id = row['student_id']
            student_first_name = row['first_name']
            student_last_name = row['last_name']
            year_class = row['school_year']
            class_name = row['classroom']
            class_full_name = year_class + class_name

            if student_id == id:
                    show_profile(student_first_name, student_last_name, class_full_name)