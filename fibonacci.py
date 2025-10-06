#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many term

while True:
    try:
        terms = int(input("Enter the number of terms: "))
        if terms <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Initialize first two Fibonacci numbers
n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")

# Generate Fibonacci sequence
for i in range(terms):
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
