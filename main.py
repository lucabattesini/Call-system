import pandas as pd
import streamlit as st

df = pd.read_csv("./bfotool-download(1).csv")

dados = {'nome': ["Luca","Clara","Nick"],
         'veio': ["he", "lo", "di"]}

dfe = pd.DataFrame(dados)

print(dfe)