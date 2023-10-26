import pandas as pd
import streamlit as st
from datetime import datetime
from functions import call_list_buttons, call_list_sum, pages_sidebar, dateweek

st.set_page_config (layout="wide")

def select_class_subject() :
    attendance = pd.read_csv("./db/attendance.csv", encoding='UTF-8')
    student_list = pd.read_csv("./db/student_info_utf-8.csv", encoding="UTF-8")
    attendance.head()
    student_list.head()

    today = datetime.now()
    ftoday = today.strftime('%d/%m/%y')
    subject_list = ['Matemática','Inglês','Português','Química','Física','Biologia','Educação','Geografia','História','Sociologia','Filosofia']
    serie_list = ['1EMA', '2EMA', '3EMA', '1EMB', '2EMB', '3EMB']

    date_week = dateweek(today)

    st.markdown("# Selecione uma turma e uma matéria")

    coluna, coluna1 = st.columns(2)

    with coluna:
        subject = st.selectbox("Matéria", subject_list)
    with coluna1:
        student_class = st.selectbox("Turma", serie_list)

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.header('Alunos')
    col2.header(date_week[0])
    col3.header(date_week[1])
    col4.header(date_week[2])
    col5.header(date_week[3])
    col6.header(date_week[4])
    st.markdown('---')

    pages_sidebar(attendance, student_list, ftoday, subject, subject_list, dateweek, today, date_week, student_class)
    dateweek(today)
