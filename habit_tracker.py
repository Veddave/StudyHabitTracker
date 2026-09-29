from datetime import datetime
from storage import save_data


def add_habit(data):
    print("\n================================")
    print("          ADD HABIT")
    print("================================")

    name = input("Enter habit name: ")

    if not name.strip():
        print("Habit name cannot be empty.")
        return

    data["habits"].append({
        "name": name,
        "completed_dates": []
    })

    save_data(data)
    print("\nHabit added successfully!")


def view_habits(data):
    print("\n================================")
    print("          VIEW HABITS")
    print("================================")

    habits = data["habits"]

    if not habits:
        print("No habits found.")
        return

    for index, habit in enumerate(habits, start=1):
        print(f"\n{index}. {habit['name']}")

        completed_dates = habit.get("completed_dates", [])

        if not completed_dates:
            print("   No completed dates yet.")
            continue

        print("   Completed:")

        for date in sorted(completed_dates):
            try:
                formatted_date = datetime.strptime(
                    date, "%d/%m/%Y"
                ).strftime("%A, %d/%m/%Y")
            except ValueError:
                formatted_date = date

            print(f"   ✓ {formatted_date}")


def delete_habit(data):
    print("\n================================")
    print("          DELETE HABIT")
    print("================================")

    habits = data["habits"]

    if not habits:
        print("No habits found.")
        return

    view_habits(data)

    while True:
        try:
            number = int(input("\nEnter habit number to delete: "))
            if 1 <= number <= len(habits):
                break
            print("Invalid habit number.")
        except ValueError:
            print("Please enter a number.")

    habit = habits[number - 1]

    print("\nYou are about to delete:")
    print("-----------------------------")
    print(f"Habit: {habit['name']}")
    print("-----------------------------")

    while True:
        confirmation = input(
            "\nAre you sure you want to delete this habit? (y/n): "
        ).strip().lower()

        if confirmation == "y":
            habits.pop(number - 1)
            save_data(data)
            print("\nHabit deleted successfully!")
            break
        elif confirmation == "n":
            print("\nDeletion cancelled.")
            break
        else:
            print("Please enter y or n.")


def mark_habit_complete(data):
    print("\n================================")
    print("       MARK HABIT COMPLETE")
    print("================================")

    habits = data["habits"]

    if not habits:
        print("No habits found.")
        return

    for index, habit in enumerate(habits, start=1):
        print(f"{index}. {habit['name']}")

    while True:
        try:
            number = int(input("\nEnter habit number: "))
            if 1 <= number <= len(habits):
                break
            print("Invalid habit number.")
        except ValueError:
            print("Please enter a number.")

    habit = habits[number - 1]

    while True:
        date = input("Enter completion date (DD/MM/YYYY): ")
        try:
            datetime.strptime(date, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date. Use DD/MM/YYYY.")

    completed_dates = habit.setdefault("completed_dates", [])

    if date in completed_dates:
        print("\nThis habit is already marked complete for this date.")
        return

    completed_dates.append(date)
    save_data(data)

    formatted_date = datetime.strptime(
        date, "%d/%m/%Y"
    ).strftime("%A, %d/%m/%Y")

    print(f"\n✓ {habit['name']} completed on {formatted_date}")


def habit_menu(data, show_progress):
    while True:
        print("\n================================")
        print("          HABIT TRACKER")
        print("================================")
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Delete Habit")
        print("4. Mark Habit as Complete")
        print("5. Show Habit Progress")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_habit(data)
        elif choice == "2":
            view_habits(data)
        elif choice == "3":
            delete_habit(data)
        elif choice == "4":
            mark_habit_complete(data)
        elif choice == "5":
            show_progress(data, "habit")
        elif choice == "6":
            break
        else:
            print("\nInvalid Habit Tracker choice.")


if __name__ == "__main__":
    from storage import load_data
    from progress import show_progress
    habit_menu(load_data(), show_progress)
