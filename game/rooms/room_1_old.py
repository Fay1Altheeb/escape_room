import streamlit as st
from pathlib import Path

# Python script for the basement room: all related functions (puzzles) and the page interface 

# Power generator puzzle function 
# The user needs to activate all five switches to turn on the power.

# # All switches in the generator starts as False (True: On, False: Off)
# # switches =  [False for x in range(5)]

# # Dictionary that takes a key indicating the switch number, and the value is a list indicating all affected switches
# switch_index = {
#     1: [0, 1],
#     2: [0, 2],
#     3: [0, 3],
#     4: [0, 4],
#     5: [0, 2, 4]
# }

# 
# def turn_switch(switches, switch_number):
#     for i in switch_index[switch_number]:
#         switches[i] = not switches[i] # flip the value of the switch

#     # Return the new state of the switches list 
#     return switches


# # Check function to check if all 5 switches is True (On)
# def check_generator(switches): 
#     # For loop to go through the switches list 
#     for i in switches:
#         # If one of the switches is off (False) return False (meaning the generator is not turned on)
#         if i == False :
#             return False 

#     # All switches equal True return True (meaning the generator is turned on)
#     return True 

# # Check function to check if all 5 switches is True (On)
# def check_generator(switches): 
#     # For loop to go through the switches list 
#     for i in switches:
#         # If one of the switches is off (False) return False (meaning the generator is not turned on)
#         if i == False :
#             return False 

#     # All switches equal True return True (meaning the generator is turned on)
#     return True 


# List to store the correct sequence of turning the switches on (switch 3, 1, 4, 2, then 5)
correct_order = [3, 1, 4, 2, 5]

# A list to save the player's order for turning the Switch on.
current_order = []

# Turn on the switch if it is the correct next switch 
def turn_switch(switches, correct_order, current_order, switch_number):

    # If the switch chosed by player is the correct one add it to the current_order list 
    if switch_number == correct_order[len(current_order)] : 
        switches[switch_number - 1] = True # Turn the switch to True 
        current_order.append(switch_number)
        return True
    # Return Fa
    return False


# Reset function that reset all generator's switches to off (False)
def reset_generator():
    return [False for x in range(5)]


# Streamlit session stat 

# Store the switches state
if "switches" not in st.session_state:
    st.session_state.switches = reset_generator()


# Store the player's current order
if "current_order" not in st.session_state:
    st.session_state.current_order = []


# Store whether the generator popup is open
if "generator_open" not in st.session_state:
    st.session_state.generator_open = False


# Store whether the player selected a wrong switch
if "wrong_switch" not in st.session_state:
    st.session_state.wrong_switch = False

# 
if "boxes_open" not in st.session_state:
    st.session_state.boxes_open = False


# Styling the popup 

