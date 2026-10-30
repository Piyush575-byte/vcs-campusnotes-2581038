
notes = []


def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    if not title or not content:
        print("Title and content cannot be empty.")
        return

    if any(note["title"].lower() == title.lower() for note in notes):
        print("A note with this title already exists.")
        return

    notes.append({"title": title, "content": content})
    print("Note added successfully!")


def view_notes():
    if not notes:
        print("No notes available.")
        return

    for index, note in enumerate(notes, start=1):
        print(f"\n{index}. {note['title']}")
        print(note["content"])


def display_menu():
    print("\n===== CampusNotes =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")


def main():
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        actions = {
            "1": add_note,
            "2": view_notes,
        }

        if choice == "3":
            print("Goodbye!")
            break

        action = actions.get(choice)

        if action:
            action()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
