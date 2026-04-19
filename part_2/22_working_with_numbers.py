# Pre-task
# Please write a program which asks the user for integer numbers. The program should keep asking for numbers until 
# the user types in zero.

# Sample output
# Please type in integer numbers. Type in 0 to finish.
# Number: 5
# Number: 22
# Number: 9
# Number: -2
# Number: 0

# # Solution
# print("Please type in integer numbers. Type in 0 to finish.")
# while True:
#     input_number = int(input("Number: "))

#     if input_number == 0 :
#         break

### Part 1: Count

# After reading in the numbers the program should print out how many numbers were typed in. The zero at the 
# end should not be included in the count.

# You will need a new variable here to keep track of the numbers typed in.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4

# # Solution:

# print("Please type in integer numbers. Type in 0 to finish.")
# count = 0
# while True:
#     input_number = int(input("Number: "))
#     if input_number == 0 :
#         break
#     count +=1
# print("Numbers typed in", count)

### Part 2: Sum
# The program should also print out the sum of all the numbers typed in. The zero at the end should not be 
# included in the calculation.

# The program should now print out the following:

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34

# # Solution:

# print("Please type in integer numbers. Type in 0 to finish.")
# count = 0
# sum = 0
# while True:
#     input_number = int(input("Number: "))
#     if input_number == 0 :
#         break
#     count +=1
#     sum += input_number
# print("Numbers typed in", count)
# print("The sum of the numbers is", sum)


### Part 3: Mean
# The program should also print out the mean of the numbers. The zero at the end should not be included in the 
# calculation. You may assume the user will always type in at least one valid non-zero number.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34
# The mean of the numbers is 8.5

# # Solution:

# print("Please type in integer numbers. Type in 0 to finish.")
# count = 0
# sum = 0
# while True:
#     input_number = int(input("Number: "))
#     if input_number == 0 :
#         break
#     count +=1
#     sum += input_number
# print("Numbers typed in", count)
# print("The sum of the numbers is", sum)
# print("The mean of the numbers is", sum/count)

### Part 4: Positives and negatives
# The program should also print out statistics on how many of the numbers were positive and how many were negative. 
# The zero at the end should not be included in the calculation.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34
# The mean of the numbers is 8.5
# Positive numbers 3
# Negative numbers 1

# Solution:

print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum = 0
positive_number = 0
negative_number = 0
while True:
    input_number = int(input("Number: "))
    if input_number == 0 :
        break
    if input_number > 0:
        positive_number += 1
    elif input_number < 0:
        negative_number += 1
    count +=1
    sum += input_number
    
print("Numbers typed in", count)
print("The sum of the numbers is", sum)
print("The mean of the numbers is", sum/count)
print("Positive numbers", positive_number)
print("Negative numbers", negative_number)

