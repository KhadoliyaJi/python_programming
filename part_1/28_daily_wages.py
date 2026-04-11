# Write your solution here
wage = float(input("Hourly wage:"))
worked = int(input("Hourls worked:"))
day = input("Day of the week:")
if (day == 'Sunday'):
    print(f"Daily wages: {2*wage*worked} euros")
else :
    print(f"Daily wages: {wage*worked} euros")