# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Tri-Color Sort
from sys import stdin, stdout


men = []
length = -1
for ii in range(3):
    men = stdin.readline().split()
    for jj in range(len(men)):
        men[jj] = int(men[jj])
        length = length + 1
        if men[jj] % 3 == 0:
            stdout.write(str(men[jj]) + " ")
    for jj in range(len(men)):
        if men[jj] % 3 == 1:
            stdout.write(str(men[jj]) + " ")
    for jj in range(len(men)):
        if men[jj] % 3 == 2:
            stdout.write(str(men[jj]) + " ")
    stdout.write("\n")
