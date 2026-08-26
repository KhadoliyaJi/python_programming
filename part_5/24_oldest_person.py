# Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. In each 
# tuple, the first element is the name of a person, and the second element is their year of birth. The function 
# should find the oldest person on the list and return their name.

# An example of the function in action:

# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# print(oldest_person(people))
# Sample output
# Mary

## Solution:

# To access the second element of a tuple stored inside a list, you use the double index notation 
# list_name[list_index][tuple_index]. 
# Because Python uses zero-based indexing, the first bracket targets the tuple's position in the list, and the 
# second bracket [] targets the item inside that specific tuple

# def oldest_person(people_list : list):
#     oldest = people_list[0][1]
#     older_person = people_list[0][0]

#     for person in people_list:
#         if person[1] < oldest:
#             oldest = person[1]
#             older_person = person[0]
#     return older_person

## Another form
def oldest_person(people_list : list):
    oldest_person = people_list[0]
    for person in people_list:
        if person[1] < oldest_person[1]:
            oldest_person = person
    return oldest_person[0]

if __name__ == "__main__":

    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))
    

