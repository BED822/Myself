from math import log10
from math import modf
from fractions import gcd
from decimal import *

################################################################################

total_list = [
	original_list_1, medium_list_1, long_list_1, extended_list_1,
	original_list_3, medium_list_3, long_list_3, extended_list_3,
	original_list_27, medium_list_27, long_list_27, extended_list_27
	]
	
# list of 2^m * 5^n
# excludes 2, 4, 5, 8, 10, 16, 20
original_list_1 = [
	25, 32, 40, 50, 64, 80, 100, 
	125, 128, 160, 200, 250, 256]
medium_list_1 = [
	320, 400, 500, 512, 625, 640, 800, 1000, 
	1024, 1250, 1280, 1600, 2000, 2048,
	2500, 2560, 3125, 3200, 4000, 4096]
long_list_1 = [
	5000, 5120, 6250, 6400, 8000, 8192, 10000, 
	10240, 12500, 12800, 15625, 16000, 16384]
extended_list_1 = [
	20000, 20480, 25000, 25600, 31250, 32000, 32768, 
	40000, 40960, 50000, 51200, 62500, 64000, 65536]
# list of 3^l * (2^m * 5^n) for 1 and 2
# excludes 3, 6, 9, 12, 15, 18, 24
original_list_3 = [
	30, 36, 45, 48, 60, 72, 75, 90, 96, 
	120, 144, 150, 180, 192, 225
	]
medium_list_3 = [
	240, 288, 300, 360, 384, 480, 375, 450, 576, 600, 
	720, 750, 768, 900, 960, 1125, 1152, 1200, 1440, 
	1500, 1536, 1800, 1875, 1920, 2250, 2304, 2400, 
	2880, 3000, 3072, 3600, 3750, 3840
	]
long_list_3 = [
	4500, 4608, 4800, 5625, 5760, 6000, 6144, 7200, 
	7500, 7680, 9000, 9216, 9375, 9600, 11250, 
	11520, 12000, 12288, 14400, 15000, 15360
	]
extended_list_3 = [
	18000, 18432, 18750, 19200, 22500, 23040, 24000, 
	24576, 28125, 28800, 30000, 30720, 36000, 36864, 
	37500, 38400, 45000, 46080, 46875, 48000, 49152, 
	56250, 57600, 60000, 61440
	]
#list of 3^l * (2^m * 5^n) for 3, 4, 5
original_list_27 = [
	27, 54, 81, 108, 135, 162, 216, 256
	]
medium_list_27 = [
	270, 324, 405, 432, 486, 540, 648, 675, 810, 864, 
	972, 1080, 1215, 1296, 1350, 1620, 1728, 1944, 2025, 
	2160, 2430, 2592, 2700, 3240, 3375, 3456, 3888, 4050
	]
long_list_27 = [
	4320, 4860, 5184, 5400, 6075, 6480, 6750, 6912, 
	7776, 8100, 8640, 9720, 10125, 10368, 10800, 
	12150, 12960, 13500, 13824, 15552, 16200
	]
extended_list_27 = [
	16875, 17280, 19440, 20250, 20736, 21600, 24300, 
	25920, 27000, 27648, 30375, 31104, 32400, 33750, 
	34560, 38880, 40500, 41472, 43200, 48600, 50625, 
	51840, 54000, 55296, 60750, 62208, 64800
	]

################################################################################

def printingPress(key, dec, i, bit, int):
	if i == 56:
		return key + ": " + str(dec) + " base" + str(i) + " " + str(bit) + "-bits" + " x=" + str(int) + " <=="
	else:
		return key + ": " + str(dec) + " base" + str(i) + " " + str(bit) + "-bits" + " x=" + str(int)

def show_list(list):
	for bit in list:
		check_bits(bit)

def check_bits(bit):
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

################################################################################

def bitList2(x, y):
	output = []
	assert isinstance(x, int) and isinstance(y, int), "not integer"
	assert x>0 and y>0, "number is not positive"
	assert x < y, "the input should be switched"
	if x == 1:
		output.append(2)
	else:
		output.append(4*(2**(x-2)))
	for i in range(x+1, y+1):
		output.append(3*(2**(i-2)))
		output.append(4*(2**(i-2)))
	return output

def bitList3(x, y):
	output = []
	assert isinstance(x, int) and isinstance(y, int), "not integer"
	assert x>0 and y>0, "number is not positive"
	assert x < y, "the input should be switched"
	if x == 1:
		output.append(2)
		output.append(3)
		output.append(4)
	elif x == 2:
		output.append(4)
	else:
		output.append(8*(2**(x-3)))
	if x != 1:
		for i in range(x+1, y+1):
			output.append(5*(2**(i-3)))
			output.append(6*(2**(i-3)))
			output.append(7*(2**(i-3)))
			output.append(8*(2**(i-3)))
	else:
		for i in range(3, y+1):
			output.append(5*(2**(i-3)))
			output.append(6*(2**(i-3)))
			output.append(7*(2**(i-3)))
		output.append(8*(2**(i-3)))
	return output
