"""
Solution is based on topics covered in class up to week 4

Many financial experts advise that property owners should insure their homes or buildings for at least 80 percent of the amount
it would cost to replace the structure. Write a program that asks the user
to enter the replacement cost of a building,then displays the minimum amount of insurance he or she should buy for the property.
"""
INSURANCE_PCT = 0.80

def min_insurance_amount(cost):
	"""
	Args: takes the user input for the replacement cost
	returns: mimimum amount of insurance
	"""

	minimum_amount = cost * INSURANCE_PCT

	return minimum_amount

def main():

	replacement_cost = float(input('What\'s your replacement cost? '))

	print(min_insurance_amount(replacement_cost))


if __name__ == '__main__':
	main()
