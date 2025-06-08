# this file should run a riddle guessing game

from helpers import *
import colorama
from colorama import Fore, Back, Style 
from colorama import init 
init(autoreset=True)

all_trivias = get_all_riddles()   

name = input("What is your name? \n")
score = 0

print("--------------------------------------------------\n" +
f"Hello {name}, welcome to the Riddler! \n" +
 "You will be asked a series of riddles.\n" +
 "Try your best to answer correctly!\n" +
 "--------------------------------------------------\n")

level_selection = input("What level would you like to play? (Easy, Medium, Hard, Mixed Difficulty) \n")
if level_selection == "Easy" or "easy":
    riddles = get_random_riddles_easy(10)

elif level_selection == "Medium" or "medium":
    riddles = get_random_riddles_medium(10)

elif level_selection == "hard" or "Hard":
    riddles = get_random_riddles_hard(10)

elif level_selection == "Mixed Difficulty" or "mixed difficulty" or "Mixed difficulty":
    riddles = get_random_riddles(10)

for riddle in riddles: 
   print(riddle['question'])
   user_answer = input()
   if user_answer == riddle['answer']:
       print(Fore.GREEN + "Correct! ✅")
       score += 1 
   else:
       print(Fore.RED + "Sorry, that is Incorrect. 😔")

print("--------------------------------------------------\n" +
f"Good job on finishing the game, {name}! \n" +
f"Your score is: {score}/5 \n" +
f"Try your best to answer correctly!\n"
f"--------------------------------------------------\n")




