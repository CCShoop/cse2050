"""This program finds and returns the Z-Score of the given input."""
# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Z-Score
from sys import stdin, stdout
from decimal import Decimal
from statistics import pstdev, mean
for line in stdin:
    list = [Decimal(num) for num in line.replace(",", " ").split()]
    if len(list) > 0:
        # Uses statistics to find average and standard deviation
        avg = mean(list)
        dev = pstdev(list)
        for ii in range(len(list)):
            # Calculates each z-score individually and prints it
            z = (list[ii] - avg) / dev
            z = round(z, 2)
            if ii == len(list) - 1:
                stdout.write(f"{z}\n")
            else:
                stdout.write(f"{z}, ")