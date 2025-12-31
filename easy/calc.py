
# Get user inputs
operator = input("Choose an operator (+, -, /, //, *, **, %): ") # Ask user for operation
firstNumber = input("Enter the first number: ") # Ask user for number
secondNumber = input("Enter the second number: ") # Ask user for number

# Addition function
def add(num1, num2):
    return num1 + num2 # Returns the sum of both numbers

# Subtract function
def sub(num1, num2):
    return num1 - num2 # Returns the difference of both numbers

# Divide function
def div(num1, num2):
    return num1 / num2 # Returns the dividend of both numbers

# Integer Division
# This is the same as division except it rounds down to the closest whole number
def intDiv(num1, num2):
    return num1 // num2 # Returns the dividend of both number as a whole number

# Multiply function
def mul(num1, num2):
    return num1 * num2 # Returns the product of both numbers

# Exponent function
def expo(num1, num2):
    return num1 ** num2 # Returns the power of both numbers

# Modulus function
# Modulus is remainder division
# eg. 5 % 2 = 1 because the remainder of 5 / 2 is 1
def mod(num1, num2):
    return num1 % num2 # Returns the modulus of both numbers


'''Choose which operation to run'''

# Addition
if operator == "+":
    output = add(firstNumber, secondNumber) 
    print(output)
    # This saves the return vale into a variable then prints that returned value

# Subtraction
elif operator == "-":
    print(sub(firstNumber, secondNumber))
    # This combines the process of getting a return value and printing
    # This will run sub() then enter the return value straight into the print function
    # num1 - num2 -> return value -> print

# Division
elif operator == "/":
    print(div(firstNumber, secondNumber))

# Integer Division
elif operator == "//":
    print(intDiv(firstNumber, secondNumber))

# Multiplication
elif operator == "*":
    print(mul(firstNumber, secondNumber))

# Exponents
elif operator == "**":
    print(expo(firstNumber, secondNumber))

# Modulus
elif operator == "%":
    print(mod(firstNumber, secondNumber))