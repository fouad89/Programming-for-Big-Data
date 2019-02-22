'''
Solution based on topics covered in class only. This could be done in many more effecient ways.

Write a program that prompts the user to enter a number within the range of 1 through 10. 
The program should display the Roman numeral version of that number.
If the number is outside the range of 1 through 10, the program should display an error message.
The following table shows the Roman numerals for the numbers 1 through 10: 
I, II, III, IV, V, VI, VII, VIII, IX, X

'''

#displaying what the program is about

print('Displaying Roman numerals for numbers 1-10\n')

#specify user input to integers between 1-10 only
user_number = int(input('Enter a number between 1-10: '))

#check if user number is between 1 & 10

#range upto 11 because remember(first number inclusive, last number exclusive)
if user_number not in range(1,11):
	#the program ends here if user inputs any number outside of the range
	print('Input is not in range 1-10,Try again')
	 
	
#below elif statements go through the conditions and prints out the user input as well as the equivelant roman numeral
elif user_number == 1:
	print('You entered {}, your Roman numeral is: {}'.format(user_number,'I'))
elif user_number == 2:
	print('You entered {}, your Roman numeral is: {}'.format(user_number,'II'))
elif user_number == 3:
	print('You entered {}, your Roman numeral is: {}'.format(user_number,'III'))
elif user_number == 4:
	print('You entered {}, your Roman numeral is: {}'.format(user_number,'IV'))
elif user_number == 5:
	print('You entered {}, your Roman numeral is: {}'.format(user_number,'V'))
elif user_number == 6:
	print('You entered {}, your Roman numeral is: {}'.format(user_number,'VI'))
elif user_number == 7:
	print('You entered {}, your Roman numeral is: {}'.format(user_number,'VII'))
elif user_number == 8:
	print('You entered {}, your Roman numeral is: {}'.format(user_number,'VIII'))
elif user_number == 9:
	print('You entered {}, your Roman numeral is: {}'.format(user_number,'IX'))
elif user_number == 10:
	print('You entered {}, your Roman numeral is: {}'.format(user_number,'X'))
