import time
import random
sentences=[
    "Python is a powerful programming language",
    "Practice coding every day to improve skills",
    "Learning programming opens many career opportunities",
    "Consistency is the key to becoming a developer"
]
sentence=random.choice(sentences)
print("==== Typing Speed Tester ====")
print("\nType the following sentence:")
print(sentence)
input("\nPress Enter when you are ready to start...")
start_time=time.time()
typed_text=input("\nStart typing:")
end_time=time.time()
time_taken=end_time-start_time
words=len(typed_text.split())
minutes=time_taken/60
if minutes>0:
    wpm=words/minutes
else:
    wpm=0
print("\n==== Your Results =====")
print(f"Time taken:{time_taken:.2f} seconds")
print(f"Words typed:{words}")
print(f"Typing speed:{wpm:.2f} WPM")
if typed_text==sentence:
    print("Accuracy: 100%")
else:
    print("Accuracy: Your typed sentence does not match exactly.")