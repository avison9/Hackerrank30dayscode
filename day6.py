# Task 
# Given an integer, n, print its first 10 multiples. Each multiple n x i  (where 1 <= i >=10) should be printed on a new line in the form: n x i = result.

n = int(input())
while n >= 2 and n <= 20:
	for i in range (1,11):
		j = n * i
		print(n, "x", i, '=', j)
	break