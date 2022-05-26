# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Treasure Hunt
from sys import stdin, stdout


def find_max(z, length):
    ans = 0
    return ans


def build_matrix(line):
    x = []
    a, b, c = line.split()
    x.append(int(a))
    x.append(int(b))
    x.append(int(c))
    return x


z = []
length = 0
while True:
    line = stdin.readline()
    if line.split():
        z.append(build_matrix(line))
        length += 1
    else:
        break
print(z)
answer = find_max(z, length)
stdout.write(str(answer) + '\n')
