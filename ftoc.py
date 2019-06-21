#f to c

import sys

def converter(num):
	try:
		floater = float(num)
		return str((floater - 32) * 5/9) + "ºC"
	except ValueError:
		return "Unknown value type. Bailing out 🚣🏽‍♂️"
	
print(converter(sys.argv[1]))