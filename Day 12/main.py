import random as rand
def game(xyz):
    guessed=False
    while xyz>0 and not guessed:
        print(f"you have {xyz} attempts remaining to guess.")
        guessed_number=int(input("Make a guess: "))
        if guessed_number>actual_number:
            print("Too high!")
            print("Guess Again.")
            xyz-=1
        elif guessed_number<actual_number:
            print("Too Low!")
            print("Guess Again.")
            xyz-=1
        elif guessed_number==actual_number:
            print("You won. You guessed it right!!")
            guessed=True
            break
    if not guessed:
        print(f"You loose!! The correct number is {actual_number} ")
    else :
        print("Game Over!")        

# driver code
print("Welcome to Number Guessing Game!")
actual_number=rand.randint(1,100)
print("I am thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty=="easy":
    game(10)
elif difficulty=="hard":
    game(5)

