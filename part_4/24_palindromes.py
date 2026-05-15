# Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. Palindromes are words which are spelled exactly the same backwards and forwards.

# Please also write a main program which asks the user to type in words until they type in a palindrome:

# Sample output
# Please type in a palindrome: python
# that wasn't a palindrome
# Please type in a palindrome: java
# that wasn't a palindrome
# Please type in a palindrome: oddoreven
# that wasn't a palindrome
# Please type in a palindrome: neveroddoreven
# neveroddoreven is a palindrome!

## Solution:

def palindromes(string):
    result = ''
    new_string = ''
    
    for i in range(len(string) - 1, -1, -1):
        new_string += string[i]
    
    # if new_string == string:
    #     result = True
    # else:
    #     result = False
    # return result
    return new_string == string     # Here the condition itself gives a boolean value i.e. True or False
 

while True:
    input_string = input("Please type in a palindrome: ")
    if palindromes(input_string):
        print(input_string, "is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

     
     

