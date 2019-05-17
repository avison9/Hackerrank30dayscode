#Task 
#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird
#Complete the stub code provided in your editor to print whether or not  is weird.

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N % 2 != 0:
        print("Weird")
    if N >= 2 and N <= 5:
        if N % 2 == 0:
            print("Not Weird")
    if N >= 6 and N <=20:
        if N % 2 == 0:
            print("Weird")
    if N > 20 and N % 2 == 0:
        print("Not Weird")
