def pal():
	l = []
	pal = []
	for x in reversed(range(100, 1000)):
		for s in reversed(range(100, 1000)):
			r = s * x
			p = str(r)[::-1]
			if str(r) == p:
				pal.append(r)
	print(max(pal))

pal()


