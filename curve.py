def isCurve(a, b, prime):
	sum = 4 * a ^ 3 + 27 * b ^ 2
	if 0 == sum % prime:
		return true
	else:
		return false
		
def isPoint(a, b, x, y, prime):
	assert isCurve(a, b, prime), "not a curve"
	left = ( y ^ 2 ) % prime
	right = ( x ^ 3 + a * x + b ) % prime
	if left == right:
		return true
	else:
		return false
def curveAdd(xP, yP, xQ, yQ, prime):
	if yP == xP and yQ = ( prime - xQ ):
		assert error "no solution"
	if yP == xP and yQ == xQ:
		return curveDouble(x, y, prime)
	slope = ( ( yP - yQ ) / ( xP - xQ ) ) % p
	xR = ( slope ^ 2 - xP - xQ ) % prime
	yR = - yP + slope * (xP - xR) % p
	return xR, yR, slope
def curveDouble(xP, yP, prime):
	slope = ( ( 3 * xP ^ 2 + a ) / ( 2 * yP ) ) % p
	xR =  ( s ^ 2 - 2 * xP ) % p
	yR = - yP + slope * ( xP - xR ) % p
