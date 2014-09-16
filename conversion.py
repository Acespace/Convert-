
'''

print " Ready to convert inchs to centimeters or vise versa?"

ans = input("type 1 if you want to convert from inches to centimeters. \n Type 0 if you want to convert from centimeters to inches")



'''

def meter():
	
	print "What would you like to convert your meters to?\n"
	
	ans = input(" Enter '1' to go to centimeters, Enter '2' for feet, Enter '3' for inches:  ")
	
	num= input("\n enter your number of meters: ")
	
	if ans == 1:
		
		num1 = num
		num *= 100

		print num1, "meter equals", num, "centimeters"

	elif ans == 2:
		
		num1 = num
		num *= 3.28084

		print num1, "meter equals", num, " feet"

	elif ans == 3:
		num1 = num
		num *= 39.3701
	
		print num1, " meter equals", num, "inches"


	else:
		pass




def feet():

	print "What would you like to convert your feet to?\n"
	ans = input(" Enter '1' to go to inches, Enter '2' for centimeters, Enter '3' for meters:  ")
	num= input("\n enter your number of centimeters: ")
	
	if ans == 1:
		
		num1 = num
		num *= 12

		print num1, "feet equals", num, "inches"

	elif ans == 2:
		
		num1 = num
		num /= 0.0328084

		print num1, "feet equals", num, " centimeters"

	elif ans == 3:
		num1 = num
		num = num / 3.28084
	
		print num1, " feet equals", num, "meters"


	else:
		pass
	



def centi():

	print "What would you like to convert your centimeters to\n"
	ans = input(" Enter '1' to go to inches, Enter '2' for feet, Enter '3' for meters:  ")
	num= input("\n enter your number of centimeters: ")
	
	if ans == 1:
		
		num1 = num
		num * 0.393701

		print num1, "centimeters equals", num, "inches"

	elif ans == 2:
		
		num1 = num
		num = num * 0.0328084

		print num1, "centimeters equals", num, " feet"

	elif ans == 3:
		num1 = num
		num = num / 100
	
		print num1, " centimeters equals", num, "meters"


	else:
		pass
	


def inches():
	
	print "What would you like to convert your inches to\n"
	
	ans = input(" Enter '1' to go to centimeters, Enter '2' for feet, Enter '3' for meters:  ")
	
	num= input("\n enter your number of inches: ")
	if ans == 1:
		
		num1 = num
		num *= 2.54

		print num1, "inches equals", num, "centimeters"

	elif ans == 2:
		
		num1 = num
		num = num / 12.0

		print num1, "inches equals", num, " feet"

	elif ans == 3:
		num1 = num
		num = num / 39.3701
	
		print num1, " inches equals", num, "meters"


	else:
		pass




print "Welcome to Conv3rsionbo0k!"


print "what is your starting unit?"

choice = input("\nEnter '1' for inches, Enter '2' for centimeters,\n Enter '3' for feet, Enter '4' for meters: ")


if choice == 1:
	inches()


elif choice == 2:
	centi()


elif choice == 3:
	feet()

elif choice == 4:
	meter()


#else:
#	Print "Please enter a valid number"



