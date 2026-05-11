# Please write a function named triangle, which draws a triangle of hashes, and takes one 
# argument. The triangle should be as tall and as wide as the value of the argument.

# The function should call the function line from the exercise above for the actual printing out. 
# Copy your solution to that exercise above the code for this exercise. Please don't change 
# anything in the line function.

# Some examples:

# triangle(6)
# print()
# triangle(3)
# Sample output
# #
# ##
# ###
# ####
# #####
# ######

# #
# ##
# ###

## Solution:

def line(multiplier, string):
    if string == "":
        print("*"*multiplier)
    else :
        print(string[0]*multiplier)


def triangle(size):
    row = 1
    while row <= size:
        line(row, "#")
        row += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
    print()
    triangle(4)
