# simple_4.py
import streamlit as st

def simple_app():
    st.header(":four:. :orange[Simple Interative App]")
    st.write("Lets create a basic calculator!")
    num1 = st.number_input("Please enter your first number: ", value = 0)
    num2 = st.number_input("Please enter your second number: ", value = 0)
    operation = st.selectbox("Choose your operation",["+","-","*","/"])
    result = 0
    if st.button("="):
        if operation == "+":
            result =num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        else:
            if num2 == 0:
                result = "You cannot divide by 0 :)"
            else:
                result = num1 / num2
    st.success(f'{result}')
    st.write("")
    if st.button("Show code"):
        st.code('''
import streamlit as st
num1 = st.number_input("Please enter your first number: ", value = 0)
num2 = st.number_input("Please enter your second number: ", value = 0)
operation = st.selectbox("Choose your operation",["+","-","*","/"])
result = 0
if st.button("="):
    if operation == "+":
        result =num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    else:
        if num2 == 0:
            result = "You cannot divide by 0 :)"
        else:
            result = num1 / num2
    st.success(f'{result}')
    ''')
