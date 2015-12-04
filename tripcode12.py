import base64
import hashlib

def trip12(key):
	key = key.encode('cp932') 
	assert len(key) >= 12
	code = hashlib.sha1(key).digest()
	code = base64.b64encode(code, b'./')
	code = code[:12]
	code = code.decode('cp932')
	return code
