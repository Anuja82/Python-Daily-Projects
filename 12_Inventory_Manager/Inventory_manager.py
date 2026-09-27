inventory={}
while True:
    print("\n--- Inventory Manager---")
    print("1. Add Product")
    print("2. View Product")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Delete Product")
    print("6. Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        name=input("Enter product name:")
        price=float(input("Enter product price: Rs"))
        quantity=int(input("Enter quantity:"))
        inventory[name]={
            "price":price,
            "quantity":quantity,
        }
        print("Product added successfully!")
    elif choice=="2":
        if not inventory:
            print("No products found.")
        else:
            print("\n--- products---")
            for name, details in inventory.items():
                print(
                    f"{name}-Rs{details['price']:.2f}"
                      f"-Quantity:{details["quantity"]}")
    elif choice=="3":
        name=input("Enter product name to search:")
        if name in inventory:
           details=inventory[name]
           print(f"Product:{name}")
           print(f"Price:Rs{details['price']:.2f}")
           print(f"Quantity:{details['quantity']}")
        else:
            print("Product not found.")
    elif choice=="4":
        name=input("Enter product name:")
        if name in inventory:
                quantity=int(input("Enter new quantity:"))
                inventory[name]["quantity"]=quantity
                print("Quantity updated successfully!")
        else:
             print("Product not found.")
    elif choice=="5":
        name=input("Enter product name to delete:")
        if name in inventory:
           del inventory[name]
           print("Product deleted successfully!")
        else:
           print("Product not found.")
    elif choice=="6":
       print("Goodbye! 👋")
       break
    else:
        print("Invalid choice. Please try again.")
           
                                   
    