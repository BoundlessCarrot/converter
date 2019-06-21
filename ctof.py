#C to F
import sys

def converter(num):
	try:
		floater = float(num)
		return str((floater * 9/5) + 32) + "ºF"
	except ValueError:
		return "Unknown value type. Bailing out 🚣🏽‍♂️"
	
print(converter(sys.argv[1]))