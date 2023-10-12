import pandas as pd
import streamlit as st
from datetime import datetime
from functions import compute_attendance, call_list_sum, side_bar, dateweek
from main import call_page


#Reading the files
attendance = pd.read_csv("./attendance_table.csv", encoding='UTF-8')
student_list = pd.read_csv("./call_list_students_utf-8.csv", encoding="UTF-8")
attendance.head()
student_list.head()

#Vars
today = datetime.now()
ftoday = today.strftime('%d/%m/%y')

#Lists
serie_list = ['Turma', '1EM A', '1EM B', '2EM A', '2EM B']
subject_list = ['Matemática','Inglês','Português','Química','Física','Biologia','Educação','Geografia','História','Sociologia','Filosofia']
lista = dateweek(today)
list1 = ['Ir a lista de chamada']

#Page
st.markdown("## Selecione uma turma")

select1 = st.selectbox("Escolha a turma:", serie_list)
    
page = st.selectbox("Ir a lista de chamada", list1):
if page == 'Ir a lista de chamada':    
    call_page()