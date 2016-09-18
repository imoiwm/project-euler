def euler5():
	l = [11,13,14,16,17,18,19,20]
	product = 1
	for x in l:
		product *= x

	i = 0
	while i <= product:
		c = 0
		if i != 0:
			for n in l:
				if i % n == 0:
					c += 1
		if c == 8:
			print(i)
			break
		i += 6466460 #Least common multiple of 7, 11, 13, 17, 19, and 20. 


euler5()
