import pandas as pd 
from datetime import datetime
from db.connection import get_attendance_df, save_notes_df, get_notes_df
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

def get_student_presence_and_absence(id) :
    presences = get_student_presence_sum(id)
    absences = get_student_absence_sum(id)
    all_classes = presences + absences
    presences_first_part_formula = presences * 100
    presences_percentage = presences_first_part_formula / all_classes
    return all_classes, presences_percentage



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
    student_notes_list = []
    for _, row in df.iterrows():
        student_id = row['student_id']
        if student_id == id:
            student_notes = row['notes']
            student_notes_subject = row['subject']
            student_notes_date = row['date']
            data = f"Anotação: {student_notes} \n Matéria: {student_notes_subject} \n Data: {student_notes_date}"
            student_notes_list.append(data)
    return student_notes_list