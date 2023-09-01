import pandas as pd
import streamlit as st

df = pd.read_csv("./dados.csv")

#dados = {'nome': ["Luca","Clara","Nick"],
         #'veio': [0, 0, 0]}

#dfe = pd.DataFrame(dados)
st.markdown("### Luca")
if st.button("Veio"):
    df.loc[df['nome']=='luca', ['presenca']] = 1
    print(df)
    df.to_csv('./dados.csv')
    #df.at['luca', 'presenca'] = 1

st.markdown("### Clara")
if st.button("Veio?"):
    df.loc[['clara'], ['presenca']] = 1
    df.to_csv('./dados.csv')

st.markdown("### Nick")
if st.button("Veio??"):
    df.loc[['yannick'], ['presenca']] = 1
    df.to_csv('./dados.csv')


print(df)