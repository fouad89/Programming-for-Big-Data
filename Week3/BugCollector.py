'''
Solution - Based on topics covered in class so far

Problem

A bug collector collects bugs every day for five days.
Write a program that keeps a running total of the number of bugs collected during the five days.
The loop should ask for the number of bugs collected for each day, and when the loop is finished, 
the program should display the total number of bugs collected. 


'''

#What the program does
print('This program keeps track of number of bugs collected for five days with an input each day\
at the end of the 5 days the program displays total # of bugs collected')

number_of_bugs = 0 #initialize number of bugs collected
days = 1 #starts from one, it will be incremented until 5 days completed
while days <= 5:
	user_input = int(input('What is the number of bugs collected in day {}? '.format(days)))
	number_of_bugs += user_input #adding num of bugs collected to number of previously collected
	days+=1 #increment with a new day

print('You have collected: {:d} bugs'.format(number_of_bugs))

