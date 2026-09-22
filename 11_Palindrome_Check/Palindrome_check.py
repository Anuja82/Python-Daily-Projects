text=input("Enter a word::").lower()
is_palindrome=True
for i in range(len(text)//2):
    if text[i]!=text[len(text)-1-i]:
        is_palindrome=False
        break
if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")