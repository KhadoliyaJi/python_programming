# Please write a new version of the program in the previous exercise. In addition to the result it should also print out the calculation performed:

# Sample output
# Limit: 2
# The consecutive sum: 1 + 2 = 3

# Sample output
# Limit: 10
# The consecutive sum: 1 + 2 + 3 + 4 = 10

# Sample output
# Limit: 18
# The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

## Solution:

limit = int(input("Limit: "))
sum = 0
count = 1
expression = ""
while sum < limit :
    sum = sum + count
    if expression == "" :
        expression += str(count)
    else :
        expression += " + " + str(count) 
    count += 1
    

print(f"The consecutive sum: {expression} = {sum}")