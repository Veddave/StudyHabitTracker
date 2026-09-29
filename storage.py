import json
import os

DATA_FILE = os.path.join("data", "tracker_data.json")


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)

            data.setdefault("study_sessions", [])
            data.setdefault("habits", [])
            return data

        except (json.JSONDecodeError, OSError):
            print("\nCould not read saved data. Starting with empty data.")

    return {"study_sessions": [], "habits": []}


def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
