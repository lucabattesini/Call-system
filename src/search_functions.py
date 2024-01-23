import streamlit as st
from student_profile import show_profile
from db.connection import get_students_df
from student_functions import get_lasts_absences_by_student, get_student_notes, create_student_note
from graphic_functions import create_a_graphic_divided_by_day, get_presence_percent_bar

def student_search(name) :
    df  = get_students_df()

    for _, row in df.iterrows():
        student_id = row['student_id']
        student_first_name = row['first_name']
        student_last_name = row['last_name']
        student_name = student_first_name + " " + student_last_name
        year_class = row['school_year']
        class_name = row['classroom']
        class_full_name = year_class + class_name

        student_name_lower = student_name.lower()
        input_student_name_lower = name.lower()

        if student_name_lower == input_student_name_lower:
            if st.button(f"### {student_name}  -  {class_full_name}"):
                
                show_profile(student_name, class_full_name)
                st.markdown("### ")

                get_presence_percent_bar(student_id)
                st.markdown("### ")

                create_a_graphic_divided_by_day(student_id)
                cl, cl2, cl3 = st.columns(3)
                with cl2:
                    st.text("          Dividido por dias")
                st.markdown("---")
                st.title("Ultimas 5 faltas")

                get_lasts_absences_by_student(student_id)
                st.markdown("### ")
                with st.form("Notes"):
                    note = st.text_input("Adicione uma nova anotação") 
                    save = st.form_submit_button("Salvar", on_click=create_student_note(note, "Matematica", student_id))
                    #if save and note:
                        #print("recebo")
                        #create_student_note(note, "Matematica", student_id)
                    st.title("Anotações")

                    get_student_notes(student_id)