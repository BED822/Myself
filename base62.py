RFC1924 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~'
ZeroMQ = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-:+=^!/*?&<>()[]{}@%$#'
Adobe = !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstu

# [0, 3, 6, 9, 11, 14, 17, 19, 22, 25, 27, 30, 33, 35, 38, 41, 43]
# n-th element = number of character needed to represent 16*i bits

def number_of_characters(bits, base):
	assert bits % 16 == 0, "not 16"
	bits //= 16
	if base == 62:
		unit, char = 16, 43
	elif base == 61:
		unit, char = 10, 27
	elif base == 60:
		unit, char = 7, 19
	else:
		return False
	answer = ( bits // units ) * char
	bits %= units
	array = [0, 3, 6, 9, 11, 14, 17, 19, 22, 25, 27, 30, 33, 35, 38, 41]
	answer += array[bits]
	return answer

def check_block(exp):
	if exp % 16 != 0:
		return False
	exp //= 16
	if exp % 16 == 0:
		return 62, 43, exp // 16
	elif exp % 10 == 0:
		return 61, 27, exp // 10
	elif exp % 7 == 0:
		return 60, 19, exp // 7
	else:
		return False

def encode_block(num, exp):
	assert check_block(exp) != False, "bad exponent"
	base, limit = check_block(exp)
	assert num >= 0, "not positive"
	assert num < (2 ** exp), "too big"
	if num == 0:
		return '0'.zfill(limit)
	str=''
	while num != 0:
		num, char = divmod(num, base)
		str = (digits[char]) + str
	return str.zfill(limit)

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

def rem(n, a, b):
	m = n
	while n > ((1 << a) - 1):
		m = 0
		while n != 0:
			m += n & ((1 << a) - 1)
			n >>= a
			n *= b
		n = m
	if m + b >= (1 << a):
		return m + b - (1 << a)
	return m

#########

def encode_block56(num):
	limit = 11285
	assert num >= 0, "not positive"
	assert num < (2 ** 65536), "too big"
	if num == 0:
		return '0'.zfill(11285)
	str=''
	while num != 0:
		num, char = divmod(num, 56)
		str = (digits[char]) + str
	return str.zfill(11285)

def encode_block85(num):
	assert num >= 0, "not positive"
	assert num < (2 ** 65536), "too big"
	if num == 0:
		return '0'.zfill(10225)
	str=''
	while num != 0:
		num, char = divmod(num, 85)
		str = (digits[char]) + str
