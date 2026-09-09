import random
number=random.randint(1,100)
attempts=0
print("🎯 Number Guessing Game")
print("I have selected a number between 1 and 100.")
while True:
    try:
        guess=int(input("Enter your guess:"))
        attempts+=1
        if guess<number:
            print("Two low! Try again.")
        elif guess>number:
            print("Too High! Try again.")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a Valid number.")