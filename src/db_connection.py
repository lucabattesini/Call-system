import pandas as pd

def get_attendance_df() :
    return pd.read_csv("./db/attendance.csv", encoding="UTF-8")

def get_students_df() :
    return pd.read_csv("./db/students.csv", encoding="UTF-8")