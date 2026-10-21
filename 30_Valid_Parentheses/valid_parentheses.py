def is_valid_parantheses(text):
    stack=[]
    pairs={
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for char in text:
        if char in "([{":stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1]!=pairs[char]:
                return False
            stack.pop()
    return len(stack)==0
text=input("Enter parentheses:")
if is_valid_parantheses(text):
    print("Valid parentheses")
else:
    print("Invalid parentheses")