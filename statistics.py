from math import log10
from math import modf
from fractions import gcd
from decimal import *

list = [25, 32, 40, 50, 64, 80, 100, 
    125, 128, 160, 200, 250, 256, 320, 
    400, 500, 512, 625, 640, 800, 1000, 
    1024, 1250, 1280, 1600, 2000, 2048,
    2500, 2560, 3125, 3200, 4000, 4096]
"""
<15625 ~16384
(8192) = 2^13*5^0 (16384)
(5120) = 2^10*5^1 (10240)
(6400) = 2^08*5^2 (12800)
(8000) = 2^06*5^3 (16000)
(5000) = 2^03*5^4 (10000)
(6250) = 2^01*5^5 (12500)
"""

def printingPress(key, dec, i, bit, int):
    return key + ": " + str(dec) + " base" + str(i) + " " + str(bit) + "-bits" + " x=" + str(int)

for i in range(56, 96):
	for bit in list:
		x = bit * log10(2) / log10(i)
		dec, int = modf(x)
		dec = round(Decimal(dec), 6) # makes dec managable
		if dec >= Decimal(0.8):
			int = int+ 1 # Ceiling of x (sice dec > 0)
			factor = gcd(bit, int)
			if factor == 1:
			    if dec >= Decimal(0.95):
			        print(printingPress('A', dec, i, bit, int))
			    elif dec >= Decimal(0.9):
			        print(printingPress('B', dec, i, bit, int))
			    elif dec >= Decimal(0.85):
			        print(printingPress('C', dec, i, bit, int))
			    else:
			        print(printingPress('D', dec, i, bit, int))
		# e.g. 32*ln(2)/ln(85)=4.992674..., int = 5, dec=0.992674, gcd=1, A:
		# print "A: 0.992674 base85 32-bits x=5.0"

