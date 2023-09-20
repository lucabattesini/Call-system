import pandas as pd
import streamlit as st
from datetime import datetime
from functions import compute_attendance, call_list_sum, side_bar, dateweek
 
attendance = pd.read_csv("./attendance_table.csv", encoding='UTF-8')
student_list = pd.read_csv("./call_list_students_utf-8.csv", encoding="UTF-8")
attendance.head()
student_list.head()

today = datetime.now()
ftoday = today.strftime('%d/%m/%y')
subject_list = ['Matemática','Inglês','Português','Química','Física','Biologia','Educação','Geografia','História','Sociologia','Filosofia']
sidebar = st.sidebar.selectbox("Selecione uma matéria", subject_list)

col1, col2 = st.columns(2)
col1.title('Alunos')
col2.title('Presença')

with col1:
    st.markdown('')
with col2:
    st.markdown('')

st.markdown('---')

side_bar(attendance, student_list, ftoday, sidebar, subject_list)

dateweek(today)
#print(df)
#print(df2)