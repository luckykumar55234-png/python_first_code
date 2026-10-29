
import json

def search():
    try:
        email = input("Enter student email to search: ")

        with open("data.json", "r") as file:
            data = json.load(file)

        if email in data:
            print("Student Found")
            print("Name:", data[email]["name"])
            print("Email:", data[email]["email"])
            print("Age:", data[email]["age"])
            print("Qualifications:", data[email]["qualifications"])
            print("Signup Date & Time:", data[email]["signup_date_time"])

        else:
            print("Student not found")

    except FileNotFoundError:
        print("data.json file not found")

    except Exception as e:
        print("Error:", e)
