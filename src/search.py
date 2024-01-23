import streamlit as st
from search_functions import student_search

def search_profile() :

    study_search = st.text_input("Insira o nome completo do aluno")

    student_search(study_search)
