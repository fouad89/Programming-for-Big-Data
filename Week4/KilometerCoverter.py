"""
Solution is based on topics covered in class upto week 4

Write a program that asks the user to enter a distance in kilometers, then converts that distance to miles.
The conversion formula is as follows:
Miles=Kilometers×0.6214

"""
CONVERSION = 0.6214
def km_to_miles():
	"""
	Takes number of kilmoeters from user input
	returns the number of kilometers and its conversion to miles

	"""
	kilometers_input = float(input('How many kilometers? '))
	miles = kilometers_input*CONVERSION

	return kilometers_input,miles


def main():
	#since the function returns two values, we assign the two values to two variables
	kms,miles = km_to_miles() 
	#format the output 
	print('You entered {} kms. The number of miles is: {:0.2f}'.format(kms,miles))

if __name__ == '__main__':
	main()
