def add_note():
    note=input("Enter your note:")
    with open("notes.txt","a") as file:
        file.write(note+"\n")
    print("Not added successfully!")
def view_notes():
    try:
        with open("notes.txt","r") as file:
            notes=file.readlines()
        if not notes:
            print("No notes found.")
        else:
            print("\n--- Your Notes ---")
            for i,note in enumerate(notes,start=1):
                print(f"{i}.{note.strip()}")
    except FileNotFoundError:
        print("No notes found.")
def search_notes():
    keyword=input("Enter keyword to search:").lower()
    try:
        with open("notes.txt","r") as file:
            notes=file.readlines()
        found=False
        for i, note in enumerate(notes,start=1):
            if keyword in note.lower():
                print(f"{i}.{note.strip()}")
                found=True
        if not found:
            print("No matching notes found.")
    except FileNotFoundError:
        print("No notes found.")
def delete_all_notes():
    with open("notes.txt","w") as file:
        file.write("")
    print("All notes deleted successfully!")
while True:
    print("\n--- Notes Manager ---")
    print("1. HaAdd Note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Delete All Notes")
    print("5. Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        add_note()
    elif choice=="2":
        view_notes()
    elif choice=="3":
        search_notes()
    elif choice=="4":
        delete_all_notes()
    elif choice=="5":
        print("Goodbye!👋")
        break
    else:
        print("Invalid choice. Please try again.")
