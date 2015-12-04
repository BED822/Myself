import base64
import hashlib

def trip12(key, length):
	assert 27 > len(key) >= 8
	key = key.encode('cp932') 
	assert len(key) >= length
	code = hashlib.sha1(key).digest()
	code = base64.b64encode(code, b'./')
	code = code[:length]
	code = code.decode('cp932')
	return code
