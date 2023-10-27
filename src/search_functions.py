import pandas as pd
import streamlit as st
from student_profile import show_profile

def student_search(student_list, student_class, student) :
    for index, row in student_list.iterrows():
            id = row['student_id']
            serie = row['school_year']
            serie_tipo = row['classroom']
            real_serie = serie + serie_tipo
            first_name = row['first_name']
            last_name = row['last_name']
            if real_serie == student_class:
                if student == '':
                      if st.button(first_name, key=id):
                            show_profile(first_name, last_name, id, real_serie)
                
                elif first_name.lower() == student:
                        if st.button(first_name, key=id):
                            st.markdown("Funcionou")
                            show_profile(first_name, last_name, id, real_serie)