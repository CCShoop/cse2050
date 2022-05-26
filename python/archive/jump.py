# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Jumping Jehoshaphat
from sys import stdout
from decimal import Decimal
import argparse
import random
value = 0
within = 0
without = 0
probability = Decimal("0")
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--seed', help="set random number generator seed")
parser.add_argument('-d', '--distance',
                    help="set distance to check probability of (required)")
parser.add_argument(
    '-j', '--jumps', type=int, choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    help="set number of jumps (required)")
parser.add_argument(
    '-t', '--trials', default=1000,
    help="set number of trials (default 1000)")
args = parser.parse_args()
if args.seed:
    args.seed = int(args.seed)
args.distance = Decimal(args.distance)
args.jumps = int(args.jumps)
args.trials = int(args.trials)
for ii in range(args.trials):
    value = random.randint(0, args.jumps)
    if value <= args.distance:
        within = within + 1
without = args.trials - within
probability = within / args.trials
probability = round(probability, 5)
stdout.write("within " + str(within) + "; without " +
             str(without) + "; probability ")
stdout.write(f'{probability:.5f}' + '\n')
