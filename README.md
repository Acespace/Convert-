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


