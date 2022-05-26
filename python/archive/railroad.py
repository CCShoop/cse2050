# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Working on the Railroad
cross = -1
ysplit = -1
while cross < 0 or ysplit < 0:
    cross, ysplit = input(
        "Enter the number of x and y-shaped switches: ").split()
    cross = int(cross)
    ysplit = int(ysplit)
if ysplit % 2 == 0:
    print("possible")
else:
    print("impossible")