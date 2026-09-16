expenses=[]
while True:
    print("\n--- Expense Tracker---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        name=input("Enter expense name:")
        amount=float(input("Enter amount:"))
        expenses.append({
            "name":name,
            "amount":amount
        })
        print("Expense added successfully!")
    elif choice=="2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}.{expense['name']}-Rs{expense['amount']:.2f}")
    elif choice=="3":
        total=sum(expense["amount"] for expense in expenses)
        print(f"Total Expense:Rs{total:.2f}")
    elif choice=="4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please try again.")