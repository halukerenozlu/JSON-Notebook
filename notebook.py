import os
import datetime
import json

path = '--------------'

file_name = os.path.join(path, "notes.json")


def initialize_file():
    if not os.path.exists(file_name):
        data = {"my notes": []}
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, dict) or "my notes" not in data:
                raise ValueError("Invalid JSON structure")
        except (json.JSONDecodeError, ValueError):
            data = {"my notes": []}
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)


def delete_notes():
    global file_name

    if not os.path.exists(file_name):
        print(f"{file_name} not found. Cannot delete notes.")
        return

    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)

    # The data is expected to be in dictionary format and
    # contain the key "my notes".
    if not isinstance(data, dict) or "my notes" not in data:
        print("notes.json is not in the expected format \
              (dictionary with 'my notes').")
        return

    notes = data.get("my notes", [])
    if not isinstance(notes, list) or not notes:
        print("No notes found. Unable to delete.")
        return

    # Mevcut notları listele
    print("Existing Notes:")
    for i, note in enumerate(notes):
        print(f"{i}. Date: {note['date']} | Content: {note['content']}")

    # Get the index of the note to be deleted from the user
    while True:
        try:
            index_str = input(
                "Enter the number of the note you want to  \
                (leave empty to cancel): ")
            if index_str.strip() == "":
                print("Delete operation canceled.")
                return

            index = int(index_str)
            if 0 <= index < len(notes):
                break
            else:
                print(
                    f"Invalid index. \
                    Enter a value between 0 and {len(notes)-1}.")
        except ValueError:
            print("Please enter an integer or press Enter to cancel.")

    # Delete selected note from list
    deleted_note = notes.pop(index)
    print(
        f"Deleted note: Date: {deleted_note['date']} | \
        Content: {deleted_note['content']}")

    # Transfer the updated list to the original dictionary and write to file
    data["my notes"] = notes
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Note deleted successfully!")


def add_note():
    global file_name
    initialize_file()

    new_note = input("Please enter your note: ")
    now = datetime.datetime.now().replace(microsecond=0)
    date_str = str(now)

    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)

    note_entry = {
        "date": date_str,
        "content": new_note
    }
    data["my notes"].append(note_entry)

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Note added successfully!")


def update_notes():
    global file_name

    if not os.path.exists(file_name):
        print(f"{file_name} not found. Cannot update notes.")
        return

    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)

    # data is expected to be a dictionary
    if not isinstance(data, dict):
        print("notes.json is not in the expected format \
              (dictionary with 'my notes').")
        return

    notes = data.get("my notes", [])
    if not isinstance(notes, list):
        print("notes.json is not in the expected format (list).")
        return

    if not notes:
        print("No notes found. Unable to update.")
        return

    print("Existing Notes:")
    for i, note in enumerate(notes):
        print(f"{i}. Date: {note['date']} | Content: {note['content']}")

    while True:
        try:
            index_str = input(
                "Enter the number of the note you want to update \
                (leave empty to cancel): ")
            if index_str.strip() == "":
                print("Update operation canceled.")
                return

            index = int(index_str)
            if 0 <= index < len(notes):
                break
            else:
                print(
                    f"Invalid index. \
                    Enter a value between 0 and {len(notes)-1}.")
        except ValueError:
            print("Please enter an integer or press Enter to cancel.")

    print(f"Current content of the selected note: {notes[index]['content']}")
    new_content = input("Enter new note content: ")

    notes[index]["content"] = new_content
    notes[index]["date"] = str(datetime.datetime.now().replace(microsecond=0))

    data["my notes"] = notes
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Note updated successfully!")


def search_notes():
    if not os.path.exists(file_name):
        print("Error: notes.json file does not exist.")
        print("Please choose option 2 (Add Note) to create the file.")
        return
    try:
        files = os.listdir(path)
    except FileNotFoundError:
        print(f"{path} directory not found.")
        return
    except OSError as e:
        print("An error occurred while reading the directory:", e)
        return

    found = False
    for fname in files:
        if fname.endswith('.json') and fname == "notes.json":
            print("The file: notes.json, you were looking for was found.")
            found = True
            break
    if not found:
        raise FileNotFoundError("notes.json was not found in this directory.")


def list_notes():
    global file_name

    if not os.path.exists(file_name):
        print(f"{file_name} not found.")
        return

    with open(file_name, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("The JSON file is empty or contains invalid data.")
            return

    # Prints JSON data with indents
    json_output = json.dumps(data, ensure_ascii=False, indent=4)
    print(json_output)


def main_menu():
    print("--------------------------------")
    print(" Welcome to your JSON Notebook! ")
    print("--------------------------------")
    current_time = datetime.datetime.now().replace(microsecond=0)
    print(current_time)
    while True:
        print("\nTransaction List:")
        print("1. Search My Notes")
        print("2. Add Note")
        print("3. List My Notes")
        print("4. Update My Note")
        print("5. Delete My Note")
        print("6. Exit")

        choice = input("Please select a transaction: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            search_notes()
        elif choice == 2:
            add_note()
        elif choice == 3:
            list_notes()
        elif choice == 4:
            update_notes()
        elif choice == 5:
            delete_notes()
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main_menu()
