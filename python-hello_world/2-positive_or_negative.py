#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# Check if the number is positive, negative, or zero
if number > 0:
    print(number, "is positive")
elif number < 0:
    print(number, "is negative")
else:
    print(number, "is zero")
