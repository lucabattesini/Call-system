#Importing pandas and streamlit
import pandas as pd
import streamlit as st
#Reading the csv file 
df = pd.read_csv("./dados.csv")
#Read header from csv file
df.head()
#Creating a var to create a unique key
x = int(1)
#Using for in to read each line of csv file
for name in df['nome']:
    #Name of the student formated
    st.markdown(f"### {name}")
    #Modifying key number 
    x = x + 1
    #Creating a button to check if the student come to class
    if st.button("Veio?", key=x):
        #Saving 1 if student come or 0 if isn't
        df.loc[df['nome']==f'{name}', ['presenca']] = 1
        #Printing the csv fle
        print(df)
        #Saving all changes in the file
        df.to_csv('./dados.csv', index=False)