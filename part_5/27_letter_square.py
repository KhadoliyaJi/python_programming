# This final exercise in this part is a relatively demanding problem solving task. It can be solved in many 
# different ways. Even though this current section in the material covers tuples, tuples are not necessarily the 
# best way to go about solving this.

# Please write a program which prints out a square of letters as specified in the examples below. You may assume 
# there will be at most 26 layers.

# Sample output
# Layers: 3

# CCCCC
# CBBBC
# CBABC
# CBBBC
# CCCCC
# Sample output
# Layers: 4

# DDDDDDD
# DCCCCCD
# DCBBBCD
# DCBABCD
# DCBBBCD
# DCCCCCD
# DDDDDDD

## Solution:


layers = int(input("Layers: "))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

size = (layers * 2) - 1 

mid = size // 2

for i in range(size):
    row = ""

    for j in range(size):
        distance = max(abs(i - mid), abs(j - mid))
        row += alphabet[distance]

    print(row)

