# Please write a function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments, 
# and creates and returns a tuple based on the following criteria:

# The first element in the tuple is the smallest of the arguments
# The second element in the tuple is the greatest of the arguments
# The third element in the tuple is the sum of the arguments
# An example of its use:


# if __name__ == "__main__":
#     print(create_tuple(5, 3, -1))
# Sample output
# (-1, 5, 7)

## Solution:

# def create_tuple(x : int, y : int, z : int):
#     sum = x+y+z
#     if x < y and x < z:
#         if y>z:
#             new_tuple = (x, y, sum)
#         elif z>y:
#             new_tuple = (x, z, sum)
#     elif y < x and y < z:
#         if x>z:
#             new_tuple = (y, x, sum)
#         elif z>x:
#             new_tuple = (y, z, sum)
#     if z < x and z < y:
#         if y>x:
#             new_tuple = (z, y, sum)
#         elif x>y:
#             new_tuple = (z, x, sum)
#     return new_tuple

# ## Simple use of sorted() function
# def create_tuple(x : int, y : int, z : int):
#     temp_list = sorted([x, y, z])
#     return (temp_list[0], temp_list[-1], sum(temp_list))

## Use of Min and Max functions
def create_tuple(x : int, y : int, z : int):
    return (min(x, y, z), max(x, y, z), x+y+z)

if __name__ == "__main__":
    print(create_tuple(100, 102, 303))



