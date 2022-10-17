#Number Guessing Game 
from random import randint
from art import logo

LEVEL_HARD = 5
LEVEL_EASY = 10

def check_answer(x, guess, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > x:
        print("Too high.")
        return turns -1
    elif guess < x:
        print("Too low.")
        return turns -1
    elif guess == x:
        print (f"You got it! The answer was {x}")

def set_diffuculty():
    level = input ("Choose a difficulty. Type 'easy' or 'hard':")
    
    if level == "easy":
        return LEVEL_EASY
    elif level == "hard":
        return LEVEL_HARD
    else:
        print("Please type 'easy' or 'hard'")
        return level

def game():
    print (logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")


    x = randint(1, 100) # Pick a random number between 1 and 100.
    #print("You have 5 attempts ramaining to guess the number.")
    #print (x)
    turns = set_diffuculty()

    guess = 0
    while guess != x:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(x, guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != x:
            print("Guess again.")

game()