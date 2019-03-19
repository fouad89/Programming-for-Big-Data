#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution based on topics covered in class up to week 6

Write a program that asks the user for the name of a file.
The program should display only the first five lines of the file’s contents.
If the file contains less than five lines,
it should display the file’s entire contents..
"""


def read_file(filename):
    """
    args: filename: user input for file name
    returns: file
    """
    with open(filename, 'r') as f:
        file = f.read()

    return file


def display_head(file):
    """
    args: file- obtained from read_file() function
    displays file contents line by line"""
    lines_list = file.split('\n')
    if len(lines_list) > 5:
        for line in lines_list[:5]:
            print (line)
    else:
        for line in lines_list:
            print(line)


def main():
    file_name = input('What\'s your file name? ')
    file = read_file(file_name)
    display_head(file)

if __name__ == "__main__":
    main()
