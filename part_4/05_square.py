# Please write a function named square, which prints out a square of characters, and takes two 
# arguments. The first parameter specifies the length of the side of the square. The second 
# parameter specifies the character used to draw the square.

# The function should call the function line from the exercise above for the actual printing out.
# Copy your solution to that exercise above the code for this exercise. Please don't change 
# anything in the line function.

# Some examples:

# square(5, "*")
# print()
# square(3, "o")
# Sample output
# *****
# *****
# *****
# *****
# *****

# ooo
# ooo
# ooo

## Solution:

def line(multiplier, string):
    if string == "":
        print("*"*multiplier)
    else :
        print(string[0]*multiplier)


def square(size, character):
    row = size
    while row > 0:
        line(size, character)
        row -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
    print()
    square(3, "o")