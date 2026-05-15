# Please write a function named all_the_longest, which takes a list of strings as its argument. The function should return a new list containing the longest string in the original list. If more than one are equally long, the function should return all of the longest strings.

# The order of the strings in the returned list should be the same as in the original.

# my_list = ["first", "second", "fourth", "eleventh"]
# result = all_the_longest(my_list)
# print(result) # ['eleventh']

# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
# result = all_the_longest(my_list)
# print(result) # ['dorothy', 'richard']

## Solution:

# def all_the_longest(given_list : list):
#     new_list = []
#     longest = len(given_list[0])
#     for i in given_list:
#         if len(i) >= longest:
#             longest = len(i)
#             new_list.append(i)
    
#     i = 0
#     while i < len(new_list):
#         if len(new_list[i]) < longest:
#             new_list.pop(i)
#             i = 0
#         else:
#             i += 1
#     return new_list


# cleaner version 

def all_the_longest(given_list : list):
    new_list = []
    longest = 0

    for word in given_list:
        if len(word) > longest:
            longest = len(word)
            new_list = [word]
        
        elif len(word) == longest:
            new_list.append(word)
    
    return new_list


if __name__ == "__main__":

    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
