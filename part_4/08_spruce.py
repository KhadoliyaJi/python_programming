# Please write a function named spruce, which takes one argument. The function prints out the 
# text a spruce!, and the a spruce tree, the size of which is specified by the argument.

# Calling spruce(3) should print out

# Sample output
# a spruce!
#   *
#  ***
# *****
#   *
# Calling spruce(5) should print out

# Sample output
# a spruce!
#     *
#    ***
#   *****
#  *******
# *********
#     *

## Solution:

def spruce(size):
    print("a spruce!")
    space = size 
    num = 0

    while space > 0:
        space -= 1
        print(" " * space + "*" + "**" * num)
        num += 1
    print(" " * (size - 1) + "*")


# if __name__ == "__main__":
#     spruce(5)
#     print()
#     spruce(8)
