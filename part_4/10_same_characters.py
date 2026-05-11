# Please write a function named same_chars, which takes one string and two integers as arguments. 
# The integers refer to indexes within the string. The function should return True if the two 
# characters at the indexes specified are the same. Otherwise, and especially if either of the 
# indexes falls outside the scope of the string, the function returns False.

# Some examples of how the function is used:

# # same characters m and m
# print(same_chars("programmer", 6, 7)) # True

# # different characters p and r
# print(same_chars("programmer", 0, 4)) # False

# # the second index is not within the string
# print(same_chars("programmer", 0, 12)) # False

## Solution:

def same_chars(string, num1, num2):
    if num2 >= len(string) or num1 >= len(string) or string[num1] != string[num2]:
        return False
    if string[num1] == string[num2]:
        return True
    
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("hello", 2, 3))
    print(same_chars("hello", 2, 2))
    print(same_chars("coder", 1, 7))