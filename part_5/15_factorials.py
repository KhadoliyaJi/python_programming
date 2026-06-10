# Please write a function named factorials(n: int), which returns the factorials of the numbers 1 to 
# nin a dictionary. The number is the key, and the factorial of that number is the value mapped to it.

# A reminder: the factorial of the number nis written n! and is calculated by multiplying the number by 
# each integer smaller than itself. For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.

# An example of the function in action:

# k = factorials(5)
# print(k[1])
# print(k[3])
# print(k[5])
# Sample output
# 1 6 120

## Solution:

def factorials(n : int):
    new_dict = {}
    for i in range(1, n+1):
        value = 1
        for j in range(i, 0, -1):
            value *= j
        new_dict[i] = value
    return new_dict

if __name__ == "_main__":
    
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
     


