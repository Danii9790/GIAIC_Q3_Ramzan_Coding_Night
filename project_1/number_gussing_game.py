# import random
# print("Welcome to Number Gussing Game \n you got 5 attempt to guess the Correct Number.")
# number_to_guess=random.randrange(50,100)
# chance=5
# guess_counter=0
# while guess_counter<chance:
#     guess_counter+=1
#     my_guess=int(input("Enter your guess : "))

#     if my_guess == number_to_guess:
#         print(f"the number is {number_to_guess} and you find a right {guess_counter} attempt.")
#         break
#     elif guess_counter >=chance and my_guess!= number_to_guess:
#         print(f"Oops sorry!!! the number is  {number_to_guess} better luck next time. ")
#     elif my_guess < number_to_guess:
#         print(f"You guess very low,try again")
#     elif my_guess > number_to_guess:
#         print("you guess very high,try again.")

import random

print("Welcome to Number Guessing Game \n you have 5 attempt to guess the correct number.")
number_to_guess=random.randint(1,50)
counter=0
chance=5

while counter < chance :
    counter +=1
    try:  # try and except is used because erorr or program chrashad handling if a user enter a alphebetic characters the program show a invalid message:
        my_guess=int(input(f"Attempt {counter}/{chance} - Enter your Guess : "))
    except ValueError:
        print("Invalid input ! please enter a valid number")
        counter -=1  #don't count invalid attempt
        continue
    if my_guess == number_to_guess:
        print(f"Congratulations! the number was {number_to_guess}.you guess it in {counter} attempt.")
    elif my_guess < number_to_guess:
        print("You are guess too low number")
    else:
        print("You guess is too high")
if my_guess !=number_to_guess:
    print(f"Oops you've  used all {chance} attempt. the correct number was {number_to_guess}.Better Luck next time ")