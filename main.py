#Importing pandas and streamlit
import pandas as pd
import streamlit as st
#Reading the csv file 
df = pd.read_csv("./attendance_table.csv", encoding='UTF-8')
df2 = pd.read_csv("./call_list_students_utf-8.csv", encoding="UTF-8")
#Read header from csv file
df.head()
df2.head()
#Creating a var to create a unique key
x = int(1)
#Using for in to read each line of csv file
for name in df2['first_name']:
    #Name of the student formated
    st.markdown(f"### {name}")
    #Modifying key number 
    x = x + 1
    #Creating a button to check if the student come to class
    if st.button("Veio?", key=x):
        #Saving 1 if student come or 0 if isn't
        df2.loc[df2['first_name']==f'{name}', ['attendance_total']] = 1
        dftosave = df2[['student_id', 'attendance_total']]
        #Printing the csv fle
        print(df2)
        #Saving all changes in the file
        df2.to_csv('./call_list_students_utf-8.csv', index=False)
        dftosave.to_csv('./attendance_table.csv', index=False)
print(df)
print(df2)