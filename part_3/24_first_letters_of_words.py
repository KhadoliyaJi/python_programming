# Please write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line.

# An example of expected behaviour:

# Sample output
# Please type in a sentence: Humpty Dumpty sat on a wall
# H
# D
# s
# o
# a
# w

## Solution:

# Write your solution here
input_string = input("Please type in a sentance:")

list_of_words = input_string.split() 
# The split() function breaks a string into smaller parts (words) and stores them in a list.
# Python looks for spaces " " [spaces are default value which can also be specified] in the sentence.
# Whenever it finds a space:
# it separates the text before and after the space into different words.
index = 0
while index < len(list_of_words):
    print(list_of_words[index][0])
    index +=1
