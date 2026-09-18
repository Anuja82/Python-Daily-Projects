print("🎓 Student Grade Calculator")
print()
name=input("Enter student name:")
marks=[]
for i in range(1,6):
    mark=float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)
total=sum(marks)
average=total/5
if average>=90:
    grade="A+"
elif average>=80:
    grade="A"
elif average>=70:
    grade="B"
elif average>=60:
    grade="C"
elif average>=50:
    grade="D"
else:
    grade="F"
print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:",total)
print("Average:", round(average,2))
print("Grade:", grade)