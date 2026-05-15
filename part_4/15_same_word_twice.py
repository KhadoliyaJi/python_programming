# Please write a program which asks the user for words. If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.

# Sample output
# Word: once
# Word: upon
# Word: a
# Word: time
# Word: upon
# You typed in 4 different words

## Solutions:

my_list = []
while True:
    input_word = input("Word: ")
    if input_word in my_list :
        print(f"You typed in {len(my_list)} different words")
        break
    my_list.append(input_word)

