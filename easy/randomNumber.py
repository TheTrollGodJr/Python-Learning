import random

# Get the lowest number then cast it to an integer value
# Use this website to learn about casting variables
# https://www.w3schools.com/python/python_casting.asp
lowerNumber = input("Enter the minimum number: ") # Get user input
lowerNumber = int(lowerNumber) # Convert the string value into an integer value -- also called casting

# Get the highest number then cast it to an integer
upperNumber = input("Enter the maximum number: ") # Get user input
upperNumber = int(upperNumber) # Convert the string value into an integer value -- also called casting

# Generate a random number then print it using the random module
# Use these websites to learn about the random module
# https://www.w3schools.com/python/module_random.asp
# https://www.w3schools.com/python/ref_random_randint.asp
randomNumber = random.randint(lowerNumber, upperNumber) # generate a random number
print(randomNumber) # Print the random number