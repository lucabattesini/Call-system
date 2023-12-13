import pandas as pd 
import streamlit as st
from db.connection import get_students_df

def get_student_presence_sum(id) :
    df = get_students_df()
    for _ in df.iterrows():
        student_id = df['student_id']
        attendance_total = df['attendance_total']
        if student_id == id:
            return attendance_total

def get_student_presence_and_absence(absences, id) :
    presences = get_student_presence_sum(id)
    all_classes = presences + absences
    presences_first_part_formula = presences * 100
    presences_percentage = presences_first_part_formula / all_classes
    return all_classes, presences_percentage
