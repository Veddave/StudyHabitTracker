from datetime import datetime, timedelta


def get_week_start(date):
    return date - timedelta(days=date.weekday())


def get_available_weeks(data):
    today = datetime.now().date()
    week_starts = {get_week_start(today)}

    for session in data["study_sessions"]:
        try:
            date = datetime.strptime(session["date"], "%d/%m/%Y").date()
            week_starts.add(get_week_start(date))
        except (ValueError, KeyError):
            pass

    for habit in data["habits"]:
        for date_string in habit.get("completed_dates", []):
            try:
                date = datetime.strptime(date_string, "%d/%m/%Y").date()
                week_starts.add(get_week_start(date))
            except ValueError:
                pass

    return sorted(week_starts)


def select_week(data):
    weeks = get_available_weeks(data)

    print("\n================================")
    print("          SELECT WEEK")
    print("================================")

    for index, week_start in enumerate(weeks, start=1):
        week_end = week_start + timedelta(days=6)
        print(
            f"{index}. {week_start.strftime('%d %b')} - "
            f"{week_end.strftime('%d %b %Y')}"
        )

    print(f"{len(weeks) + 1}. Back")

    while True:
        try:
            choice = int(input("\nSelect a week: "))

            if 1 <= choice <= len(weeks):
                return weeks[choice - 1]
            elif choice == len(weeks) + 1:
                return None

            print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")


def show_study_progress(data):
    week_start = select_week(data)

    if week_start is None:
        return

    week_end = week_start + timedelta(days=6)

    print("\n================================")
    print("       WEEKLY STUDY PROGRESS")
    print("================================")
    print(
        f"{week_start.strftime('%d %b')} - "
        f"{week_end.strftime('%d %b %Y')}"
    )

    daily_minutes = {}

    for i in range(7):
        day = week_start + timedelta(days=i)
        daily_minutes[day.strftime("%d/%m/%Y")] = 0

    for session in data["study_sessions"]:
        date_string = session["date"]
        if date_string in daily_minutes:
            daily_minutes[date_string] += session["duration"]

    daily_hours = []

    for i in range(7):
        day = week_start + timedelta(days=i)
        daily_hours.append(
            daily_minutes[day.strftime("%d/%m/%Y")] / 60
        )

    print()
    max_hours = max(daily_hours)

    if max_hours == 0:
        print("No study sessions recorded for this week.")
    else:
        graph_max = max(1, int(max_hours) + 1)

        for level in range(graph_max, 0, -1):
            line = f"{level:>3} |"

            for hours in daily_hours:
                line += "   ███   " if hours >= level else "         "

            print(line)

        print("    +" + "--------- " * 7)

        day_line = "      "
        date_line = "      "

        for i in range(7):
            day = week_start + timedelta(days=i)
            day_line += f"{day.strftime('%a'):^10}"
            date_line += f"{day.strftime('%d/%m'):^10}"

        print(day_line)
        print(date_line)

    print("\n--------------------------------")

    total_minutes = 0

    for i in range(7):
        day = week_start + timedelta(days=i)
        date_string = day.strftime("%d/%m/%Y")
        minutes = daily_minutes[date_string]
        total_minutes += minutes

        print(
            f"{day.strftime('%A'):10} "
            f"{day.strftime('%d/%m/%Y')} : "
            f"{minutes / 60:.2f} hours"
        )

    print("--------------------------------")
    print(f"Total study time: {total_minutes / 60:.2f} hours")


def show_habit_progress(data):
    week_start = select_week(data)

    if week_start is None:
        return

    week_end = week_start + timedelta(days=6)

    print("\n================================")
    print("        WEEKLY HABIT PROGRESS")
    print("================================")
    print(
        f"{week_start.strftime('%d %b')} - "
        f"{week_end.strftime('%d %b %Y')}"
    )

    if not data["habits"]:
        print("\nNo habits found.")
        return

    for habit in data["habits"]:
        completed_dates = habit.get("completed_dates", [])
        completed_count = 0

        print(f"\n{habit['name']}")
        print("--------------------------------")

        for i in range(7):
            day = week_start + timedelta(days=i)
            date_string = day.strftime("%d/%m/%Y")

            if date_string in completed_dates:
                symbol = "✓"
                completed_count += 1
            else:
                symbol = "✗"

            print(
                f"{day.strftime('%A'):10} "
                f"{day.strftime('%d/%m')} : {symbol}"
            )

        percentage = completed_count / 7 * 100
        filled = int(percentage / 10)
        bar = "█" * filled + "░" * (10 - filled)

        print(
            f"\nProgress: [{bar}] "
            f"{completed_count}/7 days ({percentage:.0f}%)"
        )


def show_progress(data, tracker_type):
    if tracker_type == "study":
        show_study_progress(data)
    elif tracker_type == "habit":
        show_habit_progress(data)
