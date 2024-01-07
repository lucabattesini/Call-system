import pandas as pd 
import streamlit as st
from datetime import datetime
from db.connection import get_attendance_df, save_notes_df, get_notes_df
from utils import dateweek, subjects_list

def get_student_presence_sum(id) :                                                            
    df = get_attendance_df()
    ct = 0
    for _, row in df.iterrows():
        student_id = row['student_id']
        attendance = row['attendance']
        if student_id == id and attendance == 1:
            ct += 1
    return ct

def get_student_absence_sum(id) :
    df = get_attendance_df()
    ct = 0
    for _, row in df.iterrows():
        student_id = row['student_id']
        attendance = row['attendance']
        if student_id == id and attendance == 0:
            ct += 1
    return ct

def get_student_absence_sum_by_week(id, day) :
    week_list = dateweek(day)
    df = get_attendance_df()
    ct = 0
    for _, row in df.iterrows():
        date = row['date']
        student_id = row['student_id']
        attendance = row['attendance']
        if student_id == id and attendance == 0:
            for week_day in week_list :
                if date == week_day:
                    ct += 1
    return ct

def get_student_presence_sum_by_week(id, day) :
    week_list = dateweek(day)
    df = get_attendance_df()
    ct = 0
    for _, row in df.iterrows():
        date = row['date']
        student_id = row['student_id']
        attendance = row['attendance']
        if student_id == id and attendance == 1:
            for week_day in week_list :
                if date == week_day:
                    ct += 1
    return ct

def get_student_presence_and_absence(id) :
    presences = get_student_presence_sum(id)
    absences = get_student_absence_sum(id)
    all_classes = presences + absences
    presences_first_part_formula = presences * 100
    presences_percentage = presences_first_part_formula / all_classes
    return all_classes, presences_percentage

def get_student_presence_and_absence_by_week(id) :
    presences = get_student_presence_sum_by_week(id)
    absences = get_student_absence_sum_by_week(id)
    all_classes = presences + absences
    presences_first_part_formula = presences * 100
    presences_percentage = presences_first_part_formula / all_classes
    return all_classes, presences_percentage

def get_absences_by_student(id) :
    df = get_attendance_df()
    column, column2 = st.columns(2)
    ct = 0
    for _, row in df.iterrows():
        student_id = row['student_id']
        date = row['date']
        attendance = row['attendance']
        if student_id == id:
            if attendance == 0:
                ct += 1
                if ct <= 5:
                    with column:
                        st.markdown(f" Ausente")
                    with column2:
                        st.markdown(f" Data: {date}")

def create_student_note(note, subject, id) :
    df = get_notes_df()
    df.head()
    today = datetime.now()
    ftoday = today.strftime('%d/%m/%y')
    new_line = pd.DataFrame({'student_id': [id], 'notes': [note], 'subject': [subject], 'date': [ftoday]})
    df = pd.concat([df, new_line], axis=0, ignore_index=True)
    save_notes_df(df)

def get_student_notes(id) :
    df = get_notes_df()
    column, column2 = st.columns(2)
    for _, row in df.iterrows():
        student_id = row['student_id']
        if student_id == id:
            student_notes = row['notes']
            student_notes_subject = row['subject']
            student_notes_date = row['date']
            with column:
                st.markdown(f" {student_notes_subject}")
            with column2:
                st.markdown(f" {student_notes_date}")
            st.markdown(f"{student_notes}")