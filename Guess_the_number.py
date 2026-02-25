#I tried to do it myself.
'''
import random
num = random.randint(1,11)
print('I am thinking of a number between 1 and 10.')
guess = ''
while guess != num:
    guess = input('Enter your guess number:-')
    if int(guess) > int(num):
        print('You guess is greater than what i am thinking. Try Again!')
    elif int(guess) < int(num):
        print('Your guess is less than what i am thinking. Try Again!')
    else:
        print(f'you are right, I was thinking of {guess}')
'''
#Here is the book's version
import random
secret_number = random.randint(1,21)
print("I am thinking of a number between 1 and 20.")
for guess_taken in range(1,7):
    print("Take Guess!")
    guess = int(input(">"))
    if guess < secret_number:
        print("Your guess is less than the Right Answer. Try Again!")
    elif guess > secret_number:
        print("Your guess is greater than the correct amnswer. Try Again!")
    else:
        break #This condition is the correct guess!
if guess == secret_number:
    print('Good job! You got  it in '+str(secret_number)+ ' guesses!')
else:
    print('Nope. The number was '+ str(secret_number))
