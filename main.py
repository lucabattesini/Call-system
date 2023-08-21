import pandas as pd
import streamlit as st

yn = st.number_input("Write 1 or 0")

if yn == 1:
    with open("bfotool-download(1).csv", 'a') as txt_file:
            txt_file.write('1')