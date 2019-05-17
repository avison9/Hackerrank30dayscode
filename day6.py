n = int(input())
while n >= 2 and n <= 20:
	for i in range (1,11):
		j = n * i
		print(n, "x", i, '=', j)
	break