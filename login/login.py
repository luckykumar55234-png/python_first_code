import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data.json"


def login():
    try:
        email = input("Enter email: ").strip()
        password = input("Enter password: ")

        if not DATA_FILE.exists():
            print("data.json file not found")
            return

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            print("No student data found")
            return

        if email in data:
            if data[email]["password"] == password:
                data[email]["login_date_time"] = str(datetime.now())

                with open(DATA_FILE, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4)

                print("Login successful")
                print("Welcome", data[email]["name"])
            else:
                print("Wrong password")
        else:
            print("Email not registered")

    except FileNotFoundError:
        print("data.json file not found")

    except Exception as e:
        print("Error:", e)
