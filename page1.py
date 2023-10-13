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
lista = dateweek(today)


#Page
st.markdown("# Selecione uma turma e uma matéria na barra lateral")



call_page()