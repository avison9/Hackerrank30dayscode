# Task 
# Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! ( N factorial).

# Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

# Input Format

# A single integer, N (the argument to pass to factorial).

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n == 0:
        return 1
    elif n >0:
        return n * factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
