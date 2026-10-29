import uuid
import json
import re
from datetime import datetime

def signup():
    

    try:
        id = str(uuid.uuid4())[:6]
        name = input("Enter name: ")
        email = input("Enter email: ")
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

        qualifications = qualification.split(",")

        with open("data.json", "r") as file:
            data = json.load(file)

        if email in data:
            print("Email already registered")
            return

        data = {
            "id":id,
            "name": name,
            "email": email,
            "password": password,
            "age": age,
            "qualifications": qualifications,
            "signup_date_time": str(datetime.now())
        }

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Signup successful")

    except FileNotFoundError:
        print("data.json file not found")


    except Exception as e:
        print("Error",e)




