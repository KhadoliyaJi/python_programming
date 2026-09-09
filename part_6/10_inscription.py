# Please write a program which asks for the name of the user and then creates an "inscription" in a file specified 
# by the user. Please see the example below.

# Sample output
# Whom should I sign this to: Ada 
# Where shall I save it: inscribed.txt

# The contents of the file inscribed.txtwould be

# Sample data
# Hi Ada, we hope you enjoy learning Python with us! Best, Mooc.fi Team

## Solution:


person_name = input("Whom should I sign this to: ")
file_name = input("Where shall I save it: ")

with open(file_name , 'w') as file_data:
    file_data.write(f"Hi {person_name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
