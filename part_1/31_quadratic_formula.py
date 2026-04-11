# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# a = int(input(print("Value of a:")))
# b = int(input(print("Value of b:")))
# c = int(input(print("Value of c:")))

# x1 = (-b + sqrt((b**2)-4*a*c))/(2*a)
# x2 = (-b - sqrt((b**2)-4*a*c))/(2*a)
# # x2 = (-b - sqrt(b²-4ac))/(2a)
# print(f"The roots are {x1} and {x2}")

import math

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

# Calculating the discriminant
discriminant = b**2 - 4*a*c

# Check if discriminant is non-negative
if discriminant < 0:
    print("No real roots")
else:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The roots are {root1} and {root2}")
