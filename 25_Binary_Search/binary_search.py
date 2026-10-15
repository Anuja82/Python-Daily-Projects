def binary_search(numbers,target):
    left=0
    right=len(numbers)-1
    while left<=right:
        mid=(left+right)//2
        if numbers[mid]==target:
            return mid
        elif numbers[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
numbers=list(map(int, input("Enter sorted numbers seprated by spaces: ").split()))
target=int(input("Enter the number to search:"))
result=binary_search(numbers,target)
if result!=-1:
    print("Number found at index:",result)
else:
    print("Number not found.")