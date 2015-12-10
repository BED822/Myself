digits='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encode(num, exp):
	assert exp == 256 or exp == 160 or exp == 112, "exp not valid"
	if exp == 256:
		base, limit = 62, 43
	elif exp == 160:
		base, limit = 61, 27
	elif exp == 112:
		base, limit = 60, 19
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
	assert exp == 256 or exp == 160 or exp == 112, "exp not valid"
	if exp == 256:
		base, limit = 62, 43
	elif exp == 160:
		base, limit = 61, 27
	elif exp == 112:
		base, limit = 60, 19
	assert len(str) <= limit, "too long"
	str = str.lstrip("0")
	num , mult = 0 , 1
	for char in reversed(str):
		num += mult * digits.index(char)
		mult *= base
	assert num < (2 ** exp), "number error"
	return num
