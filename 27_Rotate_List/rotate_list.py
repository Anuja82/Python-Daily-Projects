def rotate_list(numbers,k):
    if not numbers:
        return numbers
    k=k%len(numbers)
    return numbers[-k:]+numbers[:-k]
numbers=list(map(int,input("Enter numbers separated by spaces:").split()))
k=int(input("Enter the number of positions to rotate:"))
result=rotate_list(numbers,k)
print("Rotated list:",result)