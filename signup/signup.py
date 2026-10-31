import json
import re
import uuid
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data.json"


def load_data():
    if not DATA_FILE.exists():
        return {}

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        return {}
    return data


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def signup():
    try:
        student_id = str(uuid.uuid4())[:6]
        name = input("Enter name: ").strip()
        email = input("Enter email: ").strip()
        password = input("Enter password: ")
        age = int(input("Enter age: "))
        qualification = input("Enter qualifications separated by comma: ")

        if name == "":
            print("Name cannot be empty")
            return

        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            print("Invalid email")
            return

        if len(password) < 6:
            print("Password must be at least 6 characters")
            return

        if age <= 0:
            print("Invalid age")
            return

        qualifications = [q.strip() for q in qualification.split(",") if q.strip()]

        data = load_data()

        if email in data:
            print("Email already registered")
            return

        data[email] = {
            "id": student_id,
            "name": name,
            "email": email,
            "password": password,
            "age": age,
            "qualifications": qualifications,
            "signup_date_time": str(datetime.now()),
        }

        save_data(data)
        print("Signup successful")

    except ValueError:
        print("Age must be a valid number")

    except FileNotFoundError:
        print("data.json file not found")

    except Exception as e:
        print("Error:", e)

