#!/usr/bin/python3

def is_prime(number):
    # Numbers less than or equal to 1 are not prime
    if number <= 1:
        return False

    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    # If the number is not divisible by any smaller number, it is prime
    return True
