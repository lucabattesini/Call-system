import pandas as pd
import streamlit as st

def compute_attendance(attendance, student_list, fdata):
    for index, row in student_list.iterrows():
        id = row['student_id']
        first_name = row['first_name']
        last_name = row['last_name']

        st.markdown(f"### {first_name} {last_name}")

        if st.button("Presente", key=f'{index}_Presente'):
            row = pd.DataFrame({'student_id': [id],'attendance': [1],'date': [fdata]})
            attendance = pd.concat([attendance, row], axis=0, ignore_index=True)

        if st.button("Ausente", key=f'{index}_Ausente'):
            row = pd.DataFrame({'student_id': [id], 'attendance': [0],'date': [fdata]})
            attendance = pd.concat([attendance, row], axis=0, ignore_index=True)

    attendance.to_csv('./attendance_table.csv', index=False)

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
        
        print(x)