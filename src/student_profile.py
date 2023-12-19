import streamlit as st
import pandas as pd
from db.connection import get_students_df

def show_profile(first_name, last_name, student_class) :
    column, column2 = st.columns(2)
    aluno = first_name + ' ' + last_name
    with column:
        st.markdown(f'# {aluno}')
    with column:
        st.markdown(f'# {student_class}')

# --- READ (get)

def get_students(classId):
    df = get_students_df()
    students_from_class = []
    for i, row in df.iterrows:
        year =  row['school_year']
        classroom = row['classroom']
        class_name = year + classroom
        first_name = row['first_name']
        last_name = row['last_name']
        name = first_name + last_name
        if classId == class_name:
            students_from_class.append(name)
    # procura todos os estudantes de uma turma específica
    # retorna a lista de estudantes
    return students_from_class

def get_student(id):
    student = { 'name': "", 'grade': 0, 'attendance': [], 'total_attendance_per_class': []}
    # procura o estudante com o id passado
    # preenche no dicionário student os campos certos
    return student

