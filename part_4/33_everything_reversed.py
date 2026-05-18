# Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list.

# An example of how the function should work:

# my_list = ["Hi", "there", "example", "one more"]
# new_list = everything_reversed(my_list)
# print(new_list)
# Sample output
# ['erom eno', 'elpmaxe', 'ereht', 'iH']

## Solution:

# def everything_reversed(given_list : list):
#     changed_list = []
#     new_word = ''

#     for word in range(len(given_list) - 1, -1, -1):
#         word = given_list[word]
#         for char in range(len(word) -1, -1, -1):
#             new_word += word[char]
#         changed_list.append(new_word)
#         new_word = ''    

#     return changed_list

## another version:

def everything_reversed(given_list : list):
    changed_list = []

    for word in given_list[::-1]:
        changed_list.append(word[::-1])
    
    return changed_list



if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)




