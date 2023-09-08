import pandas as pd
import streamlit as st
from datetime import datetime
from functions import compute_attendance
 
attendance = pd.read_csv("./attendance_table.csv", encoding='UTF-8')
student_list = pd.read_csv("./call_list_students_utf-8.csv", encoding="UTF-8")
attendance.head()
student_list.head()

today = datetime.now()
ftoday = today.strftime('%d/%m/%y')

compute_attendance(attendance, student_list, ftoday)

#print(df)
#print(df2)