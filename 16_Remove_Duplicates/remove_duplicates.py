numbers=[1,2,2,3,4,4,5,1,3]
unique_numbers=[]
for number in numbers:
    if number not in unique_numbers:
     unique_numbers.append(number)
print("Original list:",numbers)
print("Unique list:",unique_numbers)
