# Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new list containing the even numbers from the original list.

# my_list = [1, 2, 3, 4, 5]
# new_list = even_numbers(my_list)
# print("original", my_list)
# print("new", new_list)
# Sample output
# original [1, 2, 3, 4, 5]
# new [2, 4]

## Solution:

def even_numbers(given_list : list):
    even_number_list = []
    for i in given_list:
        if i % 2 == 0:
            even_number_list.append(i)
    return even_number_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)