# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Modulas 10 Checksum Formula
from sys import stdin, stdout


def valid_num(input):
    new = int(input)
    digits = [0]*(len(input))
    length = len(input) - 1
    value = 10
    while length >= 0:
        digits[length] = new % value - new % (value / 10)
        while digits[length] >= 10:
            digits[length] = digits[length] / 10
        value = value * 10
        length = length - 1
    length = len(input) - 1
    check = 0
    # Adds last and every other digit from last to check
    while length >= 0:
        check = check + digits[length]
        length = length - 2
    length = len(input) - 2
    new = 0
    # Adds alternate digits * 2 (and possibly minus 9) to check
    while length >= 0:
        new = digits[length] * 2
        if new > 9:
            new = new - 9
        check = check + new
        length = length - 2
    # Returns true/false if input is valid
    if check % 10 == 0:
        return True
    else:
        return False


counter = 0
while True:
    line = stdin.readline()
    if len(line) > 100:
        quit()
    if valid_num(line):
        stdout.write("True\n")
    else:
        stdout.write("False\n")
