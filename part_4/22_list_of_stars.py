# Please write a function named list_of_stars, which takes a list of integers as its argument. The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.

# For example, with the function call list_of_stars([3, 7, 1, 1, 2]) the following should be printed out:

# Sample output
# ***
# *******
# *
# *
# **

## Solution:

def list_of_stars(list_value : list):
    for i in list_value:
        print("*" * i)

if __name__ == "__main__" :
    list_of_stars([2,3,4,5])

