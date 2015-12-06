digits='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encode(num, exp):
	if exp == 256:
		base, limit = 62, 43
	elif exp == 160:
		base, limit = 61, 27
	elif exp == 112:
		base, limit = 60, 19
	else:
		assert "exp not valid"
	assert num >= 0, "not positive"
	assert num < (2 ** exp), "too big"
	if num == 0:
		return '0'.zfill(limit)
	str=''
	while num != 0:
		num, char = divmod(num, base)
		str = (digits[char]) + str
	return str.zfill(limit)

def decode(num, exp):
	if exp == 256:
		base, limit = 62, 43
	elif exp == 160:
		base, limit = 61, 27
	elif exp == 112:
		base, limit = 60, 19
	else:
		assert "exp not valid"
	assert len(str) <= limit, "too long"
	str = str.lstrip("0")
	num , mult = 0 , 1
	for char in reversed(str):
		num += mult * digits.index(char)
		mult *= base
	assert num < (2 ** exp), "number error"
	return num

def rem31(n):
	m = n
	while n > 31:
		m = 0
		while n:
			m += n & 31
			n >>= 5
		n = m
	if m == 31:
		return 0
	return m

def rem15(n):
	m = n
	while n > 15:
		m = 0
		while n:
			m += n & 15
			n >>= 4
		n = m
	if m == 15:
		return 0
	return m

"""
if x & 1 = a and x % 31 = b
then x % 62 = a * 31 * (((31)^(-1))%2) + b * 2 * (((2)^(-1))%31)
or x % 62 = 31 * a + 32 * b (not final form)
if x & 3 = a and x % 31 = b
then x % 60 = a * 15 * (((15)^(-1))%4) + b * 4 * (((4)^(-1))%15)
or x % 60 = 45 * a + 16 * b (not final form)
"""
