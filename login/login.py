
import json
from datetime import datetime

def login():
    try:
        email = input("Enter email: ")
        password = input("Enter password: ")

        with open("data.json", "r") as file:
            data = json.load(file)

        if email in data:
            if data[email]["password"] == password:
                data[email]["login_date_time"] = str(datetime.now())

                with open("data.json", "w") as file:
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
