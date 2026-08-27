# The file matrix.txt contains a matrix in the format specified in the example below:

# 1,0,2,8,2,1,3,2,5,2,2,2
# 9,2,4,5,2,4,2,4,1,10,4,2
# ...etc...
# Please write two functions, named matrix_sum and matrix_max. Both go through the matrix in the file, and then 
# return the sum of the elements or the element with the greatest value, as the names of the functions imply.

# Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. 
# For example, calling row_sums when the matrix in the file is defined as

# 1,2,3
# 2,3,4
# the function should return the list [6, 9].


## Solution:

def row_sums():
    with open("matrix.txt") as matrix_file:
        row_sum = []
        for matrix in matrix_file:
            matrix = matrix.replace("\n","")
            matrix = [int(num) for num in matrix.split(",")]
            row_sum.append(sum(matrix))
    return row_sum

def matrix_max():
    with open("matrix.txt") as matrix_file:
        row_max = 0
        for matrix in matrix_file:
            matrix = matrix.replace("\n","")
            matrix = [int(num) for num in matrix.split(",")]
            if max(matrix) > row_max:
                row_max = max(matrix)
    return row_max

def matrix_sum():
    with open("matrix.txt") as matrix_file:
        sum_of_all = 0
        for matrix in matrix_file:
            matrix = matrix.replace("\n","")
            matrix = [int(num) for num in matrix.split(",")]
            for num in matrix:
                sum_of_all += num
    return sum_of_all


if __name__ == "__main__":
    print(matrix_sum(),matrix_max() )

            

