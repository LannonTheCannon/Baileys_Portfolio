# intro_to_streamlit_day_1
# cd C:\Users\cvsio\Desktop\Streamlit_Web
# streamlit run intro_to_streamlit_day_1.py
import streamlit as st
# src folder has all the functions
# call back using from folder_name.file_name import name_of_function
from src.landing_1 import introduction
from src.setup_2 import setup
from src.basic_3 import basic_elements
from src.simple_4 import simple_app
from src.run_5 import running_app
from src.sess_6 import sess_states
from src.todo_7 import todo
from src.hand_8 import hands_on
from src.quiz_9 import quiz_game
from src.wrap_10 import wrap_up

def main():
    st.title("Introduction to Streamlit day 1")
    st.subheader(':grey[A lesson plan for beginner python programers!]')
    
    # add a sidebar
    st.sidebar.title(":notebook: Lesson section :notebook:")
    with st.sidebar.expander("Streamlit fundamentals"):
        streamlit_sections = [
        ":one:. :red[Introduction]",
        ":two:. :red[Setup]",
        ":three:. :orange[Basic Streamlit Elements]",
        ":four:. :orange[Simple Interative App]",
        ":five:. :green[Running The App]",
        ":six:. :green[Session States]",
        ":seven:. :blue[Simple To-Do List]",
        ":eight:. :blue[Fun Hands on Activity]",
        ":nine:. :violet[Simple Quiz Game]",
        ":keycap_ten:. :violet[Wrap up]"
        ]
        selected_streamlit_section = st.radio("Go To", streamlit_sections)

    if selected_streamlit_section:
        # main content
        if selected_streamlit_section == ":one:. :red[Introduction]":
            introduction()
        elif selected_streamlit_section == ":two:. :red[Setup]":
            setup()
        elif selected_streamlit_section == ":three:. :orange[Basic Streamlit Elements]":
            basic_elements()
        elif selected_streamlit_section == ":four:. :orange[Simple Interative App]":
            simple_app()
        elif selected_streamlit_section == ":five:. :green[Running The App]":
            running_app()
        elif selected_streamlit_section == ":six:. :green[Session States]":
            sess_states()
        elif selected_streamlit_section == ":seven:. :blue[Simple To-Do List]":
            todo()
        elif selected_streamlit_section == ":eight:. :blue[Fun Hands on Activity]":
            hands_on()
        elif selected_streamlit_section == ":nine:. :violet[Simple Quiz Game]":
            st.divider()
            quiz_game()
        elif selected_streamlit_section == ":keycap_ten:. :violet[Wrap up]":
            wrap_up()
    
if __name__ == "__main__":
    main()
