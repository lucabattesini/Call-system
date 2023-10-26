import pandas as pd
import streamlit as st
from profile_1 import show_profile

def search_profile() :
    student_list = pd.read_csv("./call_list_students_utf-8.csv", encoding="UTF-8")
    subject_list = ['Matemática','Inglês','Português','Química','Física','Biologia','Educação','Geografia','História','Sociologia','Filosofia']
    serie_list = ['1EMA', '2EMA', '3EMA', '1EMB', '2EMB', '3EMB']

    st.markdown("### Pesquise o perfil do aluno utilizando as instruções abaixo")

    turma = st.selectbox("Selecione uma turma", serie_list)

    study_search = st.text_input("Pesquise pelo primeiro nome do aluno")


    for index, row in student_list.iterrows():
            id = row['student_id']
            serie = row['school_year']
            serie_tipo = row['classroom']
            real_serie = serie + serie_tipo
            first_name = row['first_name']
            last_name = row['last_name']
            if real_serie == turma:
                if study_search == '':
                      if st.button(first_name, key=id):
                            show_profile(first_name, last_name, id, real_serie)
                
                elif first_name.lower() == study_search:
                        if st.button(first_name, key=id):
                            st.markdown("Funcionou")
                            show_profile(first_name, last_name, id, real_serie)