def remBin(numerator):
	modulus = numerator
	while numerator > 31:
		modulus = 0
		while numerator:
			modulus += numerator & 31
			numerator >>= 5
		numerator = modulus
	return modulus
"""
unsigned int n;                      // numerator
const unsigned int s;                // s > 0
const unsigned int d = (1 << s) - 1; // so d is either 1, 3, 7, 15, 31, ...).
unsigned int m;                      // n % d goes here.

for (m = n; n > d; n = m)
{
  for (m = 0; n; n >>= s)
  {
    m += n & d;
  }
}
// Now m is a value from 0 to d, but since with modulus division
// we want m to be 0 when it is d.
m = m == d ? 0 : m;
"""
