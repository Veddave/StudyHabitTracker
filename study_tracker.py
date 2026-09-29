from datetime import datetime, timedelta
from storage import save_data


def add_study_session(data):
    print("\n================================")
    print("       ADD STUDY SESSION")
    print("================================")

    subject = input("Enter subject: ")
    topic = input("Enter topic: ")

    while True:
        date = input("Enter date (DD/MM/YYYY): ")
        try:
            datetime.strptime(date, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date. Use DD/MM/YYYY.")

    while True:
        start_time_input = input("Enter start time (HH:MM AM/PM): ")
        try:
            start_time = datetime.strptime(start_time_input, "%I:%M %p")
            break
        except ValueError:
            print("Invalid time. Example: 06:30 PM.")

    while True:
        try:
            duration = int(input("Enter duration in minutes: "))
            if duration <= 0:
                print("Duration must be greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a number.")

    end_time = start_time + timedelta(minutes=duration)

    session = {
        "subject": subject,
        "topic": topic,
        "date": date,
        "start_time": start_time.strftime("%I:%M %p"),
        "duration": duration,
        "end_time": end_time.strftime("%I:%M %p")
    }

    data["study_sessions"].append(session)
    save_data(data)
    print("\nStudy session added successfully!")


def view_study_sessions(data):
    print("\n================================")
    print("       VIEW STUDY SESSIONS")
    print("================================")

    sessions = data["study_sessions"]

    if not sessions:
        print("No study sessions found.")
        return

    for index, session in enumerate(sessions, start=1):
        print(f"\nSession {index}")
        print("-----------------------------")
        print(f"Subject:    {session['subject']}")
        print(f"Topic:      {session['topic']}")
        print(f"Date:       {session['date']}")
        print(f"Start Time: {session['start_time']}")
        print(f"End Time:   {session['end_time']}")
        print(f"Duration:   {session['duration']} minutes")


def edit_study_session(data):
    print("\n================================")
    print("       EDIT STUDY SESSION")
    print("================================")

    sessions = data["study_sessions"]

    if not sessions:
        print("No study sessions found.")
        return

    view_study_sessions(data)

    while True:
        try:
            number = int(input("\nEnter session number to edit: "))
            if 1 <= number <= len(sessions):
                break
            print("Invalid session number.")
        except ValueError:
            print("Please enter a number.")

    session = sessions[number - 1]

    print("\nEnter new values.")
    print("Press ENTER to keep the current value.")

    new_subject = input(f"\nSubject [{session['subject']}]: ")
    if new_subject.strip():
        session["subject"] = new_subject

    new_topic = input(f"Topic [{session['topic']}]: ")
    if new_topic.strip():
        session["topic"] = new_topic

    while True:
        new_date = input(f"Date [{session['date']}]: ")
        if not new_date.strip():
            break
        try:
            datetime.strptime(new_date, "%d/%m/%Y")
            session["date"] = new_date
            break
        except ValueError:
            print("Invalid date. Use DD/MM/YYYY.")

    while True:
        new_time = input(f"Start Time [{session['start_time']}]: ")
        if not new_time.strip():
            break
        try:
            start_time = datetime.strptime(new_time, "%I:%M %p")
            session["start_time"] = start_time.strftime("%I:%M %p")
            break
        except ValueError:
            print("Invalid time. Example: 06:30 PM.")

    while True:
        new_duration = input(f"Duration [{session['duration']} minutes]: ")
        if not new_duration.strip():
            break
        try:
            new_duration = int(new_duration)
            if new_duration <= 0:
                print("Duration must be greater than 0.")
                continue
            session["duration"] = new_duration
            break
        except ValueError:
            print("Please enter a number.")

    start_time = datetime.strptime(session["start_time"], "%I:%M %p")
    end_time = start_time + timedelta(minutes=session["duration"])
    session["end_time"] = end_time.strftime("%I:%M %p")

    save_data(data)
    print("\nStudy session updated successfully!")


def delete_study_session(data):
    print("\n================================")
    print("       DELETE STUDY SESSION")
    print("================================")

    sessions = data["study_sessions"]

    if not sessions:
        print("No study sessions found.")
        return

    view_study_sessions(data)

    while True:
        try:
            number = int(input("\nEnter session number to delete: "))
            if 1 <= number <= len(sessions):
                break
            print("Invalid session number.")
        except ValueError:
            print("Please enter a number.")

    session = sessions[number - 1]

    print("\nYou are about to delete:")
    print("-----------------------------")
    print(f"Subject:    {session['subject']}")
    print(f"Topic:      {session['topic']}")
    print(f"Date:       {session['date']}")
    print(f"Start Time: {session['start_time']}")
    print(f"Duration:   {session['duration']} minutes")
    print("-----------------------------")

    while True:
        confirmation = input(
            "\nAre you sure you want to delete this session? (y/n): "
        ).strip().lower()

        if confirmation == "y":
            sessions.pop(number - 1)
            save_data(data)
            print("\nStudy session deleted successfully!")
            break
        elif confirmation == "n":
            print("\nDeletion cancelled.")
            break
        else:
            print("Please enter y or n.")


def study_menu(data, show_progress):
    while True:
        print("\n================================")
        print("          STUDY TRACKER")
        print("================================")
        print("1. Add Study Session")
        print("2. View Study Sessions")
        print("3. Edit Study Session")
        print("4. Delete Study Session")
        print("5. Show Study Progress")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_study_session(data)
        elif choice == "2":
            view_study_sessions(data)
        elif choice == "3":
            edit_study_session(data)
        elif choice == "4":
            delete_study_session(data)
        elif choice == "5":
            show_progress(data, "study")
        elif choice == "6":
            break
        else:
            print("\nInvalid Study Tracker choice.")


if __name__ == "__main__":
    from storage import load_data
    from progress import show_progress
    study_menu(load_data(), show_progress)
