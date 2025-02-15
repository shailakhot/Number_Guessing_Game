import random

import art

def think_no():
  num_chosen = random.randint(1, 100)
  return num_chosen

def guess_no(option,no_chosen):
   if option == 'easy':
     no_of_attempts = 10
   elif option == 'hard':
     no_of_attempts = 5
   else:
       print("Invalid option")

   while not no_of_attempts == 0:
       print(f"You have {no_of_attempts} attempts remaining to guess the number.")
       no_of_attempts -= 1
       num= int(input("Make a guess:"))
       if no_of_attempts == 0 and num != no_chosen:
           print("You've run out of guesses. Refresh the page to run again.")
       elif num > no_chosen:
           print(f"too high.")
           print("guess again")
       elif num < no_chosen:
           print(f"too low.")
           print("guess again")
       elif num == no_chosen:
         print(f"You got it right! The number was {no_chosen}.")
         no_of_attempts = 0


print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
no_chosen = think_no()
option = input("Choose a difficulty. Type 'easy' or 'hard':")
guess_no(option,no_chosen)