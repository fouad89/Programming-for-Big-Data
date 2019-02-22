'''
Solution - Based on topics covered in class so far

Problem

Write a program with a loop that asks the user to enter a series of positive numbers.
The user should enter a negative number to signal the end of the series.
After all the positive numbers have been entered, the program should display their sum. 


'''
####What the program does
print('The program will be running so long as the user keep entering positive numbers\
the program stops once a negative value is entered and the sum is displayed')

total_sum = 0 #initialize the total
user_input = float(input('Enter a positive number>> '))
num_of_inputs = 0 #to keep track of how many numbers entered

while user_input>=0:
	total_sum +=user_input
	num_of_inputs+=1
	#new input required to add to the previous
	print('Enter negative number when you want the program to stop! ')
	user_input = float(int(input('Enter a positive number>> ')))

print('You entered {:d} numbers(s).\nSum of your numbers>> {:.2f}'.format(num_of_inputs,total_sum))