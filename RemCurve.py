rem266(n):
	m = n
	while n > ((1 << 266) - 1):
		m = 0
		while n != 0:
			m += n & ((1 << 266) - 1)
			n >>= a
			n *= 3
		n = m
	if m + 3 >= (1 << 266):
		return m + 3 - (1 << 266)
	return m

rem521(n):
	m = n
	while n > ((1 << 521) - 1):
		m = 0
		while n != 0:
			m += n & ((1 << 521) - 1)
			n >>= 521
			n *= 1
		n = m
	if m + 1 >= (1 << 521):
		return m + 1 - (1 << 521)
	return m
