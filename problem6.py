def dif():
	a = ssq() - sq()
	print(a)

def sq():
	l = 0
	for q in range(1, 101):
		l += (q * q)
	print(l)


def ssq():
	e = [x for x in range(1, 101)]
	squ = 0
	for y in e:
		squ += y
	ans = (squ * squ)
	print(ans)


dif()
	