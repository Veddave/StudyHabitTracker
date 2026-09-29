# Study & Habit Tracker - Project Statement

## Project Title

Study & Habit Tracker

## Course

Python Essentials 

---

## 1. Problem Statement

As a student, I have to manage both my studies and different habits. It can be difficult to remember what I studied, how much time I spent studying, and whether I followed a particular habit on a certain day.

I wanted to make a simple program where I could keep this information in one place. The program allows me to record study sessions, keep track of habits, and check my progress for a particular week.

The main idea of the project is to make a simple command-line tracker that helps a student maintain a record of their study and habit-related activities.

---

## 2. Scope of the Project

The project is a command-line application made using Python.

The Study Tracker allows the user to:

- Add study sessions
- View saved study sessions
- Edit study sessions
- Delete study sessions
- Enter the subject, topic, date, start time, and duration
- Automatically calculate the ending time
- View weekly study progress

The Habit Tracker allows the user to:

- Add habits
- View habits
- Delete habits
- Mark habits as completed for a particular date
- View weekly habit progress

The project also saves the data in a JSON file so that the information is available even after the program is closed.

The current version does not include a graphical interface, online storage, reminders, or multiple users.

---

## 3. Target Users

The main users of this project are students who want a simple way to keep track of their study sessions and regular habits.

It can help a student keep track of:

- What they studied
- How long they studied
- Which habits they completed
- Their study progress during a week
- Their habit completion during a week

The current project is mainly designed for personal use by one user.

---

## 4. High-Level Features

### Study Tracking

The user can record study sessions by entering the subject, topic, date, starting time, and duration. The program calculates the ending time automatically. Sessions can also be viewed, edited, and deleted.

### Habit Tracking

The user can create habits and mark them as completed on different dates. Habits can also be viewed and deleted.

### Weekly Progress

The user can select a week and view study time for each day. Habit progress can also be checked for the selected week.

### Data Storage

Study sessions and habits are stored in:

`data/tracker_data.json`

This allows the data to be loaded again when the program is started.

### Input Validation

The program checks inputs such as dates, times, and study duration to reduce incorrect entries.

---

## 5. Python Concepts Used

The project uses concepts such as:

- Functions
- Lists
- Dictionaries
- Loops
- Conditional statements
- Input validation
- datetime
- JSON file handling
- Python modules