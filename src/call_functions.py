import pandas as pd
import streamlit as st
import datetime as datetime

def call_list_buttons(attendance, student_list, fdata, materias, dateweek, today, lista, classes):
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
                    attendance = create_attendance(row, attendance, id, classes, materias, day)
                    
            with column3:
                day = lista[1]
                if st.button("Presente", key=f'{index}_presente' * 11):
                    attendance = create_attendance(row, attendance, id, classes, materias, day)
                    
            with column4:
                day = lista[2]
                if st.button("Presente", key=f'{index}_presente' * 13):
                    attendance = create_attendance(row, attendance, id, classes, materias, day)

            with column5:
                day = lista[3]
                if st.button("Presente", key=f'{index}_presente' * 17):
                    attendance = create_attendance(row, attendance, id, classes, materias, day)

            with column6:
                day = lista[4]
                if st.button("Presente", key=f'{index}_presente' * 23):
                    attendance = create_attendance(row, attendance, id, classes, materias, day)

            st.markdown('---')



def call_list_sum(attendance, student_list):
    for i, row in student_list.iterrows():
        id = row['student_id']
        x = 0

        for index, row2 in attendance.iterrows():
            id2 = row2['student_id']
            value = row2['attendance']
            if id == id2:
                if value == 1:
                  x = x + 1

        student_list.loc[student_list['student_id'] == id, 'attendance_total'] = x
    student_list.to_csv('./call_list_students_utf-8.csv', index=False)

def pages_sidebar(attendance, student_list, fdata, side, materias, dateweek, today, lista, classes):
    for subject in materias:
        if side == subject:
            call_list_buttons(attendance, student_list, fdata, subject, dateweek, today, lista, classes)
            if st.button("Salvar", key='ola'):
                call_list_sum(attendance, student_list)
                
                
# --- CREATE

def create_attendance(row, attendance, student_id, class_id, subject_id, date):

    row = pd.DataFrame({'student_id': [student_id],'attendance': [1],'date': [date], 'subject': [subject_id], 'class': [class_id]})
    attendance = pd.concat([attendance, row], axis=0, ignore_index=True)
    attendance.to_csv('./db/attendance.csv', index=False)
    # Verificar se essas informações existem se não retorna erro
    # Inserir uma linha com esses registros em attendance
    # retorna a attendance
    return attendance

# --- READ (get)

def get_attendances_by_student(student_id, date=None):
    student_csv = pd.read_csv("./db/students_utf-8.csv", encoding="UTF-8")
    student_list = []
    for row in student_csv.iterrows():
        first_name = student_csv['first_tname']
        last_name = student_csv['last_tname']
        name = first_name + last_name
        student_list.append(name)
    # Verificar se essas informações existem se não retorna erro
    # Procurar no csv por attendences para esse student nessas datas
    # retorna a lista com o resultado
    return student_list

# Criar outras funções para trazer a lista de várias attendances por:
    # Class -> get_attendances_by_class
    # Subject -> get_attendances_by_subject
    # Date -> get_attendances_by_date
    
# --- UPDATE

# * Precisa fazer com que attendance tenha um identificador único

def update_attendance(id, new_call_value, subject=None):
    # Verificar se essa attendance existe, se não retorna erro
    # Sobrescrever as informações com a informação nova
    # Verificar se subject é None, se sim, não sobrescrever informação
    # retornar a attendance atualizada
    return 

# --- DELETE

def delete_attendace(id):
    # Verificar se essa attendance existe, se não retorna erro
    # deletar a linha com o id
    # retornar a attendance deletada
    return