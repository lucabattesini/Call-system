import pandas as pd
import streamlit as st
from search_functions import student_search

def search_profile() :
    student_list = pd.read_csv("./call_list_students_utf-8.csv", encoding="UTF-8")
    subject_list = ['Matemática','Inglês','Português','Química','Física','Biologia','Educação','Geografia','História','Sociologia','Filosofia']
    serie_list = ['1EMA', '2EMA', '3EMA', '1EMB', '2EMB', '3EMB']

    st.markdown("### Pesquise o perfil do aluno utilizando as instruções abaixo")

    turma = st.selectbox("Selecione uma turma", serie_list)

    study_search = st.text_input("Pesquise pelo primeiro nome do aluno")


    student_search(student_list, serie_list, study_search)