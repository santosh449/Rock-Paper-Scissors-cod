import random   # Random Package from the library

# Combinations of Inputs
user_input = input("Enter either 'Rock', 'Paper', 'Scissor', 'Lizard', or 'Spock': ")
print("You entered : ", user_input)

possible_options = ['Rock', 'Paper', 'scissor', 'Lizard', 'Spock']
# Enter the code for Computer Input
computer_input = random.choice(possible_options)
print("System entered :", computer_input)

# Try all the possible combinations between user & computer
if (user_input == computer_input):
    print("This Match is a Tye")
elif user_input == 'Rock':
    if computer_input == 'Scissor':
        print("You are the Winner!")
    else:
        print("Computer is the Winner!")


elif user_input == 'Paper':
    if computer_input == 'Scissor':
        print("Computer is the Winner!")
    else:
        print("You are the Winner!")

elif user_input == 'Scissor':
    if computer_input == 'Rock':
        print("Computer is the Winner!")
    else:
        print("You are the Winner!")

elif user_input == 'Scissor':
    if computer_input == 'Paper':
        print("You are the Winner!")
    else:
        print("Computer is the Winner!")

elif user_input == 'Rock':
    if computer_input == 'Paper':
        print("Computer is the Winner!")
    else:
        print("You are the Winner!")

elif user_input == 'Paper':
    if computer_input == 'Rock':
        print("You are the Winner!")
    else:
        print("Computer is the Winner!")

elif user_input == 'Lizard':
    if computer_input == 'Rock':
        print("Computer is the Winner!")
    else:
        print("You are the Winner!")

elif user_input == 'Spock':
    if computer_input == 'Rock':
        print("You are the Winner!")
    else:
        print("Computer is the Winner!")

elif user_input == 'Lizard':
    if computer_input == 'Spock':
        print("You are the Winner!")
    else:
        print("Computer is the Winner!")

elif user_input == 'Spock':
    if computer_input == 'Lizard':
        print("Computer is the Winner!")
    else:
        print("You are the Winner!")

elif user_input == 'Spock':
    if computer_input == 'Paper':
        print("Computer is the Winner!")
    else:
        print("You are the Winner!")

elif user_input == 'Spock':
    if computer_input == 'Scissors':
        print("You are the Winner!")
    else:
        print("Computer is the Winner!")

elif user_input == 'Scissors':
    if computer_input == 'Spock':
        print("Computer is the Winner!")
    else:
        print("You are the Winner!")

elif user_input == 'Lizard':
    if computer_input == 'Scissors':
        print("Computer is the Winner!")
    else:
        print("You are the Winner!")

elif user_input == 'Scissors':
    if computer_input == 'Lizard':
        print("You are the Winner!")
    else:
        print("Computer is the Winner!")
