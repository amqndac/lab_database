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

riddles = get_random_riddles(5)

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




