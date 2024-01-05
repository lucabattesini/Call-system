import streamlit as st
from db.connection import get_students_df
from student_functions import create_student_note
from utils import subjects_list

subject = st.selectbox('Escolha uma matéria', subjects_list)
name = st.text_input("Nome do aluno")

def student_search(name) :
    df  = get_students_df()
    for _, row in df.iterrows():
        student_id = row['student_id']
        student_first_name = row['first_name']
        student_last_name = row['last_name']
        student_name = student_first_name + " " + student_last_name
        year_class = row['school_year']
        class_name = row['classroom']
        class_full_name = year_class + class_name
        student_name_lower = student_name.lower()
        input_student_name_lower = name.lower()
        if student_name_lower == input_student_name_lower:
            if st.button(f"### {student_name}  -  {class_full_name}"):
                note = st.text_input("DIgite a anotação")
                create_student_note(note, subject, student_id)