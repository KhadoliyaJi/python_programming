# Write your solution here
num_of_students = int(input("How many students on the course?"))
grp_size = int(input("Desired group size?"))

if(num_of_students%grp_size == 0):
    print(f"Number of groups formed: {num_of_students/grp_size}")
else:
    print(f"Number of groups formed: {int(num_of_students/grp_size)+1}")