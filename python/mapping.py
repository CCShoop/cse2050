"""Reads data from URLs and displays it"""
# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Mapping the Pandemic

from sys import stdin, stdout
import calendar
from urllib.request import urlopen


def det_day(date):
    day, month, year = (int(ii) for ii in date.split(' '))
    day_num = calendar.weekday(year, month, day)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return (days[day_num])


def det_month(month):
    if month == '01':
        return 'Jan'
    if month == '02':
        return 'Feb'
    if month == '03':
        return 'Mar'
    if month == '04':
        return 'Apr'
    if month == '05':
        return 'May'
    if month == '06':
        return 'Jun'
    if month == '07':
        return 'Jul'
    if month == '08':
        return 'Aug'
    if month == '09':
        return 'Sep'
    if month == '10':
        return 'Oct'
    if month == '11':
        return 'Nov'
    if month == '12':
        return 'Dec'


request = urlopen(
    'http://andrew.cs.fit.edu/~cse1002-stansifer/cse2050/projects/graph/us-states.csv')
all_states = request.read().strip()
states = [str(ii).split(',') for ii in str(all_states).split('\\n')]
request = urlopen(
    'http://andrew.cs.fit.edu/~cse1002-stansifer/cse2050/projects/graph/us-counties.csv')
all_counties = request.read().strip()
counties = [str(ii).split(',') for ii in str(all_counties).split('\\n')]
dash_line = '\n------------------------------------------------------------\n'
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
          'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
          'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
          'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
          'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
          'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
          'New Mexico', 'New York', 'North Carolina', 'North Dakota',
          'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvannia', 'Rhode Island',
          'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
          'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
          'Wisconsin', 'Wyoming', 'District of Columbia']
dated = "Date"
state = "State"
county = "County"
for line in stdin:
    if line == '\n':
        quit()
    place = line.split()
    classs = place[0]
    place.pop(0)
    count = place[0]
    place.pop(0)
    place = ' '.join(place)
    if classs != 'number' and classs != 'change':
        print('class')
        quit()
    if count != 'cases' and count != 'deaths':
        print('count')
        quit()
    check = False
    if place in states:
        stdout.write(f'{dated:18} {state:24}')
        check = True
    else:
        stdout.write(f'{dated:18} {county:24}')
    if classs == 'cases':
        stdout.write('Cases\n')
    elif classs == 'deaths':
        stdout.write('Deaths\n')
    stdout.write(dash_line)
    case_count = 0
    death_count = 0
    if check:
        for ii in range(len(states)):
            if states[ii][1] == place:
                day = states[ii][0][8:]
                month = states[ii][0][5:7]
                year = states[ii][0][:4]
                date = day + ' ' + month + ' ' + year
                weekday = det_day(date)
                month = det_month(month)
                date = (weekday + ', ' + day + ' ' + month + ' ' + year + ':')
                stdout.write(f'{date:18} {a:24}')
                if classs == 'number':
                    if count == 'cases':
                        stdout.write(f'{states[ii][3]}\n')
                    elif count == 'deaths':
                        stdout.write(f'{states[ii][4]}\n')
                elif classs == 'change':
                    if count == 'cases':
                        num = int(states[ii][3]) - case_count
                        case_count = int(states[ii][4])
                    elif count == 'deaths':
                        num = int(states[ii][4]) - death_count
                        death_count = int(states[ii][4])
                    stdout.write(f'+{num}\n')
    else:
        for ii in range(len(counties)):
            test = str(counties[ii][1] + '/' + str(counties[ii][2]))
            if place == test:
                day = counties[ii][0][8:]
                month = counties[ii][0][5:7]
                year = counties[ii][0][:4]
                date = day + ' ' + month + ' ' + year
                weekday = det_day(date)
                month = det_month(month)
                date = weekday + ', ' + ' ' + month + ' ' + year + ':'
                stdout.write(f'{date:18} {place:24}')
                if classs == 'number':
                    if count == 'cases':
                        stdout.write(f'{counties[ii][4]}\n')
                    elif count == 'deaths':
                        stdout.write(f'{counties[ii][5]}\n')
                elif classs == 'change':
                    if count == 'cases':
                        num = int(counties[ii][4]) - case_count
                        case_count = int(counties[ii][4])
                    elif count == 'deaths':
                        num = int(counties[ii][5]) - death_count
                        death_count = int(counties[ii][5])
                    stdout.write(f'+{num}\n')
    stdout.write('\n')
