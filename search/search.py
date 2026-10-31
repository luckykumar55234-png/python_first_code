import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data.json"


def search():
    try:
        email = input("Enter student email to search: ").strip()

        if not DATA_FILE.exists():
            print("data.json file not found")
            return

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            print("No student data found")
            return

        if email in data:
            student = data[email]
            print("Student Found")
            print("Name:", student["name"])
            print("Email:", student["email"])
            print("Age:", student["age"])
            print("Qualifications:", student["qualifications"])
            print("Signup Date & Time:", student["signup_date_time"])
        else:
            print("Student not found")

    except FileNotFoundError:
        print("data.json file not found")

    except Exception as e:
        print("Error:", e)
