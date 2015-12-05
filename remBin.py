def remBin(a, n):
	assert a >= 0, "a is not positive"
	while a > x:
		r = a % x
		a = a >> n
		a += r
	return a
