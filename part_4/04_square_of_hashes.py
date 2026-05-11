# Please write a function named square_of_hashes, which draws a square of hash characters. 
# The function takes one argument, which determines the length of the side of the square.

# The function should call the function line from the exercise above for the actual printing out. 
# Copy your solution to that exercise above the code for this exercise. Please don't change 
# anything in the line function.

# Some examples:

# square_of_hashes(5)
# print()
# square_of_hashes(3)
# Sample output
# #####
# #####
# #####
# #####
# #####

# ###
# ###
# ###

## Solution:

def line(multiplier, string):
    if string == "":
        print("*"*multiplier)
    else :
        print(string[0]*multiplier)

def square_of_hashes(size):
    count = size
    while size > 0:
        line(count, "#")
        size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)
