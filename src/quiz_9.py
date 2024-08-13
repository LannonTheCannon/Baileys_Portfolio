# quiz_9.py
import streamlit as st

def quiz_game():
    st.header(":nine:. :violet[Simple Quiz Game]")
    # initialize session state variables for the quiz
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    # create a variable using state called score
    if "score" not in st.session_state:
        st.session_state.score = 0
    # and another one called quiz_complete
    if "quiz_complete" not in st.session_state:
        st.session_state.quiz_complete = False

    quiz_data = [
        {
            "question": "How to install Streamlit on the command prompt",
            "options": ["install streamlit.py","pip install streamlit","pip.install streamlit","install streamlit"],
            "correct_answer": 1,
        },
        {
            "question": "How to import Streamlit ",
            "options": ["import streamlit.py","add pip.streamlit","call streamlit.py as st","import streamlit as st"],
            "correct_answer": 3,
        },
        {
            "question": "How to create a text input ",
            "options": ["st.text_input()","text_input()","input('st.write()')","st.create.text_input"],
            "correct_answer": 0,
        },
        {
            "question": "How to display a button ",
            "options": ["st.button()","st.write('Button')","st.create.button","streamlit.display.button()"],
            "correct_answer": 0,
        },
        {
            "question": "How to create a slider ",
            "options": ["st.sllder()","st.slider()","st.create.slider()","slider()"],
            "correct_answer": 1,
        },
        {
            "question": "How to display a error ",
            "options": ["error()","st_error","st.error()","streamlit_display.error"],
            "correct_answer": 2,
        },
        {
            "question": "How to run a app in the command prompt",
            "options": ["cd app","streamlit run app","streamlit run app.py","streamlit_run_app.py"],
            "correct_answer": 2,
        }
    ]

    # quiz logic
    if not st.session_state.quiz_complete:
        question = quiz_data[st.session_state.current_question]
        st.write(f'Question {st.session_state.current_question + 1} of {len(quiz_data)}')
        st.write(question["question"])

        answer = st.radio("Choose your answer", question["options"], key = f'sb_q{st.session_state.current_question}')

        if st.button("Submit Answer",key = "sb_submit"):
            if question["options"].index(answer) == question["correct_answer"]:
                st.session_state.score += 1
                st.success("Correct")
                if st.button("Next"):
                    st.rerun()
            else:
                st.error(f'Wrong. The correct answer was "{question["options"][question["correct_answer"]]}"')
            if st.session_state.current_question < len(quiz_data) - 1:
                st.session_state.current_question += 1
            else:
                st.session_state.quiz_complete = True
        if st.button("Skip"):
            st.session_state.current_question += 1
            if st.session_state.current_question > len(quiz_data) -1:
                st.session_state.current_question = len(quiz_data)
                st.session_state.quiz_complete = True
            st.rerun()
    else:
        st.success("You completed the quiz!")
        st.write(f'Your score is: {st.session_state.score}/{len(quiz_data)}')
        if st.button("Restart"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.quiz_complete = False
            st.rerun()
    st.sidebar.write('''
______________________________
''')
    st.sidebar.write(f'Current score: {st.session_state.score}/{len(quiz_data)}')
