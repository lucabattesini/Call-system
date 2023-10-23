import streamlit as st
import pandas as pd

def perfil2(first_name, last_name, id, student_class) :
    coluna, coluna1 = st.columns(2)
    aluno = first_name + ' ' + last_name
    with coluna:
        st.markdown(f'# {aluno}')
    with coluna1:
        st.markdown(f'# {student_class}')
    notes = st.text_input("Anotações")