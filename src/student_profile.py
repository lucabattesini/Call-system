import streamlit as st
import pandas as pd
from db.connection import get_students_df, get_attendance_df


def show_profile(student_name, student_class) :
    column, column2 = st.columns(2)
    with column:
        st.markdown(f'### {student_name}')
    with column2:
        st.markdown(f'### {student_class}')


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
    students = get_students_df
    attendance = get_attendance_df
    student = { 'name': "", 'grade': 0, 'attendance': [], 'total_attendance_per_class': []}
    for row in student.iterrows():
        student_id = row['student_id']
        first_name = row['first_name']
        last_name = row['last_name']
        name = first_name + last_name
        year = row['school_year']
        classes = row['classroom']
        classroom = year + classes
        if student_id == id:
            for row2 in attendance.iterrows():
                    student_id2 = row2['student_id']
                    attendance = row2['attendance']
                    attendance_total = 0
                    if student_id2 == id:
                        if attendance == 1:
                            attendance_total += 1
            student = { 'name': name, 'grade': classroom, 'attendance': attendance_total, 'total_attendance_per_class': []}                       
                    
    # procura o estudante com o id passado
    # preenche no dicionário student os campos certos
    return student

