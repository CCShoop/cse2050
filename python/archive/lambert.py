"""Lambert module containing W() function."""
from sys import stdout
from math import exp


def w(z):
    calls = 4
    x = z
    x_new = -z
    while abs(x - x_new) > 0.0000000000001:
        ex = exp(x)
        x_new = x - (x * ex - z) / (x * ex + ex)
        error = abs(x - x_new)
        if error > 0.0000000000001:
            x = x_new
    stdout.write(f'{x:5.2f} {z:6.3f} {calls:4d} {error:8.2e}' + '\n')