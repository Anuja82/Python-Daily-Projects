print("🔢 Number Analyzer")
print()
user_input=input("Enter numbers separated by spaces:")
numbers=[int(number) for number in user_input.split()]
total_numbers=len(numbers)
total_numbers=len(numbers)
total_sum=sum(numbers)
average=total_sum/total_numbers
largest=max(numbers)
smallest=min(numbers)
even_numbers=[]
odd_numbers=[]
for number in numbers:
    if number%2==0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print("\n-- Result --")
print("Numbers:", numbers)
print("Total numbers:",total_numbers)
print("Sum:",total_sum)
print("Average:",average)
print("Largest:",largest)
print("Smallest:", smallest)
print("Even numbers:",even_numbers)
print("Odd numbers:",odd_numbers)