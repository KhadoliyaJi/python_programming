# This is the very last sudoku task. This time we will create a slightly different version of the 
# function for adding new numbers to the grid.

# The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a 
# two-dimensional array representing a sudoku grid, two integers referring to the row and column 
# indexes of a single square, and a single digit between 1 and 9, as its arguments. The function 
# should return a copy of the original grid with the new digit added in the correct location. 
# The function should not change the original grid received as a parameter.

# The print_sudoku function from the previous exercise could be useful for testing, and it is used 
# in the example below:

# sudoku  = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# grid_copy = copy_and_add(sudoku, 0, 0, 2)
# print("Original:")
# print_sudoku(sudoku)
# print()
# print("Copy:")
# print_sudoku(grid_copy)
# Sample output
# Original:
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# Copy:
# 2 _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _

# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _
# _ _ _  _ _ _  _ _ _


## Solution:

def print_sudoku(sudoku: list):
    new_matrix = sudoku

    for row in range(0, 9, 3):
        # for col in range(0, 9, 3):
        for i in range(row, row + 3):

            for col in range(0, 9, 3):
            # for i in range(row, row + 3):
                for j in range(col, col + 3):
                    value = new_matrix[i][j]

                    if value == 0:
                        print("_ ", end = "")
                    else:
                        print(f"{value} ", end = "") 
                print(" ", end="")
            print("\n", end = "")
        print() 

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
## Note: we can't use [:] copying method in 2D array as [:] only copies the outer layer where as the inner
## refferces are still of the original one
    # sudoku = sudoku[:]
    
    ## method_1: (advanced) list comprehension with slicing
    # copied = [row[:] for row in sudoku]
    # copied[row_no][column_no] = number
    # return copied

    ## method_2: (simple) for loop iteration to create an accurate copy 
    copied = []
    for row in sudoku:
        new_row = []
        for col in row:
            new_row.append(col)
        copied.append(new_row)

    copied[row_no][column_no] = number
    return copied

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)