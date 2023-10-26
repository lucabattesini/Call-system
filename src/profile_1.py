import streamlit as st
import pandas as pd

def show_profile(first_name, last_name, id, student_class) :
    column, column2 = st.columns(2)
    aluno = first_name + ' ' + last_name
    with column:
        st.markdown(f'# {aluno}')
    with column:
        st.markdown(f'# {student_class}')
    notes = st.text_input("Anotações")