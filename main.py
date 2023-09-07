import pandas as pd
import streamlit as st
from datetime import datetime
from functions import call_function
 
df = pd.read_csv("./attendance_table.csv", encoding='UTF-8')
df2 = pd.read_csv("./call_list_students_utf-8.csv", encoding="UTF-8")
df.head()
df2.head()

x = int(1)
x1 = 'a'
data = datetime.now()
fdata = data.strftime('%d/%m/%y')

call_function(df, df2, x, x1, fdata)

#print(df)
#print(df2)