#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

while True:
    try:
        num_terms = int(input("Enter a positive number for how many Fibonacci terms to display: "))
        if num_terms > 0:
            break
        print("Number must be positive.")
    except ValueError:
        print("Please enter a valid positive integer.")

first, second = 0, 1

if num_terms == 1:
    print(first)
elif num_terms == 2:
    print(first, second)
else:
    print(first, second, end=" ")
    for _ in range(3, num_terms + 1):
        next_term = first + second
        print(next_term, end=" ")
        first, second = second, next_term
    print()
