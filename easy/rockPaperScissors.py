
# Get player input using the input() function
# Use this webpage for more information about input()
# https://www.w3schools.com/python/ref_func_input.asp
playerChoice = input("Pick rock, paper, or scissors: ")

# Use if statements to check the players choice
# Use these webpages for more information about if statements
# https://www.w3schools.com/python/python_conditions.asp
# https://www.w3schools.com/python/python_if_elif.asp
# https://www.w3schools.com/python/python_if_else.asp
if playerChoice == "rock": # Run this if the player entered 'rock'
    print("paper")
elif playerChoice == "paper": # Run this if the player entered 'paper'
    print("scissors")
else: # Run this if the player entered 'scissors'
    print("rock")