#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution based on topics covered in class up to week 6

4. Contact Manager
Create a program that a user can use to manage the primary email address and 
phone number for a contact. The contacts should read from the provided
contacts.csv and save to it also. Also display all the contacts to the
screen and allow a contact to be added.


contacts.csv
['Guido van Rossum', 'guido@python.org', '+31 0474 33 88 26']
['Eric Idle', 'eric@ericidle.com', '+44 20 7946 0958']
['Mike Murach', 'mike@murach.com', '559-123-4567']
"""
import csv


def read_contacts(file):
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            print(line)


def write_contacts(file, new_line):
    with open(file, 'a') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(new_line)


def new_line():
    line_content_list = []
    headers = ['Name','Email','Phone']
    for i in range(3):
        line_content = input('{} value of the new line>> '.format(headers[i]))
        line_content_list.append(line_content)
    return line_content_list


def main():
    file = input('what\'s your csv file name? ')
    new_line_input = new_line()
    write_contacts(file, new_line_input)
    read_contacts(file)


if __name__ == "__main__":
    main()
