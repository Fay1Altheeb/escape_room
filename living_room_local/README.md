# The Last Door — Local Living Room

This is level 2 of the game where the player explores the living room, solves the puzzles, and finds the key to the study.

It uses input() and print(), and calls the same puzzle functions as the web app.

## Read the code in this order

| File | What to read there |
| --- | --- |
| room_2.py | The lists, dictionaries, loops, functions, and game decisions |
| console_room_2.py | A simple menu using input(), print(), if/elif/else, and while |
| app.py | How Streamlit buttons and fields call the game functions |
| display.py and style.css | Picture display and interface appearance |

Functions usually return two things: success (True/False) and a message.
For example, success, message = room.submit_word(answer, game) receives them.

## How the puzzles work

The bookshelf uses these titles in order:
SILENT, NIGHTFALL, SECRETS, HIDDEN, DOORWAYS, ECHOES.

The bookmark says 2, 1, 1, 2, 1, 1. decode_books loops through the titles,
subtracts 1 from each bookmark number, and takes that indexed letter.
Subtracting 1 is needed because Python indexing starts at 0.

decode_pin looks up the recovered word's letters in the letter_codes
dictionary. Its lambda uses number % 10 to keep the last digit.
It converts each digit to a string and joins the six digits.

The coffee table saves observations, it does not ask the player to guess
who left or why. The drawer reveals the key and photograph with the face
covered to highlight the phone case.

## Progress and notebook

- Saving the coffee observation completes one interaction.
- Solving the bookshelf completes one interaction.
- Solving the book completes one interaction.
- Unlocking the drawer completes one interaction.

All four are needed before continuing. Coffee can be saved at any point.
Saving the photograph adds evidence but does not add another progress point.
Continue to study saves it automatically if it has not already been saved.
Repeated saves do not add duplicate evidence or keys.

Closing popups, reading the notebook, and normal Streamlit reruns preserve
progress. A fresh browser session or browser reload can start a new game, restart level is in
the sidebar and clears the level's answers, evidence, and progress.

The normal scene and original puzzle screenshots are included. display.py
shows only each screenshot's close-up region using CSS, so its printed buttons
are not displayed. Actual inputs and buttons are Streamlit widgets. The dimmed
scene is included as a reference; the native popup backdrop provides dimming,
so the background is not darkened twice. The layout follows the chosen imagery;
native Streamlit controls can differ slightly from the mockup's typography.

## Try these checks

1. Submit an empty or wrong word. It should not increase progress.
2. Enter the correct word in lowercase. It should be accepted.
3. Try the PIN before solving the bookshelf. The earlier clue is required.
4. Try letters, a decimal, a sign, or a short PIN. It should reject the input.
5. Save an observation twice. Progress and notebook entries should not duplicate.
6. Solve the puzzles before saving coffee. Continue should wait for the observation.
7. Finish the room without pressing Save photograph. Continue should retain it.
8. Close/reopen the popup, then restart from the sidebar.

## Answers for development

Spoilers: the bookshelf word is INSIDE. The drawer PIN is 383389.
Both are calculated from the clues; the logic does not compare against
an unexplained hardcoded answer.

