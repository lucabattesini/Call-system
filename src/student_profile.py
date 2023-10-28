import streamlit as st
import pandas as pd

def show_profile(first_name, last_name, student_class) :
    column, column2 = st.columns(2)
    aluno = first_name + ' ' + last_name
    with column:
        st.markdown(f'# {aluno}')
    with column:
        st.markdown(f'# {student_class}')
    notes = st.text_input("Anotações")

# --- READ (get)

def get_students(classId):
    # procura todos os estudantes de uma turma específica
    # retorna a lista de estudantes
    return []

def get_student(id):
    student = { 'name': "", 'grade': 0, 'attendance': [], 'total_attendance_per_class': []}
    # procura o estudante com o id passado
    # preenche no dicionário student os campos certos
    return student