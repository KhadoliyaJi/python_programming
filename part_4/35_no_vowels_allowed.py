# Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be the same as the original but with all vowels removed.

# You can assume the string will contain only characters from the lowercase English alphabet a...z.

# An example of expected behaviour:

# my_string = "this is an example"
# print(no_vowels(my_string))
# Sample output
# ths s n xmpl

## Solution:

## Problem solved as un-necessarily need nested loops and multiple assignment of True and False
# def no_vowels(string):
#     new_string = ''
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for char in string:
#         match = False
#         for vowel in vowels:
#             if char == vowel :
#                 match = False
#                 break 
#             else :
#                 match = True
#         if match == True:
#             new_string += char
#     return new_string


# Better version 
## Use of "not in" to check presence of vowels
def no_vowels(string):
    new_string = ''
    vowels = "aeiou"

    for char in string:
        if char not in vowels :
            new_string += char
    return new_string



if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))



