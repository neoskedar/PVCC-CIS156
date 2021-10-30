# Modify the code below
"""
File: newton.py
Project 6.2
Compute the square root of a number (uses recursive function).
1. The input is a number, or enter/return to halt the
   input process.
2. The outputs are the program's estimate of the square root
   using Newton's method of successive approximations, and
   Python's own estimate using math.sqrt.
"""

import math


# Initialize the tolerance
TOLERANCE = 0.000001

def newton(x):
        
# Initialize the tolerance and estimate
        tolerance = 0.000001
        estimate = 1.0

# Perform the successive approximations
        while True:
            estimate = (estimate + float(x) / estimate) / 2
            difference = abs(float(x) - estimate ** 2)
            if difference <= tolerance:
                break
        
        return (estimate)

def main():
    """Allows the user to obtain square roots."""
    while True:
        # Receive the input number from the user
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
             break
        x = float(x)
        # Output the result
        print("The program's estimate is", newton(x))
        print("Python's estimate is     ", math.sqrt(x))

if __name__ == "__main__":
    main()