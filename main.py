import pandas as pd
import streamlit as st
from datetime import datetime
from functions import compute_attendance, call_list_sum, side_bar, dateweek

st.set_page_config (layout="wide")

def call_page() :
    attendance = pd.read_csv("./attendance_table.csv", encoding='UTF-8')
    student_list = pd.read_csv("./call_list_students_utf-8.csv", encoding="UTF-8")
    attendance.head()
    student_list.head()

    today = datetime.now()
    ftoday = today.strftime('%d/%m/%y')
    subject_list = ['Matemática','Inglês','Português','Química','Física','Biologia','Educação','Geografia','História','Sociologia','Filosofia']
    serie_list = ['1EMA', '2EMA', '3EMA', '1EMB', '2EMB', '3EMB']


    st.sidebar.header("Escolha uma matéria e uma turma")
    materia = st.sidebar.selectbox("Matéria", subject_list)
    turma = st.sidebar.selectbox("Turma", serie_list)
    lista = dateweek(today)

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.header('Alunos')
    col2.header(lista[0])
    col3.header(lista[1])
    col4.header(lista[2])
    col5.header(lista[3])
    col6.header(lista[4])
    st.markdown('---')

    side_bar(attendance, student_list, ftoday, materia, subject_list, dateweek, today, lista, turma)
    dateweek(today)