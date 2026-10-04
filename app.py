import streamlit as st

from game_logic import check_answer
from game.rooms.room_1 import INTRO_TEXT, DOOR_PASSWORD

st.title("Sample Escape Room")
st.write(INTRO_TEXT)

answer = st.text_input("Enter the code to open the door: ")

if st.button("Unlock door"):
    if check_answer(answer, DOOR_PASSWORD):
        st.success("Correct Code! The door is open")
    else:
        st.error("Wrong Code, Try again")