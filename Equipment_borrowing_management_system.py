borrow_records = []

def borrow_equipment():
    user = input("Enter user name: ")
    equipment = input("Enter equipment name: ")
    date = input("Enter borrowing date: ")
    borrow_records.append({
        "user": user,
        "equipment": equipment,
        "date": date
    })
    print("Equipment borrowing recorded")

def view_records():
    if not borrow_records:
        print("No borrowing records found")
    else:
        for r in borrow_records:
            print("User:", r["user"])
            print("Equipment:", r["equipment"])
            print("Date:", r["date"])
            print("------------------")

def main():
    while True:
        print("1. Borrow Equipment")
        print("2. View Borrow Records")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            borrow_equipment()
        elif choice == "2":
            view_records()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
