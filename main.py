import pandas as pd
import streamlit as st
from datetime import datetime
from functions import call_function
 
df = pd.read_csv("./attendance_table.csv", encoding='UTF-8')
df2 = pd.read_csv("./call_list_students_utf-8.csv", encoding="UTF-8")
df.head()
df2.head()

call_function(df, df2)

#print(df)
#print(df2)