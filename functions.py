import pandas as pd
import streamlit as st

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