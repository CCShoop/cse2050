# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Mayan Long Count
from sys import stdin, stdout
from math import floor
from calendar import weekday

# Tzolkin


def tzolkin(day):
    if day == 0:
        stdout.write("Imix     ")
    elif day == 1:
        stdout.write("Ik       ")
    elif day == 2:
        stdout.write("Akbal    ")
    elif day == 3:
        stdout.write("Kan      ")
    elif day == 4:
        stdout.write("Chicchan ")
    elif day == 5:
        stdout.write("Cimi     ")
    elif day == 6:
        stdout.write("Manik    ")
    elif day == 7:
        stdout.write("Lamat    ")
    elif day == 8:
        stdout.write("Muluk    ")
    elif day == 9:
        stdout.write("Oc       ")
    elif day == 10:
        stdout.write("Chuen    ")
    elif day == 11:
        stdout.write("Eb       ")
    elif day == 12:
        stdout.write("Ben      ")
    elif day == 13:
        stdout.write("Ix       ")
    elif day == 14:
        stdout.write("Men      ")
    elif day == 15:
        stdout.write("Cib      ")
    elif day == 16:
        stdout.write("Caban    ")
    elif day == 17:
        stdout.write("Etznab   ")
    elif day == 18:
        stdout.write("Cauac    ")
    elif day == 19:
        stdout.write("Ahau     ")

# Haab


def haab(day):
    if day == 0:
        stdout.write("Pop     ;  ")
    elif day == 1:
        stdout.write("Uo      ;  ")
    elif day == 2:
        stdout.write("Zip     ;  ")
    elif day == 3:
        stdout.write("Zotz    ;  ")
    elif day == 4:
        stdout.write("Tzec    ;  ")
    elif day == 5:
        stdout.write("Xul     ;  ")
    elif day == 6:
        stdout.write("Yaxkin  ;  ")
    elif day == 7:
        stdout.write("Mol     ;  ")
    elif day == 8:
        stdout.write("Chen    ;  ")
    elif day == 9:
        stdout.write("Yax     ;  ")
    elif day == 10:
        stdout.write("Zac     ;  ")
    elif day == 11:
        stdout.write("Ceh     ;  ")
    elif day == 12:
        stdout.write("Mac     ;  ")
    elif day == 13:
        stdout.write("Kankin  ;  ")
    elif day == 14:
        stdout.write("Muan    ;  ")
    elif day == 15:
        stdout.write("Pax     ;  ")
    elif day == 16:
        stdout.write("Kayab   ;  ")
    elif day == 17:
        stdout.write("Cumku   ;  ")
    elif day == 18:
        stdout.write("Uayeb   ;  ")

# Testing Julian to Gregorian


def gregorian(julian):
    f = julian + 1401 + (((4 * julian + 274277) / 146097) * 3) / 4 - 38
    e = 4 * f + 3
    g = e % 1461 / 4
    h = 5 * g + 2
    D = (h % 153) / 5 + 1
    M = (h / 153 + 2) % 12 + 1
    Y = (e / 1461) - 4716 + (12 + 2 - M) / 12
    if D > 1:
        D = int(D) - 1
    else:
        D = int(D)
    M = int(M)
    Y = int(Y)
    if Y < 0:
        Y = Y - 1
    day_of_week(D, M, Y)
    stdout.write(str(D) + " ")
    print_month(M)
    stdout.write(str(Y) + "\n")

# Printing day of week


def day_of_week(D, M, Y):
    if M < 3:
        Z = Y - 1
    else:
        Z = Y
    day = (23 * M // 9 + D + 4 + Y + Z // 4 - Z // 100 + Z // 400)
    if M >= 3:
        day = day - 2
    day = day % 7
    if day == 0:
        stdout.write("Sun, ")
    elif day == 1:
        stdout.write("Mon, ")
    elif day == 2:
        stdout.write("Tue, ")
    elif day == 3:
        stdout.write("Wed, ")
    elif day == 4:
        stdout.write("Thu, ")
    elif day == 5:
        stdout.write("Fri, ")
    elif day == 6:
        stdout.write("Sat, ")


# Printing month letters
def print_month(M):
    if M == 1:
        stdout.write("Jan ")
    elif M == 2:
        stdout.write("Feb ")
    elif M == 3:
        stdout.write("Mar ")
    elif M == 4:
        stdout.write("Apr ")
    elif M == 5:
        stdout.write("May ")
    elif M == 6:
        stdout.write("Jun ")
    elif M == 7:
        stdout.write("Jul ")
    elif M == 8:
        stdout.write("Aug ")
    elif M == 9:
        stdout.write("Sep ")
    elif M == 10:
        stdout.write("Oct ")
    elif M == 11:
        stdout.write("Nov ")
    elif M == 12:
        stdout.write("Dec ")


# Increases gap between numbers and rest of input, then cuts off excess
line = stdin.readline().replace("  ", "---")
line = line.replace(" ", "")
line = line.replace("-", "   ")
line = line[:14]
v, w, x, y, z = line.split(".")
v = int(v)
w = int(w)
x = int(x)
y = int(y)
z = int(z[:2])
line = '{:>2}.{:>2}.{:>2}.{:>2}.{:>2}'.format(v, w, x, y, z)
# Formatted input
stdout.write(line + ";  ")
# Tzolkin dates
julian = v * 144000 + w * 7200 + x * 360 + y * 20 + z
day = (4 + julian) % 13
stdout.write('{:>2} '.format(day))
day = julian % 20 + 19
if day > 19:
    day = day - 20
tzolkin(day)
# Haab dates
day = (julian - 17) % 365 % 20
stdout.write('{:>2} '.format(day))
day = floor(((julian - 17) % 365) / 20)
haab(day)
# Julian
julian_other = julian + 584283
stdout.write('{:>7} '.format(julian_other) + "JD;  ")
# Gregorian
gregorian(julian_other)
