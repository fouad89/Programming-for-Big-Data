#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution based on topics covered up to week 5

Design a program that generates a seven-digit lottery number.
The program should
generate seven random numbers, each in the range of 0 through 9,
and assign each numberto a list element. Then write another loop
that displays the contents of the list
"""
import random
LENGTH = 7  # length of list
MINIMUM = 0  # random integers starting point
MAXIMUM = 9  # random integers ending point
lotto_sequence_number = ['First','Second','Third','Fourth','Fifth','Sixth','Seventh'] 

def random_generator():
    """The function will generate a random number"""
    return random.randint(MINIMUM, MAXIMUM)


def list_random():
    """
    call random_generator to create a list of 7 random numbers
    """
    lottery_numbers = []  # this list will contain the list of
    for i in range(LENGTH):
        lottery_numbers.append(random_generator())
    return lottery_numbers


def main():
    final_list = list_random()
    # print out each element on it's own
    for i in range(LENGTH):
        # formatting output
        print("{} Number is>> {}".format(lotto_sequence_number[i], final_list[i]))
if __name__ == "__main__":
    main()
