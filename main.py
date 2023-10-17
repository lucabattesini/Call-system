import pandas as pd
import streamlit as st
from datetime import datetime
from functions import compute_attendance, call_list_sum, side_bar, dateweek

st.set_page_config (layout="wide")

page = st.sidebar.radio('escolha', ['menu','seleção'])

def select() :
    attendance = pd.read_csv("./attendance_table.csv", encoding='UTF-8')
    student_list = pd.read_csv("./call_list_students_utf-8.csv", encoding="UTF-8")
    attendance.head()
    student_list.head()

    today = datetime.now()
    ftoday = today.strftime('%d/%m/%y')
    subject_list = ['Matemática','Inglês','Português','Química','Física','Biologia','Educação','Geografia','História','Sociologia','Filosofia']
    serie_list = ['1EMA', '2EMA', '3EMA', '1EMB', '2EMB', '3EMB']

    lista = dateweek(today)

    st.markdown("# Selecione uma turma e uma matéria")

    coluna, coluna1 = st.columns(2)

    with coluna:
        materia = st.selectbox("Matéria", subject_list)
    with coluna1:
        turma = st.selectbox("Turma", serie_list)

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

if page == 'seleção':
    select()