import streamlit as st
import pandas as pd
from search import perfil
from call import select
from menu import menu

page = st.sidebar.radio('Paginas', ['Menu','Chamada', 'Perfil do aluno'])

if page == 'Menu':
    menu()

if page == 'Chamada':
    select()

if page == 'Perfil do aluno':
    perfil()