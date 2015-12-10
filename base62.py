digits='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def check_block(exp):
	if exp != 256 and exp != 160 and exp != 112:
		return false
	elif exp == 256:
		base, limit = 62, 43
	elif exp == 160:
		base, limit = 61, 27
	elif exp == 112:
		base, limit = 60, 19

def encode_block(num, exp):
	assert check_block(exp) != false, "bad exponent"
	base, limit = check_block(exp)
	assert num >= 0, "not positive"
	assert num < (2 ** exp), "too big"
	if num == 0:
		return '0'.zfill(limit)
	str=''
	while num != 0:
		num, char = divmod(num, base)
		str = (digits[char]) + str
	return str.zfill(limit) + "_" + str(base)

def decode_block(num, exp):
	assert check_block(exp) != false, "bad exponent"
	base, limit = check_block(exp)
	assert len(str) <= limit, "too long"
	str = str.lstrip("0")
	num , mult = 0 , 1
	for char in reversed(str):
		num += mult * digits.index(char)
		mult *= base
	assert num < (2 ** exp), "number error"
	return num

def check(exp):
	if exp % 16 != 0:
		return false
	exp //= 16
	if exp % 16 == 0:
		return 62, 43, exp // 16
	elif exp % 10 == 0:
		return 61, 27, exp // 10
	elif exp % 7 == 0:
		return 60, 19, exp // 7
