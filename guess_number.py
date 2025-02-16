import random
import art

no_of_attempts_hard= 5
no_of_attempts_easy= 10

def think_no():
  num_chosen = random.randint(1, 100)
  return num_chosen

def check_answer(turn, num, answer):
    if turn == 0 and num != answer:
        print(f"You've run out of guesses. Refresh the page to run again.")
    elif num > answer:
        print(f"too high.")
        print(f"guess again")
    elif num < answer:
        print(f"too low.")
        print(f"guess again")
    elif num == answer:
        print(f"You got it right! The number was {answer}.")
        turn = 0
    return turn


def game(op, answer):
   global no_of_attempts
   if op == 'easy':
     no_of_attempts = no_of_attempts_easy
   elif op == 'hard':
     no_of_attempts = no_of_attempts_hard
   else:
       print("Invalid option")
   while not no_of_attempts == 0:
       print(f"You have {no_of_attempts} attempts remaining to guess the number.")
       no_of_attempts -= 1
       num = int(input("Make a guess:"))
       no_of_attempts = check_answer(no_of_attempts, num, answer)


print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
no_chosen = think_no()
option = input("Choose a difficulty. Type 'easy' or 'hard':")
game(option,no_chosen)