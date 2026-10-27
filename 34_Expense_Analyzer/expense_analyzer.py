print("=== Personal Expense Analyzer ===")
expenses={}
while True:
    category=input("\nEnter expense category (or 'done' to finish):")
    if category.lower()=="done":
        break
    try:
        amount=float(input("Enter amount:"))
        if amount<=0:
            print("Please enter an amount greater than zero.")
            continue
        expenses[category]=expenses.get(category,0)+amount
    except ValueError:
        print("Please enter a valid number.")
if expenses:
    print("\n=== Expense Summary ===")
    total=sum(expenses.values())
    for category, amount in expenses.items():
        percentage=(amount/total)*100
        print(f"{category}:Rs.{amount:.2f}({percentage:.1f}%)")
    print("---------------------")
    print(f"Total Expenses: Rs. {total:.2f}")
    print(f"Highest Spending:{max(expenses,key=expenses.get)}")
else:
    print("No expenses recorded")
