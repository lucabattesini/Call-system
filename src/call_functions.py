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
                
def create_attendance(row, presence, attendance, student_id, class_id, subject_id, date):

    row = pd.DataFrame({'student_id': [student_id],'attendance': [presence],'date': [date], 'subject': [subject_id], 'class': [class_id]})
    attendance = pd.concat([attendance, row], axis=0, ignore_index=True)
    save_attendance_df(attendance)

    return attendance