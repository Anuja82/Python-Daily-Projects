def are_anagrams(word1,word2):
    word1=word1.replace("","").lower()
    word2=word2.replace("","").lower()
    if sorted(word1)==sorted(word2):
        return True
    return False
first_word=input("Enter the first word:")
second_word=input("Enter the second word:")
if are_anagrams(first_word,second_word):
    print("The words are anagrams!")
else:
    print("The words are not anagrams.")