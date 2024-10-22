import tkinter as tk
import random

user_score = 0
computer_score = 0

def determine_winner(user_choice):
    global user_score, computer_score
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    
    label_user_choice.config(text=f"Your choice: {user_choice}")
    label_computer_choice.config(text=f"Computer's choice: {computer_choice}")
    label_result.config(text=result)
    label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    label_user_choice.config(text="Your choice: ")
    label_computer_choice.config(text="Computer's choice: ")
    label_result.config(text="")
    label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

label_instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
label_instructions.pack()

button_rock = tk.Button(root, text="Rock", command=lambda: determine_winner("Rock"))
button_rock.pack()

button_paper = tk.Button(root, text="Paper", command=lambda: determine_winner("Paper"))
button_paper.pack()

button_scissors = tk.Button(root, text="Scissors", command=lambda: determine_winner("Scissors"))
button_scissors.pack()

label_user_choice = tk.Label(root, text="Your choice: ")
label_user_choice.pack()

label_computer_choice = tk.Label(root, text="Computer's choice: ")
label_computer_choice.pack()

label_result = tk.Label(root, text="")
label_result.pack()

label_score = tk.Label(root, text=f"Score - You: {user_score} | Computer: {computer_score}")
label_score.pack()

button_reset = tk.Button(root, text="Reset Game", command=reset_game)
button_reset.pack()

root.mainloop()

'''
Here's a line-by-line breakdown of the code:

import tkinter as tk: This imports the tkinter library, which is used to create graphical user interfaces (GUIs) in Python. 
The alias tk allows you to reference it easily.

import random: This imports the random module, which provides functions to generate random numbers and select random items from a list, 
used here for the computer's choice in the game.

user_score = 0: This initializes the score for the user to 0.

computer_score = 0: This initializes the score for the computer to 0.

def determine_winner(user_choice):: This defines a function named determine_winner that will 
determine who wins the game based on the user's choice.

global user_score, computer_score: The global keyword allows the function to modify the user_score and computer_score variables, 
which are defined outside the function.

options = ["Rock", "Paper", "Scissors"]: This creates a list of possible choices for the game: "Rock," "Paper," and "Scissors."

computer_choice = random.choice(options): This uses the random.choice() function to randomly select one of the options for the computer.

result = "": This initializes an empty string result, which will later store the outcome of the game.

if user_choice == computer_choice:: This checks if the user's choice is the same as the computer's choice. If they are the same, it's a tie.

result = "It's a tie!": If the choices are the same, the result is set to "It's a tie!"

elif (user_choice == "Rock" and computer_choice == "Scissors") or ...: 
    This checks various conditions where the user would win based on the rules of Rock, Paper, Scissors.

result = "You win!": If the user wins, this sets the result to "You win!"

user_score += 1: This increases the user's score by 1 if the user wins.

else:: If the user doesn't win or tie, the computer wins.

result = "You lose!": If the computer wins, the result is set to "You lose!"

computer_score += 1: This increases the computer's score by 1 if the computer wins.

label_user_choice.config(text=f"Your choice: {user_choice}"): This updates the label to show the user's choice.

label_computer_choice.config(text=f"Computer's choice: {computer_choice}"): This updates the label to show the computer's choice.

label_result.config(text=result): This updates the label to show whether the user won, lost, or tied.

label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}"): 
This updates the label to show the current score of the user and the computer.

def reset_game():: This defines a function named reset_game that will reset the game to its initial state.

global user_score, computer_score: Again, global is used to modify the global user_score and computer_score variables.

user_score = 0: This resets the user's score to 0.

computer_score = 0: This resets the computer's score to 0.

label_user_choice.config(text="Your choice: "): This resets the label showing the user's choice.

label_computer_choice.config(text="Computer's choice: "): This resets the label showing the computer's choice.

label_result.config(text=""): This clears the result label.

label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}"): This resets the score display.

root = tk.Tk(): This creates the main application window (root window).

root.title("Rock, Paper, Scissors Game"): This sets the title of the window.

label_instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:"): 
This creates a label widget with instructions for the user to choose Rock, Paper, or Scissors.

label_instructions.pack(): This adds the instructions label to the window.

button_rock = tk.Button(root, text="Rock", command=lambda: determine_winner("Rock")): 
This creates a button labeled "Rock" that, when clicked, calls the determine_winner function with "Rock" as the user's choice.

button_rock.pack(): This adds the "Rock" button to the window.

button_paper = tk.Button(root, text="Paper", command=lambda: determine_winner("Paper")): 
This creates a button labeled "Paper" that calls the determine_winner function with "Paper."

button_paper.pack(): This adds the "Paper" button to the window.

button_scissors = tk.Button(root, text="Scissors", command=lambda: determine_winner("Scissors")): 
This creates a button labeled "Scissors" that calls the determine_winner function with "Scissors."

button_scissors.pack(): This adds the "Scissors" button to the window.

label_user_choice = tk.Label(root, text="Your choice: "): This creates a label to display the user's choice.

label_user_choice.pack(): This adds the user's choice label to the window.

label_computer_choice = tk.Label(root, text="Computer's choice: "): This creates a label to display the computer's choice.

label_computer_choice.pack(): This adds the computer's choice label to the window.

label_result = tk.Label(root, text=""): This creates a label to display the result (win/lose/tie) but leaves it blank initially.

label_result.pack(): This adds the result label to the window.

label_score = tk.Label(root, text=f"Score - You: {user_score} | Computer: {computer_score}"): 
This creates a label to display the score, which initially shows 0-0.

label_score.pack(): This adds the score label to the window.

button_reset = tk.Button(root, text="Reset Game", command=reset_game): 
This creates a button labeled "Reset Game" that, when clicked, resets the game using the reset_game function.

button_reset.pack(): This adds the "Reset Game" button to the window.

root.mainloop(): This starts the Tkinter event loop, which waits for user interaction with the window.
'''