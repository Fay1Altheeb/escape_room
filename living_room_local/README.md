# The Last Door — Local Living Room

This is a standalone local version of Chapter 2. It starts in the living room
and ends when the study door is unlocked. It does not need the team's GitHub
repository or a hosting account to run.

## Run it on Windows with VS Code

1. Download and extract Living_Room_Local.zip.
2. Open VS Code. Choose File → Open Folder and select living_room_local.
   You should see app.py, room_2.py, requirements.txt, and assets in that folder.
3. Choose Terminal → New Terminal. The terminal must be in this folder.
4. Install Streamlit and start the app:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

5. Open the Local URL printed in the terminal, usually http://localhost:8501.
   Keep the terminal running. Press Ctrl+C in that terminal to stop the app.

Use the commands above instead of VS Code's Run Python File button for app.py.
If Windows does not recognize python but recognizes py, replace python with py.
Python 3.12 is the version used for testing.

If you want a separate environment, use these commands instead:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

These commands do not require activating the environment in PowerShell.
In VS Code, Python: Select Interpreter lets you select this .venv interpreter.

For the terminal version, run:

```powershell
python console_room_2.py
```

It uses input() and print(), and calls the same puzzle functions as the web app.

## Read the code in this order

| File | What to read there |
| --- | --- |
| room_2.py | The lists, dictionaries, loops, functions, and game decisions |
| console_room_2.py | A simple menu using input(), print(), if/elif/else, and while |
| app.py | How Streamlit buttons and fields call the game functions |
| display.py and style.css | Picture display and interface appearance |

The puzzle logic uses ordinary Unit 1 Python. There are no classes, type hints,
regular expressions, databases, API calls, or advanced puzzle frameworks.
Functions usually return two things: success (True/False) and a message.
For example, success, message = room.submit_word(answer, game) receives them.

Streamlit, its dialog decorator, and session state belong to the interface
layer. They are new framework APIs, not puzzle algorithms from the slides.
os and base64 in display.py are only used to find and display local images.
The CSS controls appearance. You can study room_2.py before these display files.

## How the puzzles work

The bookshelf uses these titles in order:
SILENT, NIGHTFALL, SECRETS, HIDDEN, DOORWAYS, ECHOES.

The bookmark says 2, 1, 1, 2, 1, 1. decode_books loops through the titles,
subtracts 1 from each bookmark number, and takes that indexed letter.
Subtracting 1 is needed because Python indexing starts at 0.

decode_pin looks up the recovered word's letters in the letter_codes
dictionary. Its lambda uses number % 10 to keep the last digit.
It converts each digit to a string and joins the six digits.

The coffee table saves observations; it does not ask the player to guess
who left or why. The drawer reveals the key and photograph with the face
covered. The phone case and scratch remain visible.

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
progress. A fresh browser session or browser reload can start a new game;
this version does not write a permanent saved game. Restart level is in
the sidebar and clears the level's answers, evidence, and progress.

The local phone panel has no messages. The team's final dialogue was not in
the starter repository, so this build does not invent story messages. The map
shows the room sequence and applies the same study-access rule as the drawer.
The study completion screen marks the handoff; the other levels are not included.

The normal scene and original puzzle screenshots are included. display.py
shows only each screenshot's close-up region using CSS, so its printed buttons
are not displayed. Actual inputs and buttons are Streamlit widgets. The dimmed
scene is included as a reference; the native popup backdrop provides dimming,
so the background is not darkened twice. The layout follows the chosen imagery;
native Streamlit controls can differ slightly from the mockup's typography.

## Unit 1 project requirements

| Requirement | Example in this project |
| --- | --- |
| At least three data types | Strings, integers, booleans, lists, dictionaries |
| Collection | book_titles, letter_codes, inventory, notebook |
| if, elif, else | Answer validation, terminal menu, and prerequisites |
| for or while | Word/PIN calculations, progress, terminal menu |
| Function with parameters and return value | decode_books, decode_pin, submit_word |
| Lambda | last_digit = lambda number: number % 10 |
| input() | console_room_2.py |
| print() | console_room_2.py |
| Comments | Explanations beside the rules and important steps |
| Reflection | Prompts at the bottom of room_2.py for your own answers |

Deployment/sharing is a later project requirement. This package only runs
locally, as requested; it has not been deployed or pushed to the team repo.

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

## Later team integration

Move room_2.py into game/rooms/ and update the imports when integrating.
Keep the shared player name, inventory, notebook, and room routing consistent
with the other levels. This local game dictionary is limited to this level;
it should not overwrite the other rooms' state in the integrated app.

Official Streamlit references:
- https://docs.streamlit.io/get-started/installation/command-line
- https://docs.streamlit.io/develop/api-reference/execution-flow/st.dialog
- https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state

