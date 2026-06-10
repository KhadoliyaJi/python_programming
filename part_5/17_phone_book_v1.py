# Please write a phone book application. It should work as follows:

# Sample output
# command (1 search, 2 add, 3 quit): 2 
# name: peter 
# number: 040-5466745 
# ok! command (1 search, 2 add, 3 quit): 2 
# name: Emily 
# number: 045-1212344 
# ok! command (1 search, 2 add, 3 quit): 1 
# name: peter 
# 040-5466745 command (1 search, 2 add, 3 quit): 1 
# name: mary 
# no number command (1 search, 2 add, 3 quit): 2 
# name: peter 
# number: 09-22223333 
# ok! command (1 search, 2 add, 3 quit): 1 
# name: peter 
# 09-22223333 command (1 search, 2 add, 3 quit): 3 
# quitting...

# As you can see above, each name can be attached to a single number only. If a new entry with the same 
# name is added, the number attached to the old entry is replaced with the new number.

## Solution:

new_dict = {}

while True:
    entered = int(input("command (1 search, 2 add, 3 quit): "))

    if entered == 2:
        key = (input("name: "))
        value = (input("number: "))
        print("ok! ")
        new_dict[key] = value
    
    if entered == 1:
        key = (input("name: "))
        if key in new_dict:
            print(f"{new_dict[key]} ")
        else:
            print("no number ")
    if entered == 3:
        print("quitting...")
        break


    


