import os
import pandas as pd

db_dir = os.path.join(os.path.dirname(__file__))
attendance_path = os.path.join(db_dir, 'attendance.csv')
notes_path = attendance_path = os.path.join(db_dir, 'notes.csv')
students_summary_path = os.path.join(db_dir, 'students_summary.csv')
students_path = os.path.join(db_dir, 'students.csv')

def get_attendance_df() :
    # TODO Verify if the file exists if not create them using the os lib
    return pd.read_csv(attendance_path, encoding="UTF-8")

def get_students_df() :
    # TODO Verify if the file exists if not create them using the os lib
    return pd.read_csv(students_path, encoding="UTF-8")

def save_attendance_df(df):
    df.to_csv(attendance_path, index=False)

def save_notes_df(df):
    df.to_csv(notes_path, index=False)

def save_students_df(df):
    df.to_csv(students_path, index=False)

def save_students_summary_df(df):
    df.to_csv(students_summary_path, index=False)