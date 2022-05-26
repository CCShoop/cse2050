"""Sharkovsky ordering on user input"""
# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Sharkovsky Ordering

from sys import stdin, stdout


output = []
for line in stdin:
    if line != '\n':
        nums = line.split()
        even = []
        odd = []
        for ii in range(len(nums)):
            nums[ii] = int(nums[ii])
            if nums[ii] % 2 == 0:
                even.append(nums[ii])
            else:
                odd.append(nums[ii])
        even.sort(key=int)
        odd.sort(key=int, reverse=True)
        sharkoved = ''
        for ii in range(len(even)):
            sharkoved += (str(even[ii]) + ' ')
        for ii in range(len(odd)):
            sharkoved += (str(odd[ii]) + ' ')
        output.append(sharkoved)
    else:
        break
for ii in range(len(output)):
    stdout.write(str(output[ii]) + '\n')
