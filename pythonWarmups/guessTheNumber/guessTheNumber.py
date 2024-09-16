import random

class guessTheNumber:
    numGuesses = 3
    print("Choose a number")
    a = int(input())
    print("Choose a larger number")
    b = int(input())
    x = random.randint(a,b)
    print("I'm thinking of a number between " + str(a) + " and " + str(b) + ". Guess a number. You have " + str(numGuesses) + " guesses.")
    while (numGuesses > 0):
        guess = int(input())
        if(guess == x):
            print("Correct. You Win!")
        elif (numGuesses >1 ):
            if (x < guess):
                numGuesses -= 1
                print("Incorrect, the number is smaller. You have " + str(numGuesses) + " left. Try again.")
            else:
                numGuesses -= 1
                print("Incorrect, the number is larger. You have " + str(numGuesses) + " left. Try again.")
        else:
            numGuesses -= 1
            print("You lose. The correct number was " + str(x) + ".")