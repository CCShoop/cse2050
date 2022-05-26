# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: knitting
from sys import stdin, stdout
all_totals = []
counter = 0
nmk = [3]
n = 1
m = 1
k = 1
while n != 0 and m != 0 and k != 0:
    counter = counter + 1
    # N (number of stitches in first row), M (total number of rows),
    # and K (number of rows in repeating pattern) are set as the first line of input
    nmk = stdin.readline().split()
    n = int(nmk[0])
    m = int(nmk[1])
    k = int(nmk[2])
    # Quits the program if the input is out of bounds
    if n < 0 or n > 100:
        quit()
    if m < 0 or m > 1000:
        quit()
    if k < 0 or k > 100:
        quit()
    # If the input does not indicate end of use, the program
    # calculates the total
    if n != 0 and m != 0 and k != 0:
        # Total represents the sum of the stitches
        total = n
        # Count keeps track of the repeating pattern
        count = 0
        # Previous value set to first count
        previous = n
        # Creates list to represent pattern
        pattern = []
        pattern = stdin.readline().split()
        # Declares pattern list
        for ii in range(k):
            pattern[ii] = int(pattern[ii])
            # The program will quit if any number in the
            # pattern varies the count by 100+
            if pattern[ii] < -100 or pattern[ii] > 100:
                quit()
        # Runs through and adds each new row count to total
        for ii in range(m - 1):
            previous = previous + pattern[count]
            total = total + previous
            count = count + 1
            # Resets count to restart pattern
            if count == k:
                count = 0
        all_totals.append(total)
    # Prints all totals at end of program
    elif n == 0 and m == 0 and k == 0:
        jj = 0
        while jj < counter - 1:
            stdout.write(str(all_totals[jj]) + '\n')
            jj = jj + 1
