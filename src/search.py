import pandas as pd
import streamlit as st
from search_functions import student_search
from utils import classes_list
from db.connection import get_students_df

def search_profile() :

    study_search = st.text_input("Insira o nome completo do aluno")

    student_search(study_search)