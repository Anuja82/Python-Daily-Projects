numbers=[1,2,2,3,1,2,4,3]
frequency={}
for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print("Numbers:",numbers)
print("\nFrequency:")
for number,count in frequency.items():
    print(number, "->", count)