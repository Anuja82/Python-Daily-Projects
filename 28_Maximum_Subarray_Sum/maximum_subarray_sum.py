def max_subarray_sum(numbers):
    current_sum=numbers[0]
    maximum_sum=numbers[0]
    for i in range(1,len(numbers)):
        current_sum=max(numbers[i],current_sum+numbers[i])
        maximum_sum=max(maximum_sum,current_sum)
    return maximum_sum
numbers=list(map(int,input("Enter numbers separated by spaces:").split()))
if numbers:
    result=max_subarray_sum(numbers)
    print("Maximum subarray sum:",result)
else:
    print("Please enter at least one number.")