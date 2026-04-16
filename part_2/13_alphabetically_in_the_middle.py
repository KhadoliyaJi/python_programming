# Please write a program which asks the user for three letters. The program should then print out whichever of 
# the three letters would be in the middle if the letters were in alphabetical order.

# You may assume the letters will be either all uppercase, or all lowercase.

# Some examples of expected behaviour:

# Sample output
# 1st letter: x
# 2nd letter: c
# 3rd letter: p
# The letter in the middle is p

# Sample output
# 1st letter: C
# 2nd letter: B
# 3rd letter: A
# The letter in the middle is B

# Soluton:

f_letter = input("1st letter:")
s_letter = input("2nd letter:")
t_letter = input("3rd letter:")

if f_letter > s_letter and f_letter < t_letter:
    print("The letter in the middle is", f_letter)
elif f_letter < s_letter and f_letter > t_letter:
    print("The letter in the middle is", f_letter)
elif s_letter > f_letter and s_letter < t_letter:
    print("The letter in the middle is", s_letter)
elif s_letter < f_letter and s_letter > t_letter:
    print("The letter in the middle is", s_letter)
elif t_letter > f_letter and t_letter < s_letter:
    print("The letter in the middle is", t_letter)
elif t_letter < f_letter and t_letter > s_letter:
    print("The letter in the middle is", t_letter)