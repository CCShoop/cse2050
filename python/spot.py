"""Depth First Search of input grid"""
# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Spot On

from sys import stdin, stdout


class node:
    def __init__(self, spot):
        self.coord = spot


def det_len(location):
    x = location.coord[0]
    y = location.coord[1]
    length = (abs(x - a) - abs(y - b))
    if num == 1 and length == 1:
        stdout.write('No\n')
    else:
        stdout.write('Yes\n')
    quit()


def dfs(location):
    if grid[location.coord[0]][location.coord[1]].isdigit():
        det_len(location)
    new = location
    if location.coord[0] > 0:
        new.coord[0] -= 1
        x, y = int(new.coord[0]) - 1, int(new.coord[1]) - 1
        if grid_spot[x][y] == 0 and grid[x][y] != '*':
            grid_spot[x][y] = 1
            dfs(location)
    if location.coord[0] < grid_size - 1:
        new.coord[0] += 1
        x, y = int(new.coord[0]) - 1, int(new.coord[1]) - 1
        if grid_spot[x][y] == 0 and grid[x][y] != '*':
            grid_spot[x][y] = 1
            dfs(location)
    if location.coord[1] > 0:
        new.coord[1] -= 1
        x, y = int(new.coord[0]) - 1, int(new.coord[1]) - 1
        if grid_spot[x][y] == 0 and grid[x][y] != '*':
            grid_spot[x][y] = 1
            dfs(location)
    if location.coord[1] < grid_size - 1:
        new.coord[1] += 1
        x, y = int(new.coord[0]) - 1, int(new.coord[1]) - 1
        if grid_spot[x][y] == 0 and grid[x][y] != '*':
            grid_spot[x][y] = 1
            dfs(location)
    stdout.write('No\n')
    quit()


grid = []
grid_size = int(stdin.readline())
if grid_size < 2 or grid_size > 23:
    stdout.write('Grid is outside of size bounds.\n')
    quit()
grid_spot = [[0] * grid_size * grid_size]
for ii in range(grid_size):
    line = stdin.readline().strip('\n')
    if len(line) != grid_size:
        stdout.write('Input not equal to grid size.\n')
        quit()
    line = [char for char in line]
    grid.append(line)
num = 0
for ii in range(grid_size):
    for jj in range(grid_size):
        if grid[ii][jj] == 'M':
            root = node([ii, jj])
        if grid[ii][jj].isdigit:
            num = grid[ii][jj]
a = int(root.coord[0])
b = int(root.coord[1])
dfs(root)
