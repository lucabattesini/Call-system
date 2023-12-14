import pandas as pd 
from datetime import datetime
from db.connection import get_students_df, get_attendance_df
from utils import dateweek

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

def get_student_presence_and_absence(id) :
    presences = get_student_presence_sum(id)
    absences = get_student_absence_sum(id)
    all_classes = presences + absences
    presences_first_part_formula = presences * 100
    presences_percentage = presences_first_part_formula / all_classes
    return all_classes, presences_percentage

#def get_student_presence_and_absence_by_week(id) :
    ct = 0
    df = get_attendance_df()
    presences = get_student_presence_sum(id)
    absences = get_student_absence_sum(id)
    today = datetime.now()
    week = dateweek(today)

def get_presence_by_subject(subject, id) :
    df = get_attendance_df()
    student_presence = []
    for _, row in df.iterrows():
        student_id = row['student_id']
        presence_subject = row['subject']
        date = row['date']
        attendance = row['attendance']
        if student_id == id:
            if presence_subject == subject:
                if attendance == 1:
                    date_and_subject = str(f"Presente\n Matéria: {subject}\n Data: {date}")
                    student_presence.append(date_and_subject)
                elif attendance == 0:
                    date_and_subject = str(f"Ausente\n Matéria: {subject}\n Data: {date}")
                    student_presence.append(date_and_subject)
    return student_presence