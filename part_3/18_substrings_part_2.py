# Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest. Have a look at the example below.

# Sample output
# Please type in a string: test
# t
# st
# est
# test

## Solution:

input_string = input("Please type in a string:")
a = -1
b = len(input_string)-1 
while b >= 0:
    print(input_string[a:])
    a -= 1
    b -= 1