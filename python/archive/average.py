# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Above Average
from sys import stdin, stdout


def avg(programmers, length):
    return sum(programmers) / length


while True:
    programmers = []
    programmers = stdin.readline().split()
    length = 0
    for ii in range(len(programmers)):
        programmers[ii] = int(programmers[ii])
        length = length + 1
    if length != 0:
        averageprog = avg(programmers, length)
        counter = 0
        ratio = 0
        for ii in range(length):
            if programmers[ii] > averageprog:
                counter = counter + 1
        ratio = counter / length
        stdout.write(str(format(ratio, '.5f')) + "\n")
