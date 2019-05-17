# Task 
# Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

# Note: 0 is considered to be an even index.

test_cases = int(input())
for i in range(test_cases):
    word = str(input().strip())
    even = word[::2]
    odd = word[1::2]
    print(even, odd)