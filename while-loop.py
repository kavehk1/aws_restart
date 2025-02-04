print("Welcome to guess a Number!")
print("The rules are simple. I will think of a number, and you will ty and guess it.")

import random
number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input ("Guess a number between 1 and 10:")
    if int(guess) == number:
        print("You Guess {}, is correct, You win".format(guess))
        isGuessRight = True
    else:
        print("You Guessed {}, Sorry, that isn't it. try again.".format(guess))
        