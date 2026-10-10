numbers=[1,2,4,5,6]
n=len(numbers)+1
expected_sum=n*(n+1)//2
actual_sum=sum(numbers)
missing_number=expected_sum-actual_sum
print("Number:",numbers)
print("Missing number:",missing_number)