#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution based on topics covered in class up to week 5

Design a program that asks the user to enter a series of numbers.
The program should store the numbers in a list then display the following data:
• The lowest number in the list
• The highest number in the list
• The total of the numbers in the list
• The average of the numbers in the list
"""
NUMBERS = 20


def user_numbers():
    """
    will check the length of the list, and keep prompting until 20 nums entered
    return: final list after adding user input
    """
    user_num_list = []  # this list will contain the numbers
    # the user can input as many numbers in one line seperated by comma
    user_input = input('Enter your sequence of NUMBERS numbers and use comma:')
    # user_input will be of the form 1,2,3. using split to generate a list
    user_num_list = user_input.split(',')  # this will be a list of strings
    # each element will be a string, so we need to convert type
    for i in range(len(user_num_list)):
        # take every element of the list, and change it to a float
        user_num_list[i] = float(user_num_list[i])
    return user_num_list


def list_analysis(num_list):
    """
    Args: user number list
    rerturn min,max,total & average
    """
    # the required analysis
    minimum = min(num_list)
    maximum = max(num_list)
    total = sum(num_list)
    average = sum(num_list) / len(num_list)
    return [minimum, maximum, total, average]


def show_analysis(minimum, maximum, total, average):
    """
    Args: minimum,maximum,total,average
    displays the list analysis
    """
    print("The lowest number in the list is>> {0:.2f}".format(minimum))
    print("The highest number in the list is?? {0:.2f}".format(maximum))
    print("The total of your list is>> {0:.2f}".format(total))
    print("The average number of your list is>> {0:.2f}".format(average))


def main():
    num_list = user_numbers()
    while len(num_list) < NUMBERS:
        num_list += user_numbers()
        # this loop might enable user to input more than NUMBERS
        if len(num_list) > NUMBERS:
            del num_list[-(len(num_list) - NUMBERS):]
    # minimum, maximum, total, average =  list_analysis(num_list)
    print("You entered: {} numbers.\nThe list of numbers".
          format(len(num_list), num_list))
    show_analysis(*list_analysis(num_list))
if __name__ == "__main__":
    main()


