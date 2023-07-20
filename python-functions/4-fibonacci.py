#!/usr/bin/python3

def fibonacci_sequence(n):
    sequence = []

    # Handle edge case for n <= 0
    if n <= 0:
        return sequence

    # Append the first Fibonacci number(s) depending on n
    if n >= 1:
        sequence.append(0)
    if n >= 2:
        sequence.append(1)

    # Generate the remaining Fibonacci numbers
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence
