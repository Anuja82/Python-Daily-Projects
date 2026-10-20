def longest_consecutive(numbers):
    number_set=set(numbers)
    longest=0
    for number in number_set:
        if number -1 not in number_set:
            current=number
            length=1
            while current+1 in number_set:
                current+=1
                length+=1
                longest=max(longest,length)
    return longest
numbers=list(map(int,input("Enter numbers separated by spaces:").split()))
result=longest_consecutive(numbers)
print("Longest consecutive sequence length:",result)