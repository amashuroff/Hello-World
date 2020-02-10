print('Please think of a number between 0 and 100')
high = 100
low = 0

guessed = False


while not guessed:

    guess = (high+low)//2
    print('Is your secret number is ' + str(guess) + '?')
    user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")


    if user_inp=='c':
        print('I guessed the number!')
        guessed = True
    elif user_inp == 'l':
        low = guess
    elif user_inp == 'h':
        high = guess
    else:
        print("Sorry, i don't understand your input...")


print("Your secret number was " + str(guess) + '!')