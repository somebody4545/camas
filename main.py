# enterToClose asks user to press enter to shut down the program. 
def enterToClose():
	input('Press Enter to continue')
	quit()
	



# Asks user for side length of the hexagon and tries to turn it into an integer

try:
	sideLen = int(input('Please input any integer of 1 to 10 to draw a hexagon\n'))

# if the string can't be converted into an integer or another error with input occurs then exit program
except:
	print('Error: Invalid input. Exiting program')
	enterToClose()

# If the string can be converted into an integer, then check if it is not an integer from 1-10. If it is, give an error and close program, if not, then make the hexagon.
else:
	if sideLen > 50 or sideLen < 1:
		print('Error: Invalid input. Exiting program')
		enterToClose()
	else:

		print((" " * sideLen) + ("_" * sideLen))

# Opening the hexagon (double backslash to avoid escaping)
		for x in range(sideLen):
			y = sideLen - x - 1
			z = sideLen + x*2
			print((' ' * y) + '/' + (' ' * z) + '\\')

# Closing the hexagon
		for x in range(sideLen-1):
			a = (sideLen - x)*2 + sideLen - 3
			print((' ' * x) + '\ ' + (' ' * a) + '/')

# Bottom line of the hexagon (double backslash to avoid escaping)
		x = sideLen - 1
		print((' ' * x) + '\\' + ('_' * sideLen) + '/')

#close script
		enterToClose()


	


