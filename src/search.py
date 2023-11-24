import pandas as pd
import streamlit as st
from search_functions import student_search
from utils import classes_list
from db.connection import get_students_df

def search_profile() :
    student_list = get_students_df()

    st.markdown("### Pesquise o perfil do aluno utilizando as instruções abaixo")

    st.selectbox("Selecione uma turma", classes_list)

    study_search = st.text_input("Pesquise pelo primeiro nome do aluno")

    student_search(student_list, classes_list, study_search)