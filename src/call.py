import streamlit as st
from datetime import datetime
from call_functions import pages_sidebar
from utils import dateweek, classes_list, subjects_list
from db.connection import get_attendance_df, get_students_df

st.set_page_config (layout="wide")

def select_class_subject() :
    attendance = get_attendance_df()
    student_list = get_students_df()
    attendance.head()
    student_list.head()

    today = datetime.now()
    ftoday = today.strftime('%d/%m/%y')

    st.markdown("# Selecione uma turma e uma matéria")
    coluna, coluna1 = st.columns(2)

    with coluna:
        subject = st.selectbox("Matéria", subjects_list)
    with coluna1:
        student_class = st.selectbox("Turma", classes_list)

    col1, col2 = st.columns(2)

    col1.header('Alunos')
    col2.header(ftoday)
    st.markdown('---')

    dateweek(today)
    pages_sidebar(attendance, student_list, subject, ftoday, student_class)