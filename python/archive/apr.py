# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Annual Percentage Rate
from sys import stdin, stdout
from decimal import Decimal
counter = 0
payed = Decimal("0")
prev_payed = payed
balance, interest, payment = stdin.readline().split()
balance = Decimal(balance)
interest = Decimal(interest)
payment = Decimal(payment)
stdout.write("\npayment       balance      interest\n")
while balance >= 0:
    line = '{:>7} {:>13} {:>13}'.format(counter, balance, payed)
    line = line + "\n"
    stdout.write(line)
    if balance > 0:
        payed = payed + balance * (interest / 12 / 100)
        payed = round(payed, 2)
        prev_payed = balance * (interest / 12 / 100)
        prev_payed = round(prev_payed, 2)
        if payment * (interest / 100) <= balance:
            balance = balance - payment + prev_payed
            balance = round(balance, 2)
        else:
            balance = Decimal("0.00")
        counter = counter + 1
    else:
        quit()
balance = Decimal("0.00")
line = '{:>7} {:>13} {:>13}'.format(counter, balance, payed)
line = line + "\n"
stdout.write(line)
