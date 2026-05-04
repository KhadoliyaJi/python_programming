# Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

# An example of expected behaviour:

# Sample output
# Please type in a string: hiya
# a
# y
# i
# h

## Solution:

given_string = input("Please type in a string: ")
index = 0
reverse = -1

while index < len(given_string):
    print(given_string[reverse])
    index += 1
    reverse -= 1