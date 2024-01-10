import streamlit as st
import pandas as pd
from student_functions import get_student_presence_by_day

def create_a_graphic_divided_by_week(id) :
    presence_list_by_day = get_student_presence_by_day(id)
    df = pd.DataFrame(presence_list_by_day, columns = ["Presença"])
    return st.line_chart(df, y="Presença")
