'''
This code will solve the first problem in Week2 Lab

Problem 1. Sales Prediction
 A company has determined that its annual profit is typically 23 percent of total sales. Write a program that asks the user to enter 
the projected amount of total sales, then displays the profit that will be made from that amount.
Hint: Use the value 0.23 to represent 23 percent.


'''
#requesting user input for projected total sales
total_sales = float(input('What is the project amount of Project Total Sales? '))

#percentage of profit
annual_profit_pct = 0.23 

#calculating total proft
total_profit = total_sales * annual_profit_pct

#program output
print('Total Projected Profit is: {:0.2f}'.format(total_profit))