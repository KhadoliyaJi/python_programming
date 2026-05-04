# Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

# Some examples of expected behaviour:

# Sample output
# Please type in string 1: hey
# Please type in string 2: hiya
# hiya is longer

# Sample output
# Please type in string 1: howdy doody
# Please type in string 2: hola
# howdy doody is longer

# Sample output
# Please type in string 1: hey
# Please type in string 2: bye
# The strings are equally long

## Solution:

first_string = input("Please type in string 1: ")
second_string = input("Please type in string 2: ")

if len(first_string) > len(second_string):
    print(f"{first_string} is longer")
elif len(second_string) > len(first_string):
    print(f"{second_string} is longer")
elif len(second_string) == len(first_string):
    print("The strings are equally long")