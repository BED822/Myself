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

for bit in list:
    for i in range(56, 96):
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
A: 0.989285 base77 25-bits x=4.0
A: 0.992674 base85 32-bits x=5.0
C: 0.887817 base56 40-bits x=7.0
A: 0.972262 base57 64-bits x=11.0
A: 0.966122 base72 80-bits x=13.0
A: 0.999162 base59 100-bits x=17.0
A: 0.993597 base62 125-bits x=21.0
A: 0.954324 base69 128-bits x=21.0
A: 0.978096 base61 160-bits x=27.0
A: 0.970171 base67 200-bits x=33.0
A: 0.962477 base88 200-bits x=31.0
C: 0.860400 base57 250-bits x=43.0
B: 0.926414 base69 250-bits x=41.0
B: 0.902848 base86 250-bits x=39.0
A: 0.994887 base62 256-bits x=43.0
A: 0.973587 base76 256-bits x=41.0
A: 0.965849 base95 256-bits x=39.0

B: 0.941617 base66 320-bits x=53.0
B: 0.911619 base78 320-bits x=51.0
B: 0.935958 base93 320-bits x=49.0
D: 0.820759 base94 320-bits x=49.0
C: 0.878174 base56 400-bits x=69.0
B: 0.920072 base63 400-bits x=67.0
B: 0.917299 base82 400-bits x=63.0
C: 0.884139 base95 400-bits x=61.0
C: 0.866219 base81 500-bits x=79.0
D: 0.830943 base91 500-bits x=77.0
A: 0.983180 base72 512-bits x=83.0
A: 0.987951 base80 512-bits x=81.0
C: 0.868082 base90 512-bits x=79.0
D: 0.808630 base60 625-bits x=106.0
A: 0.969512 base70 625-bits x=102.0
A: 0.972167 base73 625-bits x=101.0
C: 0.862244 base80 625-bits x=99.0
D: 0.806555 base92 625-bits x=96.0
B: 0.948761 base81 640-bits x=101.0
D: 0.830504 base89 640-bits x=99.0
D: 0.838117 base65 800-bits x=133.0
A: 0.964524 base69 800-bits x=131.0
D: 0.835817 base74 800-bits x=129.0
B: 0.907967 base79 800-bits x=127.0
B: 0.929509 base91 800-bits x=123.0
C: 0.861775 base83 1000-bits x=157.0
B: 0.924868 base93 1000-bits x=153.0
D: 0.804254 base58 1024-bits x=175.0
D: 0.807277 base67 1024-bits x=169.0
B: 0.909846 base74 1024-bits x=165.0
B: 0.917179 base78 1024-bits x=163.0
B: 0.933568 base87 1024-bits x=159.0
A: 0.969460 base92 1024-bits x=157.0
D: 0.803192 base66 1250-bits x=207.0
C: 0.873510 base78 1250-bits x=199.0
D: 0.833561 base70 1280-bits x=209.0
C: 0.870092 base60 1600-bits x=271.0
D: 0.835280 base68 1600-bits x=263.0
C: 0.870537 base75 1600-bits x=257.0
A: 0.978840 base83 1600-bits x=251.0
A: 0.978226 base86 1600-bits x=249.0
C: 0.883201 base57 2000-bits x=343.0
C: 0.885108 base66 2000-bits x=331.0
C: 0.875577 base84 2000-bits x=313.0
D: 0.845326 base89 2000-bits x=309.0
D: 0.826350 base66 2048-bits x=339.0
C: 0.865597 base73 2048-bits x=331.0
D: 0.802259 base77 2048-bits x=327.0
C: 0.884396 base79 2048-bits x=325.0
B: 0.928539 base77 2500-bits x=399.0
D: 0.820311 base56 2560-bits x=441.0
C: 0.890497 base57 2560-bits x=439.0
A: 0.992859 base75 2560-bits x=411.0
B: 0.915933 base61 3125-bits x=527.0
D: 0.813059 base63 3125-bits x=523.0
D: 0.833333 base64 3125-bits x=521.0
C: 0.898894 base65 3125-bits x=519.0
B: 0.913870 base81 3125-bits x=493.0
C: 0.868089 base84 3125-bits x=489.0
C: 0.890213 base93 3125-bits x=478.0
A: 0.977496 base73 3200-bits x=517.0
B: 0.925510 base90 3200-bits x=493.0
D: 0.829119 base58 4000-bits x=683.0
B: 0.929754 base81 4000-bits x=631.0
D: 0.834251 base87 4000-bits x=621.0
D: 0.841387 base95 4000-bits x=609.0
C: 0.858317 base68 4096-bits x=673.0
B: 0.944653 base90 4096-bits x=631.0
B: 0.905710 base94 4096-bits x=625.0
"""
