# basic_3.py
import streamlit as st

def basic_elements():
    st.header(":three:. :orange[Basic Streamlit Elements]")
    st.write("Lets explore some basic streamlit elements")
    st.subheader(":three:.:one: :orange[Text Elements:]")
    st.write("Here are some examples of text elements: ")
    st.code('''
st.title("Introduction to Streamlit day 1")
st.header(":one:. :red[Introduction]")
st.subheader(':grey[A lesson plan for beginner python programers!]')
st.write("Then create a new Python file for your project.")
st.markdown("The quick brown fox jumps over the lazy dog")
''')
    st.subheader(":three:.:two: :orange[Input elements]")
    st.write("Streamlit provides various input elements:")
    username = st.text_input("Enter your username")
    age = st.slider("Select your age", 0, 150)
    st.write(f'Hello {username}, you are {age} years old.')
    st.subheader(":three:.:three: :orange[Display an image]")
    st.write("You can display images like this: ")
    st.image("https://scentofagamer.wordpress.com/wp-content/uploads/2014/11/plains_alara_michaelkomarck.jpg")
