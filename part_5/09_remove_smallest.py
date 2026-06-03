# Please write a function named remove_smallest(numbers: list), which takes a list of integers as its 
# argument.

# The functions should find and remove the smallest item in the list. You may assume there is a single 
# smallest item in the list.

# The function should not have a return value - it should directly modify the list it receives as a 
# parameter.

# An example of how the function works:

# if __name__ == "__main__":
#     numbers = [2, 4, 6, 1, 3, 5]
#     remove_smallest(numbers)
#     print(numbers)
# Sample output
# [2, 4, 6, 3, 5]

## Solution:

def remove_smallest(numbers : list):
    
    # method_1 : finding smallest through a loop and use of function remove
    smallest = numbers[0]
    for item in numbers:
        if item < smallest:
            smallest = item
    numbers.remove(smallest)

    # method_2 : creating a new list and finding smallest during creation with a helper variable 
    # smallest = numbers[0]
    # new_list = []
    # for item in numbers:
    #     if item > smallest:
    #         new_list.append(item)
    #     elif item < smallest:
    #         new_list.append(smallest)
    #         smallest = item
    # numbers[:] = new_list    
    

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)


    