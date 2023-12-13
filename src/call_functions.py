import pandas as pd
import streamlit as st
import datetime as datetime
from utils import subjects_list
from db.connection import get_attendance_df, save_attendance_df, save_students_summary_df

def call_list_buttons(attendance, student_list, materias, lista, classes):
    for index, row in student_list.iterrows():
        id = row['student_id']
        first_name = row['first_name']
        last_name = row['last_name']
        serie = row['school_year']
        serie_tipo = row['classroom']
        real_serie = serie + serie_tipo

        column1, column2, column3, column4, column5, column6 = st.columns(6)
        if real_serie == classes:
            with column1:
                st.markdown(f"### {first_name} {last_name}")

            with column2:
                day = lista[0]
                if st.button("Presente", key=f'{index}_presente'):
                    attendance = create_attendance(row, attendance, id, classes, materias, day, 1, 0)
                elif st.button("Ausent", key=f'{index}_ausente'):
                    attendance = create_attendance(row, attendance, id, classes, materias, day, 0, 1)
                    
            with column3:
                day = lista[1]
                if st.button("Presente", key=f'{index}_presente' * 11):
                    attendance = create_attendance(row, attendance, id, classes, materias, day, 1, 0)
                elif st.button("Ausent", key=f'{index}_ausente' * 11):
                    attendance = create_attendance(row, attendance, id, classes, materias, day, 0, 1)
                    
            with column4:
                day = lista[2]
                if st.button("Presente", key=f'{index}_presente' * 13):
                    attendance = create_attendance(row, attendance, id, classes, materias, day, 1, 0)
                elif st.button("Ausent", key=f'{index}_ausente' * 13):
                    attendance = create_attendance(row, attendance, id, classes, materias, day, 0, 1)

            with column5:
                day = lista[3]
                if st.button("Presente", key=f'{index}_presente' * 17):
                    attendance = create_attendance(row, attendance, id, classes, materias, day, 1, 0)
                elif st.button("Ausent", key=f'{index}_ausente' * 17):
                    attendance = create_attendance(row, attendance, id, classes, materias, day, 0, 1)

            with column6:
                day = lista[4]
                if st.button("Presente", key=f'{index}_presente' * 23):
                    attendance = create_attendance(row, attendance, id, classes, materias, day, 1, 0)
                elif st.button("Ausent", key=f'{index}_ausente' * 23):
                    attendance = create_attendance(row, attendance, id, classes, materias, day, 0, 1)

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

def create_attendance(row, attendance, student_id, class_id, subject_id, date, present, absent):
    """Create a new line to attendance

    Returns:
    The new line of attendance

   """
    row = pd.DataFrame({'student_id': [student_id],'present': [present],'absent': [absent],'date': [date], 'subject': [subject_id], 'class': [class_id]})
    attendance = pd.concat([attendance, row], axis=0, ignore_index=True)
    save_attendance_df(attendance)
    #if 'oi' == 'ola':
        #raise 'erro: estudante não existe'

    # Verificar se essas informações existem se não retorna erro
    # Inserir uma linha com esses registros em attendance
    # retorna a attendance
    return attendance

# --- READ (get)

def get_attendances_by_student(id, date=None):
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

def get_students_by_date(chosen_date): #x
    attendance_csv = get_attendance_df()
    student_list_by_date = []
    for row in attendance_csv.iterrows():
        student_id = attendance_csv['student_id']
        date_saved = attendance_csv['date']
        if chosen_date == date_saved:
            return row      
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