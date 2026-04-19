# Please write a program which asks the user for a year, and prints out the next leap year.

# Sample output
# Year: 2023
# The next leap year after 2023 is 2024

# If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

# Sample output
# Year: 2024
# The next leap year after 2024 is 2028

# Solution:

#### shorter and complex version:

# year = int(input("Year: "))

# next_year = year + 1

# while True:
#     if (next_year % 4 == 0 and next_year % 100 != 0) or (next_year % 400 == 0):
#         print(f"The next leap year after {year} is {next_year}")
#         break

#     next_year += 1

#### Longer and easier version:

year = int(input("Year: "))
remainder = year % 400

if year % 100 == 0:
    if year % 400 == 0:
        print(f"The next leap year after {year} is {year + 4}")
    else :
        print(f"The next leap year after {year} is {year + 4}")
elif year % 4 == 0:
    if (year + 4) % 100 == 0:
        if (year + 4) % 400 != 0:
            print(f"The next leap year after {year} is {year + 8}")
    else :        
        print(f"The next leap year after {year} is {year + 4}")
elif year % 4 != 0:
    if year % 4 == 1:
        if (year + 3) % 100 == 0:
            if (year + 3) % 400 != 0:
                print(f"The next leap year after {year} is {year + 7}")
            else:
                print(f"The next leap year after {year} is {year + 3}")
                
        else:
            print(f"The next leap year after {year} is {year + 3}")
    elif year % 4 == 2:
        if (year + 2) % 100 == 0:
            if (year + 2) % 400 != 0:
                print(f"The next leap year after {year} is {year + 6}")
            else:
                print(f"The next leap year after {year} is {year + 2}")
        else:
            print(f"The next leap year after {year} is {year + 2}")
    elif year % 4 == 3:
        if (year + 1) % 100 == 0:
            if (year + 1) % 400 != 0:
                print(f"The next leap year after {year} is {year + 5}")
            else:
                print(f"The next leap year after {year} is {year + 1}")
        else:    
            print(f"The next leap year after {year} is {year + 1}")







