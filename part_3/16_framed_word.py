# Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

# If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

# Sample output
# Word: testing

# ******************************
# *          testing           *
# ******************************
# Sample output
# Word: python

# ******************************
# *           python           *
# ******************************

## Solution:

# input_string = input("Word:")
# # input_string = 'This is a longer sentence.'
# frame = 30
# position = int((28 - len(input_string))//2)
# print("*"*frame)
# if len(input_string) % 2 == 0:  # Unnecessary even odd computation 
#     print(f"*" + " "*position + input_string + " "*position + "*")
# else :
#     print(f"*" + " "*(position+1) + input_string + " "*position + "*")
# print("*"*frame)

### This logic gives correct output but the way to solution is not optimized.
### We don't need odd even calculasion here, just have to find left and right spaces

input_string = input("Word:")
frame = 30
left_space = (28 - len(input_string))//2
right_space = 28 - len(input_string) - left_space

print("*"*frame)
print("*" + " "*left_space + input_string + " "*right_space + "*")
print("*"*frame)

## Optimized solution