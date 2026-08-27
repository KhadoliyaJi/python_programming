# The file numbers.txt contains integer numbers, one number per line. The contents could look like this:

# 2
# 45
# 108
# 3
# -10
# 1100
# ...etc...
# Please write a function named largest, which reads the file and returns the largest number in the file.

# Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.


## Solution:

def largest():
    with open("numbers.txt") as numbers_file:
        largest = 0
        for number in numbers_file:
            
            number = int(number)

            if number > largest:
                largest = number
    return largest


if __name__ == "__main__":
    print(largest())
