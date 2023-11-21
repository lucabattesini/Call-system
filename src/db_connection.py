import pandas as pd

def get_attendance_df() :
    return pd.read_csv("./db/attendance.csv", encoding="UTF-8")

def get_students_df() :
    return pd.read_csv("./db/students_utf-8.csv", encoding="UTF-8")