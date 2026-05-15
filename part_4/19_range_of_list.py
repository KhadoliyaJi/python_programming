# Please write a function named range_of_list, which takes a list of integers as an argument. The function returns the difference between the smallest and the largest value in the list.

# my_list = [1, 2, 3, 4, 5]
# result = range_of_list(my_list))
# print("The range of the list is", result)
# Sample output
# The range of the list is 4

## Solution:

def range_of_list(input_list : list):
    maximum = int(max(input_list))
    minimum = int(min(input_list))
    return (maximum - minimum)
    


if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print(result)