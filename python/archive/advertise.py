# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: To Advertise, Or Not
from sys import stdin, stdout
# Takes number input as string, then converts to integer
count = int(stdin.readline())
ocount = count
# Variables for cost/profit
rec = [3]
r = 0
e = r
c = r
# Output
output = []
# For the number entered originally, this will split
# the new input among the three variables and run
# comparisons to decide which course of action to take
while count > 0:
    count = count - 1
    # Records input into list locations
    rec = stdin.readline().split()
    r = int(rec[0])
    e = int(rec[1])
    c = int(rec[2])
    # Decides based on advanced algorithm
    if r < e - c:
        output.append("advertise")
    elif r == e - c:
        output.append("does not matter")
    else:
        output.append("do not advertise")
# Prints final output
for jj in range(ocount):
    stdout.write(output[jj] + '\n')
