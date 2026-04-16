# Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

# Some examples:

# Sample output
# Please type in a year: 2011
# That year is not a leap year.

# Sample output
# Please type in a year: 2020
# That year is a leap year.

# Sample output
# Please type in a year: 1800
# That year is not a leap year.

# Solution:
year = int(input("Please enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("That year is a leap year.")
        else:
            print("That year is not a leap year.")
    else:
        print("That year is a leap year.")
else:
    print("That year is not a leap year.")