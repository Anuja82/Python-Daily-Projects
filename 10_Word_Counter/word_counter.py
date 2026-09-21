print("📝 Word Counter")
print()
text=input("Enter a Sentence:")
words=text.split()
word_count=len(words)
character_count=len(text)
vowels=0
consonants=0
for char in text.lower():
    if char.isalpha():
        if char in "aeiou":
            vowels+=1
        else:
            consonants+=1
print("\n--- Result ---")
print("Word:", word_count)
print("Characters:",character_count)
print("Vowels:", vowels)
print("Consonants:",consonants)
