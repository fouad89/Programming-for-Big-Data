#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution based on topics covered in class up to week 6
1. File Display
Assume a file containing a series of integers is named numbers.txt and exists
on the computer’s disk. Write a program that displays all
of the numbers in the file.

"""


def read_file(filename):
	"""
	args:filename: input from user
	returns: file contents"""
    with open(filename, 'r') as f:
        numbers = f.read()
    return numbers


def display_file(numbers):
	"""
	args: takes file content
	returns"""
    return(numbers)[:5]


def main():
    filename = input('What\'s your file name? ')
    numbers = read_file(filename)
    print(display_file(numbers))

if __name__ == "__main__":
    main()