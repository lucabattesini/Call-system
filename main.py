import pandas as pd
import streamlit as st

#df = pd.read_csv("./bfotool-download(1).csv")

dados = {'nome': ["Luca","Clara","Nick"],
         'veio': [0, 0, 0]}

dfe = pd.DataFrame(dados)

st.markdown("### Luca")
if st.button("Veio"):
    dfe.loc[dfe['nome'] == 'Luca', 'veio'] = 1

st.markdown("### Clara")
if st.button("Veio?"):
    dfe.loc[dfe['nome'] == 'Clara', 'veio'] = 1

st.markdown("### Nick")
if st.button("Veio??"):
    dfe.loc[dfe['nome'] == 'Nick', 'veio'] = 1


print(dfe)