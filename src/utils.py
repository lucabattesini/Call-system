import pandas as pd
import streamlit as st
import datetime as datetime

def dateweek(fdata) :
    week_day = fdata.weekday()
    week_start = fdata - datetime.timedelta(days=week_day)
    week_end = week_start + datetime.timedelta(days=4)
    temporary_list = [1, 2, 3, 4, 5]
    day = 0
    week_days = []
    week_days_name = []
    formated_week_days = []
    translated_names = {
        "Monday": "Segunda-feira",
        "Tuesday": "Terça-feira",
        "Wednesday": "Quarta-feira",
        "Thursday": "Quinta-feira",
        "Friday": "Sexta-feira",
    }

    for n in temporary_list:
        delta = datetime.timedelta(days=day)
        new_date = week_start + delta
        week_days.append(new_date)
        day = day + 1

    for data in week_days:
        especific_week_day = data.strftime('%d/%m/%y')
        formated_week_days.append(especific_week_day)

    for day_name in week_days:
        name_of_day = day_name.strftime("%A")
        name_in_portuguese = translated_names.get(name_of_day)
        week_days_name.append(name_in_portuguese)
    return formated_week_days

def get_attendance_df() :
    return pd.read_csv("./db/attendance.csv", encoding="UTF-8")

