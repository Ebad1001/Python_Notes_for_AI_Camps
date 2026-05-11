# !python -m streamlit run file.py
import streamlit as st

# In Streamlit, every time the user interacts with a widget (button, slider, text input, etc.),
# the entire script reruns from top to bottom. Because of this behavior,
# normal Python variables do not remember their values between interactions.

# st.session_state is a special dictionary-like object in Streamlit
# that stores data for a particular user session.

# It helps your app:
# - Remember values
# - Maintain app state
# - Store user progress
# - Preserve variables between reruns
# - Without session state, variables reset after every interaction.

def incr():
    global temp_counter
    temp_counter += 1
    st.session_state.perm_counter += 1

st.button("Increment", on_click=incr)

temp_counter = 0
st.write(f"TEMP = {temp_counter}")

if "perm_counter" not in st.session_state:
    st.session_state.perm_counter = 0
st.write(f"PERM = {st.session_state.perm_counter}")