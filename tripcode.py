def trip8(password, length):
	assert length >=7, "length is less than 8"
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
####################################################################################
import base64
import hashlib
def tripSHA(key, length):
	assert 27 > length >= 8
	key = key.encode('cp932') 
	assert len(key) >= length
	trip = hashlib.sha1(key).digest()
	trip = base64.b64encode(trip, b'./')
	trip = trip[:length]
	trip = trip.decode('cp932')
	return trip
