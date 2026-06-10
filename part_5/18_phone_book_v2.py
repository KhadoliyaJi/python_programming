# Please write an improved version of the phone book application. Each entry should now accommodate 
# multiple phone numbers. The application should work otherwise exactly as above, but this time all 
# numbers attached to a name should be printed.

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
# 040-5466745 09-22223333 command (1 search, 2 add, 3 quit): 3 
# quitting...

## Solution:

new_dict = {}

while True:
    entered = int(input("command (1 search, 2 add, 3 quit): "))

    if entered == 2:
        key = (input("name: "))
        value = (input("number: "))
        print("ok! ")
        if key not in new_dict:
            new_dict[key] = []
        new_dict[key].append(value) 
    
    if entered == 1:
        key = (input("name: "))
        if key in new_dict:
            for num in new_dict[key]:
                print(num)
        else:
            print("no number ")
    if entered == 3:
        print("quitting...")
        break
