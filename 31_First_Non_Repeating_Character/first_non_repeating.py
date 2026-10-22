def first_non_repeating(text):
    for char in text:
        if text.count(char)==1:
            return char
        return None
text=input("Enter a String:")
result=first_non_repeating(text)
if result is not None:
    print("First non-repeating character:",result)
else:
    print("No non-repeating character found.")