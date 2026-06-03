# Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional 
# array representing a sudoku grid as its argument. The function should use the functions from the 
# three previous exercises to determine whether the complete sudoku grid is filled in correctly. 
# Copy the functions from the exercises above into your Python code file for this exercise.

# The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. If all 
# contain each of the numbers 1 to 9 at most once, the function returns True. If a single one is 
# filled in incorrectly, the function returns False.

# The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with 
# thicker borders. These are the blocks the function should check, and they begin at the indexes 
# (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).

# sudoku1 = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [2, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [2, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]

# print(sudoku_grid_correct(sudoku1))

# sudoku2 = [
#   [2, 6, 7, 8, 3, 9, 5, 0, 4],
#   [9, 0, 3, 5, 1, 0, 6, 0, 0],
#   [0, 5, 1, 6, 0, 0, 8, 3, 9],
#   [5, 1, 9, 0, 4, 6, 3, 2, 8],
#   [8, 0, 2, 1, 0, 5, 7, 0, 6],
#   [6, 7, 4, 3, 2, 0, 0, 0, 5],
#   [0, 0, 0, 4, 5, 7, 2, 6, 3],
#   [3, 2, 0, 0, 8, 0, 0, 5, 7],
#   [7, 4, 5, 0, 0, 3, 9, 0, 1]
# ]

# print(sudoku_grid_correct(sudoku2))
# Sample output
# False
# True

## Solution:

def row_correct(sudoku_list : list):
    empty_list = []
    
    for row_no in range(0, 9):
        for j in sudoku_list[row_no]:
            if j == 0:
                continue
            elif j in empty_list:
                return False
            else:
                empty_list.append(j)
        empty_list.clear()
    return True

def column_correct(sudoku : list):
    empty_list = []

    for col_no in range(0, 9):
        for i in sudoku:
            if i[col_no] == 0:
                continue
            elif i[col_no] in empty_list:
                return False
            else:
                empty_list.append(i[col_no])
        empty_list.clear()
    return True

# def block_correct(sudoku : list):
#     # [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]] 
#     block = [0, 3, 6]
#     empty_list = []
#     count = 0
#     # row_no = 
#     # col_no = 
#     # for i in range(row_no, row_no + 3):
#     # for i in range(0, 9, 3):
#     for block in block:
#         # for i in range(block, block + 3):
#         for i in range(0, 9):
#             for j in range(block, block + 3):
#                 value = sudoku[i][j]
#                 # print(value, end="")
#                 count += 1
#                 if count <= 9:
#                     if value == 0:
#                         continue
#                     elif value in empty_list:
#                         return False
#                     else: 
#                         empty_list.append(value)
#                 if count == 9:
#                     empty_list.clear()
#                     count = 0
#     return True


def block_correct(sudoku : list):
    
    for row_no in range(0, 9, 3):
        for col_no in range(0, 9, 3):

            empty_list = []

            for i in range(row_no, row_no + 3):
                for j in range(col_no, col_no + 3):
                    value = sudoku[i][j]
                    # print(value,end="")
                    if value == 0:
                        continue
                    elif value in empty_list:
                        return False
                    else: 
                        empty_list.append(value)
                # print()
    return True

def sudoku_grid_correct(sudoku : list):
    ## un-necessary conditional statement 
    # result = row_correct(sudoku)
    # if result == False:
    #     return False
    # result = column_correct(sudoku)
    # if result == False:
    #     return False
    # result = block_correct(sudoku)
    # return  result

    return (row_correct(sudoku) and column_correct(sudoku) and block_correct(sudoku))


if __name__ == "__main__":

    sudoku = [
        [ 2, 9, 5, 0, 8, 4, 7, 1, 3 ],
        [ 6, 4, 8, 1, 3, 7, 9, 2, 5 ],
        [ 1, 7, 3, 2, 0, 9, 4, 6, 8 ],
        [ 8, 6, 0, 3, 4, 1, 2, 5, 7 ],
        [ 5, 2, 7, 8, 9, 6, 0, 3, 4 ],
        [ 3, 1, 4, 0, 7, 2, 6, 8, 9 ],
        [ 7, 5, 0, 9, 2, 8, 1, 4, 0 ],
        [ 4, 3, 6, 7, 1, 5, 8, 0, 2 ],
        [ 0, 8, 0, 4, 6, 3, 5, 7, 1 ],
    ]

    print(sudoku_grid_correct(sudoku))

    sudoku2 = [
      [2, 6, 7, 8, 3, 9, 5, 0, 4],
      [9, 0, 3, 5, 1, 0, 6, 0, 0],
      [0, 5, 1, 6, 0, 0, 8, 3, 9],
      [5, 1, 9, 0, 4, 6, 3, 2, 8],
      [8, 0, 2, 1, 0, 5, 7, 0, 6],
      [6, 7, 4, 3, 2, 0, 0, 0, 5],
      [0, 0, 0, 4, 5, 7, 2, 6, 3],
      [3, 2, 0, 0, 8, 0, 0, 5, 7],
      [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))