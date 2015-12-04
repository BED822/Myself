def mktripcode(password, length):
	if l < 8:
		assert error "length is less than 8"
	password = password.decode('utf_8', 'ignore') \
		.encode('shift_jis', 'ignore') \
		.replace('"', '&quot;') \
		.replace("'", '') \
		.replace('<', '&lt;') \
		.replace('>', '&gt;') \
		.replace(',', ',')
	salt = (password + '...')[1:3]
	salt = re.compile('[^\.-z]').sub('.', salt)
	salt = salt.translate(string.maketrans(':;<=>?@[\\]^_`', 'ABCDEFGabcdef'))
	trip = crypt.crypt(password, salt)[-length:]
	return trip
