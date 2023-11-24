import streamlit as st
import pandas as pd
from db_connection import get_students_df

df = get_students_df()

def show_profile(first_name, last_name, student_class) :
    column, column2 = st.columns(2)
    aluno = first_name + ' ' + last_name
    with column:
        st.markdown(f'# {aluno}')
    with column:
        st.markdown(f'# {student_class}')

# --- READ (get)

def get_students(classId):
    # procura todos os estudantes de uma turma específica
    # retorna a lista de estudantes
    return []

def get_student(id):
    for students in df.iterrows() :
        student_first_name = students['first_name']
        student_last_name = students['last_name']
        student_name = student_first_name + ' ' + student_last_name
        student_attendance = students['attendance_total']
        student = { 'name': [student_name], 'grade': 0, 'attendance': [student_attendance], 'total_attendance_per_class': []}

    # procura o estudante com o id passado
    # preenche no dicionário student os campos certos
    return student

