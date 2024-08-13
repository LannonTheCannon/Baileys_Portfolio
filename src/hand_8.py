# hand_8.py
import streamlit as st

def hands_on():
    st.header(":eight:. :blue[Fun Hands on Activity]")
    st.write("Now its your turn to create a fun activity")
    import random
    st.title("Guess the number game")

    # Intialize a var in a session state
    if "secret_number"  not in st.session_state:
        # generate a random number between 1 and 100
        st.session_state["secret_number"] = random.randint(1,100)
    secret_num = st.session_state["secret_number"]

    # get the player's guess
    guess = st.number_input("Enter a number between 1 and 100", min_value = 1, max_value = 100)
    if st.button("Check your guess!"):
        if secret_num == guess:
            st.success("Wow you guessed right!")
            st.balloons()
        elif guess <= secret_num:
            st.warning("You guessed too low")
        elif guess >= secret_num:
            st.warning("You guessed too high")
    st.write("")
    if st.button("Show code"):
        st.code('''
import streamlit as st
import random
st.title("Guess the number game")

# Intialize a var in a session state
if "secret_number"  not in st.session_state:
    # generate a random number between 1 and 100
    st.session_state["secret_number"] = random.randint(1,100)
secret_num = st.session_state["secret_number"]

# get the player's guess
guess = st.number_input("Enter a number between 1 and 100", min_value = 1, max_value = 100)
if st.button("Check your guess!"):
    if secret_num == guess:
        st.success("Wow you guessed right!")
        st.balloons()
    elif guess <= secret_num:
        st.warning("You guessed too low")
    elif guess >= secret_num:
        st.warning("You guessed too high")
''')
