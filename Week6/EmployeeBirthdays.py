#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution based on topics covered in class upto week 6

4. Employee birthdays
See the program employees_birthdays.py which reads the file
employee_birthday.txt. Update this program to use a Dictionary instead.
Hint: you can use csv.DictReader()
"""
import csv


with open('employee_birthday.txt', 'r') as csv_file:
    # user DictReader()
    csv_reader = csv.DictReader(csv_file)
    # using the method fieldnames to obtain headers
    headers = csv_reader.fieldnames
    # print headers formatted by unpacking the list
    print('Field Names: {}, {}, {}\n'.format(*headers))
    for line in csv_reader:
        # using the fieldnames as keys to the dict
        print('{} works in the {}, and was born in {}\n'.
              format(line['name'], line['department'], line['birthday month']))
