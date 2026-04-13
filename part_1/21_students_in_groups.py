# Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.

# Sample output
# How many students on the course? 8
# Desired group size? 4
# Number of groups formed: 2

# Sample output
# How many students on the course? 11
# Desired group size? 3
# Number of groups formed: 4

# Solution:
num_of_students = int(input("How many students on the course?"))
grp_size = int(input("Desired group size?"))

if(num_of_students%grp_size == 0):
    print(f"Number of groups formed: {num_of_students/grp_size}")
else:
    print(f"Number of groups formed: {int(num_of_students/grp_size)+1}")