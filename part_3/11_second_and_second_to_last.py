# Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.

# Sample output
# Please type in a string: python
# The second and the second to last characters are different

# Sample output
# Please type in a string: pascal
# The second and the second to last characters are a

## Solution:

input_string = input("Please type in a string: ")

if input_string[1] == input_string[-2]:
    print("The second and the second to last characters are",input_string[1])
elif input_string[1] != input_string[-2]:
    print("The second and the second to last characters are different")
 