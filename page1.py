import streamlit as st

st.markdown("## Selecione uma turma e uma matéria")

column1, column2 = st.columns(2)
serie_list = ['Turma', '1EM A', '1EM B', '2EM A', '2EM B']
subject_list = ['Matéria', 'Matemática','Inglês','Português','Química','Física','Biologia','Educação','Geografia','História','Sociologia','Filosofia']

with column1:
    select = st.selectbox("Escolha a turma:", serie_list)

with column2:
    select = st.selectbox("Escolha a matéria:", subject_list)
 
if st.button("Ir a lista de chamada"):
    st.markdown("esta funcionando")