st.markdown(
    """
    <style>

    /* Start Generator button */
    div[data-testid="stDialog"] button[kind="primary"] {
        background-color: #5f6959;
        color: #f1eee6;
        border: 1px solid #747f6d;
        border-radius: 8px;
    }

    /* Start Generator hover */
    div[data-testid="stDialog"] button[kind="primary"]:hover {
        background-color: #6c7765;
        color: #ffffff;
        border-color: #899482;
    }

    /* Normal buttons inside the popup */
    div[data-testid="stDialog"] button[kind="secondary"] {
        border-radius: 8px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# Generator Popup Function 
@st.dialog("Emergency Generator", width="meduim")
def generator_popup():

    # Friendly caption to the player 
    st.caption(
        "The power is off. Find the correct startup sequence."
    )

    # Root path 
    ROOT = Path(__file__).resolve().parents[2]

    # Generator image and the note image one by the other in same rwo 
    generator_column, note_column = st.columns(
        [2.2, 1],
        gap="small"
    )

    with generator_column:
        st.image(ROOT / "assets/images/room_1/generator.png", 
                 use_container_width=True)
        
    with note_column:
        st.image(ROOT / "assets/images/room_1/generator_note.png", 
                 use_container_width=True)


    # Wrong message if the sequence is wrong 
    if st.session_state.wrong_switch:

        st.error(
            "Wrong sequence. The switches have reset."
        )

        st.session_state.wrong_switch = False


    # Switch buttons 

    switch_columns = st.columns(5)

    roman_numbers = ["I", "II", "III", "IV", "V"]


    for i, column in enumerate(switch_columns):

        with column:

            is_on = st.session_state.switches[i]

            label = (
                f"{roman_numbers[i]}\n"
                f"{'🟢' if is_on else '⚫'}"
            )


            if st.button(
                label,
                key=f"switch_{i + 1}",
                use_container_width=True,
                disabled=is_on
            ):

                correct = turn_switch(
                    st.session_state.switches,
                    correct_order,
                    st.session_state.current_order,
                    i + 1
                )


                # Reset if the player selects the wrong switch
                if correct == False:

                    st.session_state.switches = reset_generator()
                    st.session_state.current_order = []
                    st.session_state.wrong_switch = True


                st.rerun(scope="fragment")


    st.caption(
        "Follow the note and activate the switches in the correct order."
    )


    # Start generator button 

    if st.button(
        "Start generator",
        type="primary",
        icon=":material/power_settings_new:",
        use_container_width=True
    ):

        if all(st.session_state.switches):

            st.session_state.generator_open = False
            st.rerun()

        else:

            st.error(
                "It didn't start. Complete the startup sequence first."
            )


    # Reset button 

    if st.button(
        "Reset switches",
        icon=":material/restart_alt:",
        use_container_width=True
    ):

        st.session_state.switches = reset_generator()
        st.session_state.current_order = []
        st.session_state.wrong_switch = False

        st.rerun(scope="fragment")


##########################################ُ End of the first puzzle ##########################################ُ

# The other puzzle is finding the correct sequence of numbers from the boxes
# Tuple storing the correct answers that user should enter to solve this puzzle 
shapes_counts = (3, 4, 3) # Tuple to store the counts of the spaes 

triangle_count =  shapes_counts[0]
circle_count = shapes_counts[1]
x_count = shapes_counts[2]

answers = []

answers.append(triangle_count + circle_count)
answers.append(triangle_count - x_count)
answers.append(circle_count + x_count)

answers = tuple(answers)

# Check player answer
def check_answer(player_answer):

    for i in range(3):
        if player_answer[i] != answers[i]:
            return False
    return True

# Storage Boxes Popup Function
@st.dialog("Storage Boxes", width="small")
def boxes_popup():

    # Friendly caption to the player
    st.caption(
        "Check the inspection labels and solve the equations."
    )

    # Image Path
    project_root = Path(__file__).resolve().parents[2]

    boxes_path = (
        project_root / "assets" / "images" / "room_1" / "storage_boxes.png"
    )

    # Boxes and note image
    st.image(
        str(boxes_path),
        use_container_width=True
    )

    # Player inputs
    input_columns = st.columns(3)

    with input_columns[0]:
        answer_1 = st.text_input("△ + 〇")
        
    with input_columns[1]:
        answer_2 = st.text_input("△ - X")
        
    with input_columns[2]:
        answer_3 = st.text_input("〇 + X")

    # Submit button
    if st.button(
        "Submit",
        type="primary",
        icon=":material/arrow_forward:",
        use_container_width=True
    ):
        
        
        player_answer = (
            int(answer_1),
            int(answer_2),
            int(answer_3)
        )

        if check_answer(player_answer):

            st.session_state.boxes_open = False
            st.rerun()

        else:

            st.error(
                "Incorrect. Check the labels and try again."
            )

    

# Basement Page (Just sample for now)

st.title("Basement")


if st.button("Start generator puzzle"):
    st.session_state.generator_open = True

# Reopen the popup after each rerun
if st.session_state.generator_open:
    generator_popup()

if st.button("Start boxes puzzle"):
    st.session_state.boxes_open = True

if st.session_state.boxes_open:
    boxes_popup()