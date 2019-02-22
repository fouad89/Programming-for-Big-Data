'''
Solution - Based on topics covered in class so far

Problem

Write a program that asks the user to enter the amount that he or she has budgeted for a month.
A loop should then prompt the user to enter each of his or her expenses for the month and keep a running total. 
When the loop finishes, the program should display the amount that the user is over or under budget. 

'''

###What the program does
print('###############################\nThis program keeps track of expenses and displays the amount the has left of their budget\
User will be prompted if they have a new expend(can answer with yes or no) if yes, they will enter the amount\n\
###############################')


#prompt for total budget
user_budget = float(input('What\'s your budget for the month? >> ')) 
new_expense = input('Do you have a new expense? Y/n >> ')#is there a new expense to add?

total_expense = 0
num_of_expenses = 0 #this will keep track of how many expenses entered

while True:

	if new_expense.lower() =='n' or new_expense.lower()=='no':
		#if the user answer n or no for new expense, the program will stop and display amount left
		print('\n You have {:.2f} left of your budget.\n You entered>> {} expense(s)\n Total Spending>> {}'.
			format(user_budget,num_of_expenses,total_expense))
		break
	elif new_expense.lower() == 'y' or new_expense.lower()=='yes': #to incapsulate the ueser input.
		expense = float(input('How much is it? >> '))
		user_budget-=expense #budget - new expense
		num_of_expenses+=1 #increment number of expenses
		total_expense+=expense
		new_expense = input('Do you have a new expense? Y/n? >> ')









