#This is guess the number game
import random
print('Hello, What is your name.')
name= input()
secretNumber = random.randint(1, 20)
print('Well, '+name +', I am thinking of a number in between 1 to 20')

#Ask the user to guess 6 times
for guessTaken in range(6):
    print('Take a guess')
    guess = int(input())
    if guess>secretNumber:
        print('Your guess is too high')
    elif guess<secretNumber:
        print('Your guess is too low')
    else:
        break

if guess == secretNumber:
    print('Good job '+ name+'! you guessed my number in '+ str(guessTaken + 1) +' guesses.')
else:
    print('Nope the number i was thinking of was '+ str(secretNumber))
