# In this exercise we are handling tuples just like the ones described in the previous exercise.

# Please write a function named older_people(people: list, year: int), which selects all those people on the list 
# who were born before the year given as an argument. The function should return the names of these people in a new 
# list.

# An example of its use:

# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# older = older_people(people, 1979)
# print(older)
# Sample output
# [ 'Adam', 'Mary' ]

## Solution:

def older_people(person : list, year : int):

    older_persons = []
    for people in person:
        if people[1] < year:
            older_persons.append(people[0])
    return older_persons

if __name__ == "__main__":

    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)


