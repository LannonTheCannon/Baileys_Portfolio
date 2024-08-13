# landing_1.py
import streamlit as st

def introduction():
    st.header(":one:. :red[Introduction]")
    st.write("Streamlit is a Python library that makes it easy to create web apps.")
    if st.button("Show Example App"):
        st.code('''
import streamlit as st
st.title("Hello, Streamlit!")
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")
''')
