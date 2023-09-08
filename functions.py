import pandas as pd
import streamlit as st

<<<<<<< HEAD
def call_function(df, df2) :
    x = int(1)
    x1 = 'a'
    data = datetime.now()
    fdata = data.strftime('%d/%m/%y')
    for index, row in df2.iterrows():
=======
def compute_attendance(attendance, student_list, fdata):
    for index, row in student_list.iterrows():
>>>>>>> 5a060d70602e4a8b3e1244565835d7e0aa03baa4
        id = row['student_id']
        first_name = row['first_name']
        last_name = row['last_name']

        st.markdown(f"### {first_name} {last_name}")

        if st.button("Presente", key=f'{index}_Presente'):
            row = pd.DataFrame({'student_id': [id],'attendance': [1],'date': [fdata]})
            attendance = pd.concat([attendance, row], axis=0, ignore_index=True)

<<<<<<< HEAD
        if st.button("Ausente", key=x1):
            df.loc[index] = {'student_id': id, 'attendance_total': 0, 'date': fdata}
            df2.loc[df2['student_id']==id, 'attendance_total'] += 0
            df2.loc[df2['student_id']==id, 'date'] = fdata
            df.to_csv('./attendance_table.csv', index=False)
        df2.to_csv('./call_list_students_utf-8.csv', index=False)
=======
        if st.button("Ausente", key=f'{index}_Ausente'):
            row = pd.DataFrame({'student_id': [id], 'attendance': [0],'date': [fdata]})
            attendance = pd.concat([attendance, row], axis=0, ignore_index=True)
        
    attendance.to_csv('./attendance_table.csv', index=False)
>>>>>>> 5a060d70602e4a8b3e1244565835d7e0aa03baa4
