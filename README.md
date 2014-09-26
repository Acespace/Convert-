Convert-
========

A simple conversion table

There are three parts of this project.

Model(s), Control, and Veiw.

The Model(s) for this project are the files containing functions to preform the conversions.

The Control will manage the importing, calling, and execution of the application.

My goal is to make a UI using Tkinter; however for now, the Veiw will just run from commandline.


DESIGN:

function template:


def meter(num,endU):                       num  is the number to convert and endU is the ending unit
		
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



