import streamlit as st
from search import search_profile
from call import select_class_subject
from menu import menu

page = st.sidebar.radio('Paginas', ['Menu','Chamada', 'Perfil do aluno'])

if page == 'Menu':
    menu()

if page == 'Chamada':
    select_class_subject()

if page == 'Perfil do aluno':
    search_profile()