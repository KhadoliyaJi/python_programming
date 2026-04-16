# Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.

# Some examples of expected behaviour:

# Sample output
# Person 1:
# Name: Alan
# Age: 26
# Person 2:
# Name: Ada
# Age: 27
# The elder is Ada

# Sample output
# Person 1:
# Name: Bill
# Age: 1
# Person 2:
# Name: Jean
# Age: 1
# Bill and Jean are the same age

# Solution:


f_person = input("Persin 1:\nNane:")
f_age = int(input("Age:"))
s_person = input("Persin 2:\nName:")
s_age = int(input("Age:"))

if f_age > s_age:
    print("The elder is", f_person)
elif s_age > f_age:
    print("The elder is", s_person)
else:
    print(f"{f_person} and {s_person} are the same age")