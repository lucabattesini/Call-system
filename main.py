import pandas as pd
import streamlit as st

df = pd.read_csv("./dados.csv")
df.head()

#dados = {'nome': ["Luca","Clara","Nick"],
         #'veio': [0, 0, 0]}

#dfe = pd.DataFrame(dados)
st.markdown("### Luca")
if st.button("Veio"):
    df.loc[df['nome']=='luca', ['presenca']] = 1
    print(df)
    df.to_csv('./dados.csv', index=False)
    #df.at['luca', 'presenca'] = 1

st.markdown("### Clara")
if st.button("Veio?"):
    df.loc[df['nome']=='clara', ['presenca']] = 1
    print(df)
    df.to_csv('./dados.csv', index=False)

st.markdown("### Nick")
if st.button("Veio??"):
    df.loc[df['nome']=='yannick', ['presenca']] = 1
    print(df)
    df.to_csv('./dados.csv', index=False)

st.markdown("### Lola")
if st.button("Veio???"):
    df.loc[df['nome']=='lola', ['presenca']] = 1
    print(df)
    df.to_csv('./dados.csv', index=False)

print(df)