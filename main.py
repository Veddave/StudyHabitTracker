from storage import load_data
from study_tracker import study_menu
from habit_tracker import habit_menu
from progress import show_progress


def main():
    data = load_data()

    while True:
        print("\n================================")
        print("       STUDY & HABIT TRACKER")
        print("================================")
        print("1. Study Tracker")
        print("2. Habit Tracker")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            study_menu(data, show_progress)
        elif choice == "2":
            habit_menu(data, show_progress)
        elif choice == "3":
            print("\nExiting program...")
            break
        else:
            print("\nInvalid Main Menu choice.")


if __name__ == "__main__":
    main()
