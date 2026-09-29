# Study & Habit Tracker

## About the Project

Study & Habit Tracker is a small command-line program made in Python.

I made this project to keep track of my study sessions and habits in one place. The program lets me add and manage study sessions, keep a list of habits, mark habits as completed for different dates, and check weekly progress.

The project also saves the data in a JSON file. This means the saved information is still available when the program is closed and opened again.

## What the Program Does

### Study Tracker

The Study Tracker is used to record study sessions.

For each session, the program takes:

- Subject
- Topic
- Date
- Starting time
- Duration in minutes

The ending time is calculated automatically from the starting time and duration.

For example, if the starting time is 7:00 PM and the duration is 60 minutes, the program calculates the ending time as 8:00 PM.

Study sessions can also be viewed, edited, and deleted. Deleting a session requires confirmation.

The study progress option asks for a week and then shows the amount of study time for each day of that week.

### Habit Tracker

The Habit Tracker is used for habits that are meant to continue over time.

I can:

- Add a habit
- View habits
- Mark a habit as completed for a particular date
- Delete a habit
- View weekly habit progress

When a habit is completed, the completion date is stored. The same date is not added again if it has already been recorded.

### Progress

The program has separate progress views for study and habits.

For study progress, I first select a week. The program then adds the study duration for each day in that week and displays the result in the terminal.

For habit progress, I select a week and the program shows the completion status of each habit for the seven days of that week. It also shows how many days each habit was completed.

## How the Data is Stored

The saved data is kept in:

data/tracker_data.json

This file contains the study sessions and habits.

The program loads the data when it starts and saves it after changes such as adding, editing, deleting, or completing something.

## Python Concepts Used

This project uses concepts from Python that were useful for solving different parts of the problem, including:

- Variables and user input
- `if` conditions
- `while` loops
- `for` loops
- Functions
- Lists
- Dictionaries
- String handling
- Input validation
- `datetime` and `timedelta` for dates and times
- JSON file handling
- Python modules and imports

## Project Structure

The project is divided into separate files so that related parts of the program are kept together instead of putting everything into one large file.

StudyHabitTracker
│
├── main.py
├── study_tracker.py
├── habit_tracker.py
├── progress.py
├── storage.py
│
├── data/
│   └── tracker_data.json
│
├── README.md
└── statement.md

### File Overview

- `main.py`: starts the program and handles the main menu.
- `study_tracker.py`: contains the study session features.
- `habit_tracker.py`: contains the habit features.
- `progress.py`: handles the weekly progress calculations and display.
- `storage.py`: handles loading and saving the data.
- `data/tracker_data.json`: stores the saved study and habit data.
- `statement.md`: contains the project statement and basic project description.

## Technologies Used

The project is made using Python.

It uses Python's standard library, including:

```python
datetime
json
os
```

No external Python packages are required to run the project.

## How to Run

1. Make sure Python is installed on the computer.
2. Open the `StudyHabitTracker` folder in VS Code.
3. Open a terminal in the same folder.
4. Run:

```bash
python main.py
```

The main menu will then appear in the terminal.

## Testing

I tested the project by running it from the terminal and using the different menu options.

The main things I checked were:

- Adding and viewing study sessions
- Editing study sessions
- Deleting study sessions with confirmation
- Adding and viewing habits
- Marking habits as completed
- Deleting habits with confirmation
- Viewing weekly study progress
- Viewing weekly habit progress
- Entering invalid dates, times, and durations
- Closing and reopening the program to check that saved data is loaded again

## Limitations

This version of the project is command-line based, so it does not have a graphical user interface.

The progress is displayed as text in the terminal instead of using external chart libraries.

## Possible Future Improvements

Some improvements that could be added in a future version are:

- A graphical interface
- More detailed progress statistics
- Habit reminders
- More ways to filter and view study sessions
- Exporting progress into a separate report

## Project Purpose

The main purpose of this project was to use Python concepts to build a practical program that I could actually use for tracking study and habits.
