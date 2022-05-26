"""Program to decipher heat map of birth dates"""
# Author: Cael Shoop, cshoop2018@my.fit.edu
# Course: CSE 2050, Spring 2020
# Project: Birth Date Heat Map

from sys import stdin, stdout
import mysql.connector
from mysql.connector import Error
import numpy
import matplotlib.pyplot as plt


def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='andrew.cs.fit.edu',
                                       database='stansifer',
                                       user='cse2050',
                                       password='sp2020')
        cursor = conn.cursor()
        cursor.execute('SELECT * from SSDI')
        rows = cursor.fetchmany(750000)
        dates = []
        for ii in range(len(rows)):
            dates.append(rows[ii][3])
        for ii in range(len(dates)):
            dates[ii] = dates[ii].split('-')
        a = []
        b = []
        for ii in range(len(dates)):
            a.append(int(dates[ii][1]))
            b.append(int(dates[ii][2]))
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        days = []
        for ii in range(31):
            days[ii] = ii
        print(ii)
        heatmap, a_edges, b_edges = numpy.histogram2d(a, b, bins=(31, 12))
        stdout.write(heatmap)
        fig, ax = plt.subplots()
        im = ax.imshow(heatmap)
        ax.set_aticks(numpy.arange(len(months)))
        ax.set_bticks(numpy.arange(len(days)))
        ax.set_aticklabels(months)
        ax.set_bticklabels(days)
        plt.setp(ax.get_aticklabels(), rotation=90, ha='right',
                 rotation_mode='anchor')
        ax.set_title("Birthdates")
        plt.show()
    except Error as e:
        stdout.write(e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()