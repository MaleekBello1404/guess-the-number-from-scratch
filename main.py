import random
from art import logo

EASY = 10
HARD = 5

def difficulty():
    #this function returns the amount of turns the user will use
    level = input("What difficulty will you like? type 'easy' or 'hard': ")
    if level == "easy":
        return EASY
    else:
        return HARD


def calc(guess, answer, level):
    #a function that calc to see if the user guess is similar to the actual guess, it also returns a value if the user misses it.
    if guess > answer:
        print("Too High")
        return level - 1
    elif guess < answer:
        print("Too Low")
        return level -1
    else:
        print(f"you got it, the answer is {answer}")
        return
    
def game():
    print(logo)
    final_answer = random.randint(1,100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(final_answer)
    level = difficulty()

    user_guess = 0
    while user_guess != final_answer:
        #check to see if the user got the guess right, if he doesn't. this should repeat itself 
        print(f"You have {level} attempts remaining to guess the number.")
        
        user_guess = int(input("Make a guess: "))
        
        level = calc(user_guess, final_answer,level)
        #make a if statement so when the number of tries the user have goes to 0 you want the program to exist
        if level == 0:
            print("You've run out of lives, You lose")
            return 
        elif user_guess != final_answer:
            print("Guess Again")
            
           
            
game()


