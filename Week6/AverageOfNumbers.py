#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution based on topics covered in class upto week 6

3. Average of Numbers
Assume a file containing a series of integers is named numbers.txt
and exists on the computer’s disk. Write a program that calculates
the average of all the numbers stored in the file.
** assuming the file contains one number per line

"""


def read_file(file_name):
    """
    args: filename: user input for file name
    returns: file
    """
    with open(file_name, 'r') as f:
        content = f.read()

    return content


def file_to_list(content):
    """
    args: file reutrned from previous function read_file()
    returns: list of numbers from the file"""
    # removing the last element as it will be an empty string
    numbers_list_str = content.split('\n')[:-1]
    # initiate an empty list that will containt float format
    final_numbers_list = []
    for num in numbers_list_str:
        # this loop will convert each element into float
        final_numbers_list.append(float(num))
    return final_numbers_list


def calculate_average(num_list):
    """
    args: numbers list of floats
    returns: average of that list"""
    length_num_list = len(num_list)
    average = sum(num_list) / length_num_list
    return average


def main():
    file_name = input('File name? ')
    content = read_file(file_name)
    final_list = file_to_list(content)
    print('Average is ',calculate_average(final_list))

if __name__ == "__main__":
    main()
    