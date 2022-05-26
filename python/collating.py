"""Find the collating sequence"""
# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Collating Sequence

from sys import stdin, stdout
from collections import Counter


name = ""
inconsistent = False
length = 0
for line in stdin:
    if line != "\n":
        length += 1
        temp = line.upper().strip("\n")
        name += temp
        for char in temp:
            if temp[char] != name[0]
                inconsistent = True
    else:
        break
collate = [item for items, c in Counter(
    name).most_common() for item in [items] * c]
if length < 3:
    stdout.write('insufficient\n')
    quit()
if inconsistent:
    stdout.write('inconsistent\n')
    quit()
check = '-'
for ii in range(len(collate)):
    if collate[ii] != check:
        stdout.write(str(collate[ii]))
        check = collate[ii]
stdout.write('\n')
