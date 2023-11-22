import os
import pandas as pd

attendance_path = os.path.join(os.path.dirname(__file__), 'attendance.csv')
students_path = os.path.join(os.path.dirname(__file__), 'students_utf-8.csv')

def get_attendance_df() :
    return pd.read_csv(attendance_path, encoding="UTF-8")

def get_students_df() :
    return pd.read_csv(students_path, encoding="UTF-8")