"""
C: 0.887817 base56 40-bits x=7.0
C: 0.878174 base56 400-bits x=69.0
D: 0.820311 base56 2560-bits x=441.0
C: 0.857664 base57 40-bits x=7.0
A: 0.972262 base57 64-bits x=11.0
C: 0.860400 base57 250-bits x=43.0
C: 0.883201 base57 2000-bits x=343.0
C: 0.890497 base57 2560-bits x=439.0
D: 0.828291 base58 40-bits x=7.0
B: 0.925266 base58 64-bits x=11.0
D: 0.804254 base58 1024-bits x=175.0
D: 0.829119 base58 4000-bits x=683.0
C: 0.879463 base59 64-bits x=11.0
A: 0.999162 base59 100-bits x=17.0
D: 0.834804 base60 64-bits x=11.0
B: 0.929381 base60 100-bits x=17.0
D: 0.808630 base60 625-bits x=106.0
C: 0.870092 base60 1600-bits x=271.0
C: 0.861310 base61 100-bits x=17.0
A: 0.978096 base61 160-bits x=27.0
B: 0.915933 base61 3125-bits x=527.0
A: 0.993597 base62 125-bits x=21.0
C: 0.871805 base62 160-bits x=27.0
A: 0.994887 base62 256-bits x=43.0
B: 0.912522 base63 125-bits x=21.0
D: 0.828846 base63 256-bits x=43.0
B: 0.920072 base63 400-bits x=67.0
D: 0.813059 base63 3125-bits x=523.0
D: 0.833333 base64 125-bits x=21.0
D: 0.833333 base64 3125-bits x=521.0
D: 0.838117 base65 800-bits x=133.0
C: 0.898894 base65 3125-bits x=519.0
B: 0.941617 base66 320-bits x=53.0
D: 0.803192 base66 1250-bits x=207.0
C: 0.885108 base66 2000-bits x=331.0
D: 0.826350 base66 2048-bits x=339.0
A: 0.970171 base67 200-bits x=33.0
D: 0.807277 base67 1024-bits x=169.0
C: 0.854410 base68 200-bits x=33.0
D: 0.835280 base68 1600-bits x=263.0
C: 0.858317 base68 4096-bits x=673.0
A: 0.954324 base69 128-bits x=21.0
B: 0.926414 base69 250-bits x=41.0
A: 0.964524 base69 800-bits x=131.0
C: 0.883356 base70 128-bits x=21.0
A: 0.969512 base70 625-bits x=102.0
D: 0.833561 base70 1280-bits x=209.0
D: 0.813864 base71 128-bits x=21.0
A: 0.966122 base72 80-bits x=13.0
A: 0.983180 base72 512-bits x=83.0
B: 0.924437 base73 80-bits x=13.0
A: 0.972167 base73 625-bits x=101.0
C: 0.865597 base73 2048-bits x=331.0
A: 0.977496 base73 3200-bits x=517.0
C: 0.883582 base74 80-bits x=13.0
D: 0.835817 base74 800-bits x=129.0
B: 0.909846 base74 1024-bits x=165.0
D: 0.843527 base75 80-bits x=13.0
C: 0.870537 base75 1600-bits x=257.0
A: 0.992859 base75 2560-bits x=411.0
D: 0.804246 base76 80-bits x=13.0
A: 0.973587 base76 256-bits x=41.0
A: 0.989285 base77 25-bits x=4.0
C: 0.850282 base77 256-bits x=41.0
D: 0.802259 base77 2048-bits x=327.0
B: 0.928539 base77 2500-bits x=399.0
A: 0.977470 base78 25-bits x=4.0
B: 0.911619 base78 320-bits x=51.0
B: 0.917179 base78 1024-bits x=163.0
C: 0.873510 base78 1250-bits x=199.0
A: 0.965874 base79 25-bits x=4.0
B: 0.907967 base79 800-bits x=127.0
C: 0.884396 base79 2048-bits x=325.0
A: 0.954490 base80 25-bits x=4.0
A: 0.987951 base80 512-bits x=81.0
C: 0.862244 base80 625-bits x=99.0
B: 0.943311 base81 25-bits x=4.0
C: 0.866219 base81 500-bits x=79.0
B: 0.948761 base81 640-bits x=101.0
B: 0.913870 base81 3125-bits x=493.0
B: 0.929754 base81 4000-bits x=631.0
B: 0.932331 base82 25-bits x=4.0
B: 0.917299 base82 400-bits x=63.0
B: 0.921544 base83 25-bits x=4.0
C: 0.861775 base83 1000-bits x=157.0
A: 0.978840 base83 1600-bits x=251.0
B: 0.910945 base84 25-bits x=4.0
C: 0.875577 base84 2000-bits x=313.0
C: 0.868089 base84 3125-bits x=489.0
B: 0.900527 base85 25-bits x=4.0
A: 0.992674 base85 32-bits x=5.0
C: 0.890285 base86 25-bits x=4.0
A: 0.979565 base86 32-bits x=5.0
B: 0.902848 base86 250-bits x=39.0
A: 0.978226 base86 1600-bits x=249.0
C: 0.880214 base87 25-bits x=4.0
A: 0.966674 base87 32-bits x=5.0
D: 0.802141 base87 250-bits x=39.0
B: 0.933568 base87 1024-bits x=159.0
D: 0.834251 base87 4000-bits x=621.0
C: 0.870310 base88 25-bits x=4.0
A: 0.953996 base88 32-bits x=5.0
A: 0.962477 base88 200-bits x=31.0
C: 0.860567 base89 25-bits x=4.0
B: 0.941525 base89 32-bits x=5.0
C: 0.884533 base89 200-bits x=31.0
D: 0.830504 base89 640-bits x=99.0
D: 0.845326 base89 2000-bits x=309.0
C: 0.850981 base90 25-bits x=4.0
B: 0.929255 base90 32-bits x=5.0
D: 0.807844 base90 200-bits x=31.0
C: 0.868082 base90 512-bits x=79.0
B: 0.925510 base90 3200-bits x=493.0
B: 0.944653 base90 4096-bits x=631.0
D: 0.841547 base91 25-bits x=4.0
B: 0.917180 base91 32-bits x=5.0
D: 0.830943 base91 500-bits x=77.0
B: 0.929509 base91 800-bits x=123.0
D: 0.832262 base92 25-bits x=4.0
B: 0.905296 base92 32-bits x=5.0
D: 0.806555 base92 625-bits x=96.0
A: 0.969460 base92 1024-bits x=157.0
D: 0.823122 base93 25-bits x=4.0
C: 0.893596 base93 32-bits x=5.0
B: 0.935958 base93 320-bits x=49.0
B: 0.924868 base93 1000-bits x=153.0
C: 0.890213 base93 3125-bits x=478.0
D: 0.814122 base94 25-bits x=4.0
C: 0.882076 base94 32-bits x=5.0
D: 0.820759 base94 320-bits x=49.0
B: 0.905710 base94 4096-bits x=625.0
D: 0.805259 base95 25-bits x=4.0
C: 0.870731 base95 32-bits x=5.0
A: 0.965849 base95 256-bits x=39.0
C: 0.884139 base95 400-bits x=61.0
D: 0.841387 base95 4000-bits x=609.0
"""
