# Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.

# Some examples of expected behaviour:

# Sample output
# Number 1: 10
# Number 2: 17
# Operation: add

# 10 + 17 = 27

# Sample output
# Number 1: 4
# Number 2: 6
# Operation: multiply

# 4 * 6 = 24

# Sample output
# Number 1: 4
# Number 2: 6
# Operation: subtract

# 4 - 6 = -2


# Solution:
num1 = int(input("Number1:"))
num2 = int(input("Number2:"))
operation = input("Operation:")
print("")

if(operation=='add'):
    print(f"{num1} + {num2} = {num1+num2}")
if(operation=='multiply'):
    print(f"{num1} * {num2} = {num1*num2}")
if(operation=='subtract'):
    print(f"{num1} - {num2} = {num1-num2}")