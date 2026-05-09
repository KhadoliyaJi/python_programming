# Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below.

# squared("ab", 3)
# print()
# squared("aybabtu", 5)
# Sample output
# aba
# bab
# aba

# aybab
# tuayb
# abtua
# ybabt
# uayba


## Solution:

def squared (string, number):
    
    row = number
    index = 0

    while row > 0:
        column = number
        while column > 0:
            print(string[index], end = "")
            if index < len(string) - 1:
                index += 1
            else :
                index = 0
            column -= 1
        
        print()
        row -= 1

# if __name__ == __main__:
#     squared("ab", 3)
#     squared("aigfsdfasd", 5)

            
