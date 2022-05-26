"""Calculates lost votes and efficiency gap"""
# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Gerrymandering

from sys import stdin, stdout


d, p = stdin.readline().split()
p = int(p)
d = int(d)
votes = [[0] * 2 for ii in range(p)]
v = 0
for jj in range(d):
    count, a, b = stdin.readline().split()
    count = int(count) - 1
    a = int(a)
    b = int(b)
    votes[count][0] += a
    votes[count][1] += b
    v += a
    v += b
w_a = 0
w_b = 0
for kk in range(p):
    vote_count = int((votes[kk][0] + votes[kk][1])/2) + 1
    if votes[kk][0] > votes[kk][1]:
        elected = 'A'
        lost_a = int(votes[kk][0]) - vote_count
        lost_b = int(votes[kk][1])
    else:
        elected = 'B'
        lost_a = int(votes[kk][0])
        lost_b = int(votes[kk][1]) - vote_count
    w_a += lost_a
    w_b += lost_b
    stdout.write(str(elected) + ' ' + str(lost_a) + ' ' + str(lost_b) + '\n')
E = abs((w_a - w_b)/v)
output = '{:0.10f}'.format(E)
stdout.write(output + '\n')
