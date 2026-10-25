print("=== Shopping Bill Calculator ===")
items=[]
total=0
while True:
    name=input("Enter item name or 'done' to finish: ")
    if name.lower()=="done":
        break
    price=float(input("Enter item price:"))
    items.append((name,price))
    total+=price
print("\n==== SHOPPING BILL =====")
for name,price in items:
    print(f"{name}: Rs{price:.2f}")
print("---------------")
print(f"Total: Rs{total:.2f}")
if total>=1000:
    discount=total*0.10
    print(f"Discount (10%):Rs{discount:.2f}")
    total-=discount
print(f"Final Amount: Rs{total:.2f}")
print("Thank you for shopping!")