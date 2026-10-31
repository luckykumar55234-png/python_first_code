from datetime import datetime


def display():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Signup")
        print("2. Login")
        print("3. Search")
        print("4. Date and Time")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                from python_first_code.signup.signup import signup
            except ModuleNotFoundError:
                from signup.signup import signup
            signup()

        elif choice == "2":
            try:
                from python_first_code.login.login import login
            except ModuleNotFoundError:
                from login.login import login
            login()

        elif choice == "3":
            try:
                from python_first_code.search.search import search
            except ModuleNotFoundError:
                from search.search import search
            search()

        elif choice == "4":
            print("Current Date and Time:", datetime.now())

        elif choice == "5":
            print("Program closed")
            break

        else:
            print("Invalid choice")
