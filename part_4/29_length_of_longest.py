# Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns the length of the longest string.

# my_list = ["first", "second", "fourth", "eleventh"]
# result = length_of_longest(my_list)
# print(result)

# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
# result = length_of_longest(my_list)
# print(result)
# Sample output
# 8
# 7

## Solution:

def length_of_longest(given_list : list):
    longest_string = 0
    for i in given_list:
        if len(i) > longest_string :
            longest_string = len(i)
    return longest_string

if __name__ == "__main__":

    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)


