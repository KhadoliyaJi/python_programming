# Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

# In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

# Some examples of expected behaviour:

# Sample output
# Please type in a string: abcabc
# Please type in a substring: ab
# The second occurrence of the substring is at index 3.

# Sample output
# Please type in a string: methodology
# Please type in a substring: o
# The second occurrence of the substring is at index 6.

# Sample output
# Please type in a string: aybabtu
# Please type in a substring: ba
# The substring does not occur twice in the string.

## Solution:

# First approach, very complicated
input_string = input("Please type in a string:")
substring = input("Please type in a substring:")
substring_length = len(substring)
index = input_string.find(substring)
skip = substring_length
while index != -1:

    if index + skip + substring_length > len(input_string):
        print("The substring does not occur twice in the string.")
        break 

    if input_string[index + skip : index + skip + substring_length] == substring :
        print(f"The second occurrence of the substring is at index {index + skip}.")
        break 
    skip += 1 
if index == -1:
    print("The substring does not occur twice in the string.")


## Easier version:


# string = input("Please type in a string: ")
# substring = input("Please type in a substring: ")

# first = string.find(substring)

# if first == -1:
#     print("The substring does not occur twice in the string.")
# else:
#     second = string.find(substring, first + len(substring))

#     if second == -1:
#         print("The substring does not occur twice in the string.")
#     else:
#         print(f"The second occurrence of the substring is at index {second}.")
