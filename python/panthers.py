"""Dijkstra's Algorithm"""
# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Panther Party

from sys import stdin, stdout


class vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([ii.id for ii in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, node):
        if node in self.vert_dict:
            return self.vert_dict[node]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

    def get_vertices(self):
        return self.vert_dict.keys()


if __name__ == '__main__':
    g = graph()
    layers, paths, dest = stdin.readline().split()
    layers = int(layers)
    paths = int(paths)
    for ii in range(layers):
        vert = str(ii)
        g.add_vertex(vert)
    max = 0
    for ii in range(paths):
        a, b, c = stdin.readline().split()
        c = int(c)
        if (a == dest or b == dest) and c > max:
            max = c
        g.add_edge(a, b, c)
    stdout.write(f'{max * 2}\n')
