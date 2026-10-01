balance=5000
while True:
    print("\n--- ATM ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("4. Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        print(f"Current Balance:Rs {balance:.2f}")
    elif choice=="2":
        amount=float(input("Enter deposit amount:Rs"))
        if amount>0:
           balance+=amount
           print(f"Rs{amount:.2f}deposited successfully!")
           print(f"New Balance:Rs{balance:.2f}")
        else:
           print("Enter a valid amount.")
    elif choice=="3":
        amount=float(input("Enter withdrawal amount:Rs."))
        if amount<=0:
            print("Enter a valid amount")
        elif amount>balance:
            print("Insufficient balance.")
        else:
          balance-=amount
          print(f"Rs{amount:.2f}withdrawn successfully!")
          print(f"Remaining Balance:Rs{balance:.2f}")
    elif choice== "4":
      print("Thankyou for using the ATM")
      break
    else:
        print("Invalid choice.Please try again.")

            
