# todo_7.py
import streamlit as st

def todo():
    st.header(":seven:. :blue[Simple To-Do List]")
    st.write("Lets try to use session states in an app")
    if "todos" not in st.session_state:
        st.session_state.todos = []
    # create a text input and give it a varible name todo and ask the user to enter a todo item
    todo = st.text_input("Please enter a to-do item")
    # todo is diffrent from todos
    if st.button("Add"):
        st.session_state.todos.append(todo)

    st.header(f'To do list')
    for i, todo in enumerate(st.session_state.todos):
        st.write(f'{i + 1}. {todo} ')
    st.write("")
    if st.button("Show code"):
        st.code('''
if "todos" not in st.session_state:
    st.session_state.todos = []
# create a text input and give it a varible name todo and ask the user to enter a todo item
todo = st.text_input("Please enter a to-do item")
# todo is diffrent from todos
if st.button("Add"):
    st.session_state.todos.append(todo)

st.header(f'To do list')
for i, todo in enumerate(st.session_state.todos):
    st.write(f'{i + 1}. {todo} ')
''')
