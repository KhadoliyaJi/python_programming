# Please write a program which asks the user to type in some text. Your program should then perform a spell check,
#  and print out feedback to the user, so that all misspelled words have stars around them. Please see the two 
# examples below:

# Sample output
# Write text: We use ptython to make a spell checker

# We use *ptython* to make a spell checker
# Sample output
# Write text: This is acually a good and usefull program

# This is *acually* good and *usefull* program
# The case of the letters should be irrelevant to the functioning of your program.

# The exercise template includes the file wordlist.txt, which contains all the words the spell checker should 
# accept as correct.


## Solution:
dataset = {}
with open("wordlist.txt") as file_data:
    for data in file_data:
        data = data.replace("\n", "")
        dataset[data] = data

sentence = input("Write text: ")
sentence = sentence.split(" ")
output = ''
for word in sentence:
    if word.lower() in dataset:
        output += f"{word} "
    else:
        output += f"*{word}* "
        
# for word in sentence:
#     temp = word.lower()
#     if temp in dataset:
#         output += f"{word} "
#     else:
#         output += f"*{word}* "

print(output)
    


