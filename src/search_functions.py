import pandas as pd
import streamlit as st
from student_profile import show_profile

def student_search(student_list, student_class, student) :
    for _, row in student_list.iterrows():
            student_id = row['student_id']
            class_number = row['school_year']
            class_letter = row['classroom']
            class_fullname = class_number + class_letter
            student_first_name = row['first_name']
            student_last_name = row['last_name']
            if class_fullname == student_class:
                if student == '':
                      if st.button(student_first_name, key=student_id):
                            show_profile(student_first_name, student_last_name, student_id, class_fullname)
                
                elif student_first_name.lower() == student:
                        if st.button(student_first_name, key=student_id):
                            st.markdown("Funcionou")
                            show_profile(student_first_name, student_last_name, student_id, class_fullname)