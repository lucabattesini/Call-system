import pandas as pd
import streamlit as st
from datetime import datetime
 
df = pd.read_csv("./attendance_table.csv", encoding='UTF-8')
df2 = pd.read_csv("./call_list_students_utf-8.csv", encoding="UTF-8")
df.head()
df2.head()

x = int(1)
x1 = 'a'
data = datetime.now()
fdata = data.strftime('%d/%m/%y')

for index, row in df2.iterrows():
    id = row['student_id']
    first_name = row['first_name']
    last_name = row['last_name']

    st.markdown(f"### {first_name} {last_name}")

    x = x + 1
    x1 = x1 + 'b'
    if st.button("Presente", key=x):
        df.loc[index] = {'student_id': id, 'attendance_total': 1, 'date': fdata}
        df2.loc[df2['student_id']==id, 'attendance_total'] += 1
        df2.loc[df2['student_id']==id, 'date'] = fdata
        df.to_csv('./attendance_table.csv', index=False)

    if st.button("Ausente", key=x1):
        df.loc[index] = {'student_id': id, 'attendance_total': 0, 'date': fdata}
        df2.loc[df2['student_id']==id, 'attendance_total'] += 0
        df2.loc[df2['student_id']==id, 'date'] = fdata
        df.to_csv('./attendance_table.csv', index=False)

df2.to_csv('./call_list_students_utf-8.csv', index=False)

#print(df)
#print(df2)