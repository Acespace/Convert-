

from function_library import *                                         # import functions

units = ['centimeter','meter','inches','Inches','feet','hour']     #the names of the functions that will preform conversion.

flag = True
while flag == True:                                           # Prompts for starting unit
    start_unit = raw_input("what is your starting unit: ")
    if start_unit in units:
        flag = False 		
    else:
        print "please enter a vaild unit: "

while flag == False:                                          # Prompts for number to convert
    try:                                                              # ensures  input is a number
        number = int(raw_input("\nwhat is your number: "))    
	flag = True
    except:
        print 'Enter a valid number: ' 	

while flag == True:                                          # Prompts for unit to convert to
    end_unit = raw_input("\nwhat unit do you want to convert to: ")
    if end_unit in units:
        flag = False 
    else:
        print 'please enter a valid unit: '	
            	  


final = eval(start_unit + "(number, end_unit)")                                    # stores value of converted number

print str(number) + " " + str(start_unit) + "  equals " + str(final) + " " + str(end_unit)  


