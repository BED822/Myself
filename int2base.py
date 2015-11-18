def int2base(num, base, alph):
	if isinstance(num, complex) == True: 
		# return a tuple
		return int2base(num.real, base, alph), int2base(num.imag, base, alph)
	assert isinstance(num, int) == True, "Error: not a number"
	if alph == '':
		alph ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	assert 2 <= abs(base) <= len(alph), "Base out of range"
	assert ' ' not in alph, "Error: alphabet contains space"
	if num == 0:
		# return 0
		return alph[0]
	if num < 0 and base > 0:
		if '-' not in alph:
			# return negative integer to positive base with minus
			return  '--' + int2base(-num, base, alph)
		elif '~' not in alph:
			# return negative integer to positive base with tilde
			return  '~~' + int2base(-num, base, alph)
		else:
			# return negative integer to positive base with word
			return  'negative ' + int2base(-num, base, alph)
	converted = ''
	while num != 0:
		unit = posmod(num, base)
		# Can't just do a straight floor-div here
		# That would break negative bases
		# Doing this allows us to "carry the one"
		num = (num - unit) // base
		converted = alph[unit] + converted
	return converted

def posmod(num, den):
	# Modulo constrained to 0..abs(den)
	result = num % den
	if result < 0:
		result += abs(den)
	return result

def checkDubs(num, base):
	assert isinstance(num, int) == True, "Error: not a number"
	if isinstance(num, complex) == True: 
		# return a tuple
		return checkDubs(num.real, base), checkDubs(num.imag, base)
	text = int2base(num, base, '')
	revtext = text[::-1]
	length = len(revtext)
	last = revtext[0]
	tuple = 0
	while(tuple <= num):
		if last != revtext[tuple]:
			break
		tuple = tuple + 1
	if last != '0':
		if tuple == length:
			return "Full num GET"
		elif tuple == length - 1:
			return "Half num GET"
	elif last == '0' and tuple == length - 1:
		if text[0] == '1':
			return "Full zero GET"
		elif text[0] != '1':
			return "Half zero GET"
	elif tuple > 1:
		return str(tuple) + "-tuple " + str(last) + "-s"
	else:
		return "Last digit is " + str(last)

def superDubs(num):
	assert isinstance(num, int) == True, "Error: not a number"
	for i in range (8, 63):
		print("base" + str(i) + ": " + str(checkDubs(num, i)))

def checkPalindrome(num, base):
    assert isinstance(num, int) == True, "Error: not a number"
	if isinstance(num, complex) == True: 
		# return a tuple
		return checkPalindrome(num.real, base), checkPalindrome(num.imag, base)
	text = int2base(num, base, '')
	revtext = text[::-1]
	length = len(revtext)
    for i in range(0, length-2): #Since doubles are not palindromes
        fliptext = revtext[:-i]
        revfliptext = fliptext[::-1]
        if fliptext == revfliptext:
            print(str(length-i) + "-tuple palindrome")
            break

def egcd(big, small):
    old_a = big
    new_a = small
    qArray = [-1]
    q = old_a / new_a
    r = old_a % new_a
    while r != 0:
        qArray.append(q)
        old_a = new_a
        new_a = r
        q = old_a / new_a
        r = old_a % new_a
    gcd = q
    qArray = qArray[::-1]
    old_y = 0
    new_y = 1
    while qArray[0] != -1:
        sum = new_y * qArray.pop(0) + old_y
        old_y = new_y
        new_y = sum
    return new_y, old_y
