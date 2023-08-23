import pandas as pd
import streamlit as st

yn = st.number_input("Write 1 or 0")

df = pd.read_csv("./bfotool-download(1).csv")

print(df)