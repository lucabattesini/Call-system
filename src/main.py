import streamlit as st
from search import search_profile
from call import select_class_subject
from menu import menu
from notes import student_search
from utils import subjects_list

page = st.sidebar.radio('Paginas', ['Menu','Chamada', 'Perfil do aluno',  'Anotações'])

if page == 'Menu':
    menu()

if page == 'Chamada':
    select_class_subject()

if page == 'Perfil do aluno':
    search_profile()

if page == 'Anotações':
    subject = st.selectbox('Escolha uma matéria', subjects_list)
    name = st.text_input("Nome do aluno")
    student_search(name)