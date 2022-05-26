# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Directory Listing
from sys import stdout
import os
import argparse
import re


def directories(dirs, recurse):
    for file in dirs:
        if recurse > 0:
            os.path.join(new_path, file)
            new_dirs = os.listdir(new_path)
            directories(new_dirs, recurse - 1)
        else:
            stdout.write(file + "\n")


parser = argparse.ArgumentParser()
parser.add_argument('-g', '--gutter', help="set gutter", type=int,
                    default=2)
parser.add_argument('-w', '--line-width', help="set line width",
                    type=int, default=80)
parser.add_argument('-r', '--recursive', help="display contents of subdirs",
                    type=int, default=0)
parser.add_argument('-e', '--regular-expression',
                    help="only files matching regular expression are shown")
args = parser.parse_args()
new_path = '.'
dirs = os.listdir(new_path)
recurse = args.recursive
directories(dirs, recurse)
