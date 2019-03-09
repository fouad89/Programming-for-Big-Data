#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution based on topics covered up to week 5

Design a program that lets the user enter the total rainfall for each of 12
months into a list.The program should calculate and display the total
rainfall for the year, the average monthly
rainfall, the months with the highest and lowest amounts.
"""
NUM_OF_MONTHS = 12


def rainfall_amount_input():
    """This function will ask the user to input the amount of rainfull
    for each of the 12 months
    """
    user_input = float(input('What\'s the amount of rain fall? '))
    return user_input


def year_total(rainfall):
    """
    args: annual list of rainfall
    return: total amount of rain for the 12 months
    """
    return sum(rainfall)


def average_monthly(rainfall):
    """
    args: annual list of rainfall
    return: average monthly
    """
    return sum(rainfall)/NUM_OF_MONTHS


def min_max(rainfall):
    """
    args: annual list of rainfall
    returns: two values, first is minimum, second is maximum
    """
    return min(rainfall), max(rainfall)


def main():
    annual_rainfall = []  # initiate the list that will contain 12 month values
    for month in range(1, NUM_OF_MONTHS+1):
        monthly_value = rainfall_amount_input()
        annual_rainfall.append(monthly_value)
    total_rainfall = year_total(annual_rainfall)
    average = average_monthly(annual_rainfall)
    minimum, maximum = min_max(annual_rainfall)
    print("Total rain for the year {}".format(total_rainfall))
    print("Monthly average: {:.2f}".format(average))
    print("Month {} had the minimum of {}".
          format(annual_rainfall.index(minimum)+1, minimum))
    print("Month {} had the maximum of {}".
          format(annual_rainfall.index(maximum)+1, maximum))
if __name__ == "__main__":
    main()
