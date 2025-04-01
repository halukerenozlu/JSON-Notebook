import os
import datetime
# import json

path = 'C:\\Users\\hlker\\Desktop\\py_uygulama'


def delete_notes():
    pass


def create_notes():
    pass


def update_notes():
    pass


def search_notes():
    try:
        files = os.listdir(path)
    except FileNotFoundError:
        print(f"{path} directory not found.")
        return
    except OSError as e:
        print("An error occurred while reading the directory:", e)
        return

    found = False
    for file_name in files:
        if file_name.endswith('.json') and file_name == "notes.json":
            print(f"The file: {"notes.json"}, you were looking for was found.")
            found = True
            break
    if not found:
        raise FileNotFoundError("notes.json was not found in this directory.")


current_time = datetime.datetime.now().replace(microsecond=0)
print(current_time)

while True:
    print("\nTransaction List:")
    print("1. Search My Notes")
    print("2. Create Note")
    print("3. Update My Note")
    print("4. Delete My Note")
    print("5. Exit")

    choice = input("Please select a transaction: ")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        search_notes()
    elif choice == 2:
        create_notes()
    elif choice == 3:
        update_notes()
    elif choice == 4:
        delete_notes()
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
        continue
