import random

target = random.randint(1, 500)

while True:
    userChoice = input("Guess the target or Quit(Q) : ")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Your number was small. Take a bigger guess...")
    else:
        print("Your number was big. Take a smaller guess...")

print("-----GAME OVER-----")

# Guess the number game


'''
 let's break down the provided code step-by-step:

Importing the Random Module:
import random
This imports the random module, which allows the program to generate random numbers.

Generating a Target Number:
target = random.randint(1, 500)
This line generates a random integer between 1 and 500 (inclusive) and assigns it to the variable target. 
This will be the number the user has to guess.

Starting an Infinite Loop:
while True:
This initiates an infinite loop that will keep running until it is explicitly broken.

Prompting the User for Input:
userChoice = input("Guess the target or Quit(Q) : ")
This line prompts the user to input a guess or quit the game by entering "Q". The input is stored in the variable userChoice.

Checking for Quit Condition:
if(userChoice == "Q"):
    break
If the user enters "Q", the loop breaks, and the game ends.

Converting User Input to Integer:
userChoice = int(userChoice)
This line converts the user's input from a string to an integer. 
If the user enters something that cannot be converted to an integer (like "abc"), this will raise a ValueError. 
In a production code, it would be better to handle such exceptions.

Checking User's Guess:
if(userChoice == target):
    print("Success : Correct Guess!!")
    break
elif(userChoice < target):
    print("Your number was small. Take a bigger guess...")
else:
    print("Your number was big. Take a smaller guess...")
This block of code checks if the user's guess is correct, too low, or too high:
If the guess is correct, it prints a success message and breaks the loop, ending the game.
If the guess is too low, it prints a message indicating the guess was too small and suggests guessing a bigger number.
If the guess is too high, it prints a message indicating the guess was too big and suggests guessing a smaller number.

Printing the Game Over Message:
print("-----GAME OVER-----")
After the loop ends (either because the user guessed correctly or chose to quit), 
this line prints "-----GAME OVER-----" to indicate the end of the game.
'''