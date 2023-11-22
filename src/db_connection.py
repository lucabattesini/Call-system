import pandas as pd
import os
attendance_path = os.path.abspath(r'.\db\attendance.csv')
def get_attendance_df() :
    return pd.read_csv(attendance_path, encoding="UTF-8")

def get_students_df() :
    return pd.read_csv("./db/students_utf-8.csv", encoding="UTF-8")