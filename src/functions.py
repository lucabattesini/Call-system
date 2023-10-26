import pandas as pd
import streamlit as st
import datetime as datetime

def call_list_buttons(attendance, student_list, fdata, materias, dateweek, today, lista, classes):
    for index, row in student_list.iterrows():
        id = row['student_id']
        first_name = row['first_name']
        last_name = row['last_name']
        serie = row['school_year']
        serie_tipo = row['classroom']
        real_serie = serie + serie_tipo

        column1, column2, column3, column4, column5, column6 = st.columns(6)
        if real_serie == classes:
            with column1:
                st.markdown(f"### {first_name} {last_name}")

            with column2:
                if st.button("Presente", key=f'{index}_presente'):
                    row = pd.DataFrame({'student_id': [id],'attendance': [1],'date': [lista[0]], 'subject': [materias], 'class': [classes]})
                    attendance = pd.concat([attendance, row], axis=0, ignore_index=True)
                    
            with column3:
                if st.button("Presente", key=f'{index}_presente' * 11):
                    row = pd.DataFrame({'student_id': [id],'attendance': [1],'date': [lista[1]], 'subject': [materias], 'class': [classes]})
                    attendance = pd.concat([attendance, row], axis=0, ignore_index=True)
                    
            with column4:
                if st.button("Presente", key=f'{index}_presente' * 13):
                    row = pd.DataFrame({'student_id': [id],'attendance': [1],'date': [lista[2]], 'subject': [materias], 'class': [classes]})
                    attendance = pd.concat([attendance, row], axis=0, ignore_index=True)

            with column5:
                if st.button("Presente", key=f'{index}_presente' * 17):
                    row = pd.DataFrame({'student_id': [id],'attendance': [1],'date': [lista[3]], 'subject': [materias], 'class': [classes]})
                    attendance = pd.concat([attendance, row], axis=0, ignore_index=True)

            with column6:
                if st.button("Presente", key=f'{index}_presente' * 23):
                    row = pd.DataFrame({'student_id': [id],'attendance': [1],'date': [lista[4]], 'subject': [materias], 'class': [classes]})
                    attendance = pd.concat([attendance, row], axis=0, ignore_index=True)

            st.markdown('---')
    attendance.to_csv('./db/attendance.csv', index=False)



def call_list_sum(attendance, student_list):
    for i, row in student_list.iterrows():
        id = row['student_id']
        x = 0

        for index, row2 in attendance.iterrows():
            id2 = row2['student_id']
            value = row2['attendance']
            if id == id2:
                if value == 1:
                  x = x + 1

        student_list.loc[student_list['student_id'] == id, 'attendance_total'] = x
    student_list.to_csv('./call_list_students_utf-8.csv', index=False)


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


def pages_sidebar(attendance, student_list, fdata, side, materias, dateweek, today, lista, classes):
    for subject in materias:
        if side == subject:
            call_list_buttons(attendance, student_list, fdata, subject, dateweek, today, lista, classes)
            if st.button("Salvar", key='ola'):
                call_list_sum(attendance, student_list)

