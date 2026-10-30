
notes = []

def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    if not title or not content:
        print("Title and content cannot be empty.")
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

def main():
    while True:
        print("\n===== CampusNotes =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
notes.append({"title": title, "content": content})