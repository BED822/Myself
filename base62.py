digits='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decode256(str):
	assert len(str) <= 43, "too long"
	str = str.lstrip("0")
	num , mult = 0 , 1
	for char in reversed(str):
		num += mult * digits.index(char)
		mult *= 62
	assert num < (2 ** 256), "number error"
	return num

def encode256(num):
	assert num >= 0, "not positive"
	assert num < (2 ** 256), "too big"
	if num == 0:
		return '0'.zfill(43)
	str=''
	while num != 0:
		num, char = divmod(num, 62)
		str = (digits[char]) + str
	return str.zfill(43)

def decode160(str):
	assert len(str) <= 27, "too long"
	str = str.lstrip("0")
	num , mult = 0 , 1
	for char in reversed(str):
		num += mult * digits.index(char)
		mult *= 61
	assert num < (2 ** 160), "number error"
	return num

def encode160(num):
	assert num >= 0, "not positive"
	assert num < (2 ** 160), "too big"
	if num == 0:
		return '0'.zfill(43)
	str=''
	while num != 0:
		num, char = divmod(num, 61)
		str = (digits[char]) + str
	return str.zfill(27)
