# sess_6
import streamlit as st

def sess_states():
    st.header(":six:. :green[Session States]")
    st.write("Session states saves variables during reruns except if the tab is closed")
    st.header(":six:.:one: :green[Initialization]")
    st.write("You can initialize the session state by using these lines of code: ")
    st.code('''
if 'key' not in st.session_state
    st.session_state['key'] = 'value'
    
# you can also use the .dot method
if 'key' not in st.session_state
    st.session_state.key = 'value'
''')
    st.header(":six:.:two: :green[Reading and Updating]")
    st.write("The sessions states work similarly to a dictionary with keys and values")
    st.write("You can read the value of it by using st.write")
    st.code("st.write(f'{st.session['key']}')")
    st.write("You can also update it like a dictionary by setting its value")
    st.code('''
st.session_state['key'] = 'better_value'
# .dot method
st.session_state.key = 'better_value'
''')
    st.header(":six:.:three: :green[Deleting]")
    st.write("After you\'re finished with a session state you can delete it with del")
    st.code('''
# single delete
del st.session_key['key']

# or delete all
for key in session_state.keys():
    del session_state['key']

''')
