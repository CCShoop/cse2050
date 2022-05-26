# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Swimming Manatees
from sys import stdin, stdout
U = [0] * 25000
D = [0] * 25000
count = 0
sumU = 0
sumD = 0
minU = 50001
minD = 50001
line = " "
while line != "":
    line = stdin.readline()
    # Stops reading when empty line is entered
    if line.split():
        U[count], D[count] = line.split()
        U[count] = int(U[count])
        D[count] = int(D[count])
        count += 1
    else:
        break
for ii in range(count):
    sumU += U[ii]
    sumD += D[ii]
    if D[ii] < minD:
        minD = D[ii]
    if U[ii] < minU:
        minU = U[ii]
# If the upstream trip total is longer than the
# downstream, the fastest returning manatee is sent
# last in order to achieve the fastest time.
if sumU > sumD:
    time = sumU + minD
# If the return trip total is longer, it simply uses that value
# added to the minimum upstream time.
else:
    time = sumD + minU
stdout.write(str(time) + "\n")
