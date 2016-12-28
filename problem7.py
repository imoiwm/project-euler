from math import sqrt, floor
def p(n):
	c = 0
	lp = [2,3,5,7,11]
	d = 13
	while c <= (n-6):
		if isitprime(d):
			lp.append(d)
			c += 1
		d += 2
	print(lp[-1])


def isitprime(x):
	c = 0
	y = int(sqrt(x))
	for a in range(2, y+1):
		if x%a == 0:
			c += 1
	if c >= 1:
		return False
	else:
		return True

p(10001)