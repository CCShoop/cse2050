# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Manatee Vocalization
from sys import stdin, stdout
input = int(stdin.readline())
if input < 1:
    stdout.write("Error\n")
    quit()
a = 2
size = 0
test = ''
while size < input:
    a += 1
    a_2 = a
    b = 0
    size = 0
    while a_2 >= 3:
        size += 2 ** b * a_2
        a_2 -= 1
        b += 1
while test != 'k' and test != 'i':
    left = (size - a) / 2 + 1
    right = left + a - 1
    if input == left:
        test = 'k'
    elif input > left and input <= right:
        test = 'i'
    else:
        test = 0
    if (test == 0):
        if input > (size - a) / 2 + a:
            input -= (size - a) / 2 + a
        a -= 1
        a_2 = a
        b = 0
        size = 0
        while a_2 >= 3:
            size += 2 ** b * a_2
            a_2 -= 1
            b += 1
    else:
        stdout.write(test + '\n')
