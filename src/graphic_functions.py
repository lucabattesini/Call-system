import streamlit as st
import pandas as pd
from student_functions import get_student_presence_and_absence_by_week

def create_a_graphic_divided_by_week() :
    df = pd.DataFrame(lista, columns = ["Presença"])
    st.line_chart(df, y="Presença")