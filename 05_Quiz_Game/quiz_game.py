questions={
    "what is the capital of India?": "delhi",
    "Which language is used to create web pages?": "html",
    "What is 5+5?": "10",
    "Which keyword is used to define a function in Python?":
     "def",
    "What does Cpu stand for?": "central processing unit"

}
score=0
print("🧠 Python Quiz Game")
print()
for question, answer in questions.items():
    user_answer=input(question+"").lower().strip()
    if user_answer==answer:
        print("Correct! ✅")
        score+=1
    else:
        print("Wrong! ❌")
        print("Correct answer:",answer)
        print()
print("Quiz completed!")
print(f"Your score: {score}/{len(questions)}")