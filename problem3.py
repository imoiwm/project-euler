from math import sqrt, floor
def problem3(n):
	prime = 1
	l = 1
	dummy = n
	while True:
		if dummy % l == 0:
			prime = l
			dummy //= l
			l = 1
		if dummy == l:
			break
		l += 1
	print(prime)
problem3(600851475143)



	

























"""l = []
primo = []
u = floor(sqrt(n))
for x in range(1, u):
if n % x == 0:
l.append(x)
for m in l:
if m
print(l)

prime(600851475143)"""
