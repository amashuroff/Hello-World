import random

strt = input("""
Welcome to the guessing game!
To begin, type start: """)
print("""

I am thinking of some number between 1 and 100
Try to guess it!
Don't worry, i'll help you with that!
Within 10 of the number, i'll tell you that you are VERY WARM!
Let's go!""")


num = random.randint(1,101)
guesses = [0]

while True:
    guess = int(input("""
I am thinking of a number between 0 and 100...
What is your guess?  """))
    if guess < 1 or guess > 100:
        print("""
        Are you a hard one?
        Try again... """)
        continue
    if guess == num:
        print(f"Congratulations! You guessed it in only {len(guesses)} guesses!!!")
        break
    guesses.append(guess)
    if guesses[-2]:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
    else:
        if abs(num - guess) <= 10:
            print('WARM! YOU ARE LESS THEN 10 NUMBERS AWAY FROM THE RIGHT GUESS!!!')
        else:
            print('YOU ARE MORE THEN 10 NUMBERS AWAY FROM THE RIGHT GUESS...COLD!')
