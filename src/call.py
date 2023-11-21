import pandas as pd
import streamlit as st
from datetime import datetime
from call_functions import pages_sidebar
from utils import dateweek, get_attendance_df, get_students_df, classes_list, subjects_list

st.set_page_config (layout="wide")

def select_class_subject() :
    attendance = get_attendance_df()
    student_list = get_students_df()
    attendance.head()
    student_list.head()

    today = datetime.now()
    ftoday = today.strftime('%d/%m/%y')

    date_week = dateweek(today)

    st.markdown("# Selecione uma turma e uma matéria")

    coluna, coluna1 = st.columns(2)

    with coluna:
        subject = st.selectbox("Matéria", subjects_list)
    with coluna1:
        student_class = st.selectbox("Turma", classes_list)

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.header('Alunos')
    col2.header(date_week[0])
    col3.header(date_week[1])
    col4.header(date_week[2])
    col5.header(date_week[3])
    col6.header(date_week[4])
    st.markdown('---')

    pages_sidebar(attendance, student_list, ftoday, subject, subjects_list, dateweek, today, date_week, student_class)
    dateweek(today)
