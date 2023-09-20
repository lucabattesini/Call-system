import pandas as pd
import streamlit as st
import datetime as datetime

def compute_attendance(attendance, student_list, fdata, materias):
    for index, row in student_list.iterrows():
        id = row['student_id']
        first_name = row['first_name']
        last_name = row['last_name']
        column1, column2 = st.columns(2)
        with column1:
            st.markdown(f"### {first_name} {last_name}")

        with column2:
            if st.button("Presente", key=f'{index}_presente'):
                row = pd.DataFrame({'student_id': [id],'attendance': [1],'date': [fdata], 'subject': [materias]})
                attendance = pd.concat([attendance, row], axis=0, ignore_index=True)

            if st.button("Ausente", key=f'{index}_ausente'):
                row = pd.DataFrame({'student_id': [id], 'attendance': [0],'date': [fdata], 'subject': [materias]})
                attendance = pd.concat([attendance, row], axis=0, ignore_index=True)
        st.markdown('---')
    attendance.to_csv('./attendance_table.csv', index=False)

def call_list_sum(attendance, student_list):
    for i, row in student_list.iterrows():
        id = row['student_id']
        print(id)
        x = 0
        for index, row2 in attendance.iterrows():
            id2 = row2['student_id']
            value = row2['attendance']
            if id == id2:
                if value == 1:
                  x = x + 1
        student_list.loc[student_list['student_id'] == id, 'attendance_total'] = x
    student_list.to_csv('./call_list_students_utf-8.csv', index=False)
    print(id2)

def side_bar(attendance, student_list, fdata, side, materias):
    for subject in materias:
        if side == subject:
            compute_attendance(attendance, student_list, fdata, subject)
            if st.button("Contar", key='ola'):
                call_list_sum(attendance, student_list)

def dateweek(fdata) :
    week_day = fdata.weekday()
    week_start = fdata - datetime.timedelta(days=week_day)
    week_end = week_start + datetime.timedelta(days=6)
    temporary_list = [1, 2, 3, 4, 5, 6, 7]
    day = 0
    week_days = []
    formated_week_days = []
    for n in temporary_list:
        delta = datetime.timedelta(days=day)
        new_date = week_start + delta
        week_days.append(new_date)
        day = day + 1
    for data in week_days:
        especific_week_day = data.strftime('%d/%m/%y')
        formated_week_days.append(especific_week_day)