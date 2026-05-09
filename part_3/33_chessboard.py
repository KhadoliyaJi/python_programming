# Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board. See the examples below for details:

# chessboard(3)
# print()
# chessboard(6)
# Sample output
# 101
# 010
# 101

# 101010
# 010101
# 101010
# 010101
# 101010
# 010101

## Solution:

def chessboard(length):
    row = length
    num = 1
    while row > 0:
        column = length
        while column > 0:
            if num == 1:
                print(1,end="")
                num = 0
            else :
                print(0,end="")
                num = 1
            column -= 1
            
        if length % 2 == 0:
            if num == 0:
                num = 1
            elif num == 1:
                num = 0
        print()
        row -= 1            

## Another approach:

## In this approach, instid of focusing on value 1 and 0, we're focusing on the position of the 
## chessboard in the form of matrix and placing 1 at even and 0 at odd index values.

# def chessboard(length):
#     row = 0

#     while row < length:
#         column = 0

#         while column < length:
#             if (row + column) % 2 == 0:
#                 print(1, end="")
#             else:
#                 print(0, end="")

#             column += 1

#         print()
#         row += 1

# Testing the function
if __name__ == "__main__":
    chessboard(4)
    # chessboard(3)
    