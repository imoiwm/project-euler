def fib(n):
	l = [1,2]
	fibe = []
	while l[-1] <= n:
		z = l[-2] + l[-1]
		l.append(z)
	for y in l:
		if y % 2 == 0:
			fibe.append(y) 
		else:
			pass
	print(sum(fibe))

fib(4000000)