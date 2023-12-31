import pandas as pd
import streamlit as st
import datetime as datetime
from utils import subjects_list
from db.connection import get_attendance_df, save_attendance_df, save_students_summary_df

def call_list_buttons(attendance, student_list, materias, today, classes):
    for index, row in student_list.iterrows():
        id = row['student_id']
        first_name = row['first_name']
        last_name = row['last_name']
        serie = row['school_year']
        serie_tipo = row['classroom']
        real_serie = serie + serie_tipo

        column1, column2 = st.columns(2)
        if real_serie == classes:
            with column1:
                st.markdown(f"### {first_name} {last_name}")

            with column2:
                if st.button("Presente", key=f'{index}_presente'):
                    attendance = create_attendance(row, 1, attendance, id, classes, materias, today)
                
                if st.button("Ausente", key=f'{index}_ausente'):
                    attendance = create_attendance(row, 0, attendance, id, classes, materias, today)

            st.markdown('---')



def call_list_sum(attendance, student_list):
    for _, row in student_list.iterrows():
        id = row['student_id']
        x = 0

        for _, row2 in attendance.iterrows():
            id2 = row2['student_id']
            value = row2['present']
            if id == id2:
                if value == 1:
                  x =+ 1
        for _, row2 in attendance.iterrows():
            id2 = row2['student_id']
            value = row2['absent']
            if id == id2:
                if value == 1:
                  y =+ 1

        student_list.loc[student_list['student_id'] == id, 'attendance_total'] = x - y
        save_students_summary_df(student_list)

def pages_sidebar(attendance, student_list, subject, lista, classes):
    for sub in subjects_list:
        if subject == sub:
            call_list_buttons(attendance, student_list, sub, lista, classes)
            if st.button("Salvar", key='ola'):
                call_list_sum(attendance, student_list)
                
                
# --- CREATE
def create_attendance(row, presence, attendance, student_id, class_id, subject_id, date):
    """Create a new line to attendance

    Returns:
    The new line of attendance

   """
    row = pd.DataFrame({'student_id': [student_id],'attendance': [presence],'date': [date], 'subject': [subject_id], 'class': [class_id]})
    attendance = pd.concat([attendance, row], axis=0, ignore_index=True)
    save_attendance_df(attendance)

    return attendance

# --- READ (get)

def get_attendances_by_student(id):
    student_csv = get_attendance_df()
    attenddance_list = []
    for _ in student_csv.iterrows():
        student_id = student_csv['student_id']
        if student_id == id:
            student_attendance = student_csv['attendance_total']
            attenddance_list.append(student_attendance)
    
    # Verificar se essas informações existem se não retorna erro
    # Procurar no csv por attendences para esse student nessas datas
    # retorna a lista com o resultado
    return attenddance_list

def get_students_by_class(class_name): 
    attendance_csv = get_attendance_df()
    student_list_by_class = []
    for _, row in attendance_csv.iterrows():
        student_class = row['class']
        if class_name == student_class:
            student_list_by_class.append(row)
    return student_list_by_class

def get_students_by_subject(subject_name): 
    attendance_csv = get_attendance_df()
    student_list_by_subject = []
    for _, row in attendance_csv.iterrows():
        student_subject = attendance_csv['subject']
        if subject_name == student_subject:
            student_list_by_subject.append(row)
    return student_list_by_subject

def get_students_by_date(chosen_date): 
    attendance_csv = get_attendance_df()
    student_list_by_date = []
    for row in attendance_csv.iterrows():
        date_saved = attendance_csv['date']
        if chosen_date == date_saved:
            student_list_by_date.append(row)
    return student_list_by_date

def get_students_by_subject(chosen_subject): 
    attendance_csv = get_attendance_df()
    student_list_by_subject = []
    for row in attendance_csv.iterrows():
        subject = attendance_csv['subject']
        if chosen_subject == subject:
            student_list_by_subject.append(row)
    return student_list_by_subject

def get_students_by_class(chosen_class): 
    attendance_csv = get_attendance_df()
    student_list_by_class = []
    for row in attendance_csv.iterrows():
        student_class = attendance_csv['class']
        if chosen_class == student_class:
            student_list_by_class.append(row)
    return student_list_by_class

#Criar outras funções para trazer a lista de várias attendances por:
    # Class -> get_attendances_by_class
    # Subject -> get_attendances_by_subject
    # Date -> get_attendances_by_date
    
# --- UPDATE

# * Precisa fazer com que attendance tenha um identificador único 
def attendance(student_list, id, new_call_value, subject=None) : 
    for _ in student_list.iterrows:
        student_id = student_list['student_id']
        if student_id == id:
            new_line = {'attendance_total': new_call_value, }
            student_list.loc[id] = new_line
            student_list.to_csv('')

#def update_attendance(id, new_call_value, subject=None):
    """Atualizar a linha de um attendance que já existe

    Função: sobrescrever e salvar
    """
    # Verificar se essa attendance existe, se não retorna erro
    # Sobrescrever as informações com a informação nova
    # Verificar se subject é None, se sim, não sobrescrever informação
    # retornar a attendance atualizada
def delete_attendace(id):
    counter = 0
    attendance_csv = get_attendance_df() 
    for row in attendance_csv.iterrows():
        row_id = attendance_csv['student_id']
        if id == row_id:
            attendance_csv.drop([counter], axis=0, inplace=True)
            return row
        counter += 1

#Refazer a função com base no id por linha do attendance.csv