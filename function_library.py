

def feet(num, endU):
	
	if endU == "inches" or "INCH" or "inch":
		
		num1 = num
		num *= 12

		return num 

	elif endU == "centimeters" or "CENTIMETERS":
		
		num1 = num
		num /= 0.0328084

		return num 

	elif endU == "Meters" or "meters" or "meter":
		num1 = num
		num /= 3.28084
	
		return num


	else:
		pass
	





def inches(num, endU):
	
	if endU == "centimeters" or "Centimeters":
		
		num1 = num
		num *= 2.54

		return num

	elif endU == "feet" or "Feet" or "FEET":
		
		num1 = num
		num = num / 12.0

		return num

	elif endU == "meters" or "meter":
		num1 = num
		num = num / 39.3701
	
		return num


	else:
		pass

	


def centimeter(num, endU):
	
	if endU == "INch" or "inches" or "inch":
		
		num1 = num
		num = num * 0.393701

		return num

	elif endU == "feet" or "FEET" or "feet":
		
		num1 = num
		num = num * 0.0328084

		return num 

	elif endU == "meters" or "METER" or "meter":

		num1 = num
		num = num / 100
		return num


	else:
		pass
	

def meter(num,endU):
		
	if endU == "centimeters" or "centi" or "Centimeters" or "CENTIMETERS":
		
		num1 = num
		num *= 100

		return num

	elif endU == "feet" or "Feet" or "FEET":
		
		num1 = num
		num *= 3.28084

		print num1, "meter equals", num, " feet"

	elif endU == "inches" or " inche":
		num1 = num
		num *= 39.3701
	
		print num1, " meter equals", num, "inches"


	else:
		pass


