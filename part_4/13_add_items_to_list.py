# Please write a program which first asks the user for the number of items to be added. 
# Then the program should ask for the given number of values, one by one, and add them to a 
# list in the order they were typed in. Finally, the list is printed out.

# An example of expected behaviour:

# Sample output
# How many items: 3
# Item 1: 10
# Item 2: 250
# Item 3: 34
# [10, 250, 34]

## Solution:

my_list = []
range = int(input("How many items: "))
index = 1
limit = 1

while limit <= range:
    list_value = int(input(f"Item {index}: "))
    my_list.append(list_value)
    index += 1
    limit += 1
print(my_list)




