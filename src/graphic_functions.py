import streamlit as st
import pandas as pd
from student_functions import get_student_presence_by_day, get_student_presence_and_absence

def presence_list_by_day_function(id) :
    presence_list = get_student_presence_by_day(id)
    presença_dia = 0
    presence_list_by_day  = []
    ct = 0
    for presence in presence_list:
        ct += 1
        if ct < 5:
            if presence == 1:
                presença_dia += 1
        elif ct == 5:
            ct = 0
            if presence == 1:
                presença_dia +=1
            presence_list_by_day.append(presença_dia)
            presença_dia = 0
    return presence_list_by_day

def create_a_graphic_divided_by_day(id) :
    presences_by_day = presence_list_by_day_function(id)
    df = pd.DataFrame(presences_by_day, columns = ["Presença"])
    return st.line_chart(df, y="Presença")

def get_presence_percent_bar(id) :
    percentage = get_student_presence_and_absence(id)
    bar = st.progress(0, text=f"{percentage}%")
    bar.progress(percentage, text=f"{percentage}")
