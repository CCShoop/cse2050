"""Save the Manatee Game"""
#Author: Cael Shoop, cshoop2018@my.fit.edu
#Course: CSE 2050, Spring 2020
#Project: Save the Manatee

from urllib.request import urlopen
import argparse
import time
import pygame
from pygame.locals import *


coquinas = list()
hyacinth = list()
closed_gate = list()
opened_gate = list()
boats = list()
water = list()


def within(a_list, coordinates):
    if coordinates in a_list:
        return True
    return False


def move_boat():
    for boat in boats:
        right = ((boat[0] + 48), (boat[1] + 48))
        left = ((boat[0] - 48), (boat[1] + 48))
        down = (boat[0], (boat[1] + 48))
        if within(water, down) and down != (hugh_x, hugh_y):
            display.blit(boat_pic, down)
            boats.remove(boat)
            boats.append(down)
            display.blit(water_pic, boat)
            water.remove(down)
            water.append(boat)
        elif within(water, left) and left != (hugh_x, hugh_y):
            display.blit(boat_pic, left)
            boats.remove(boat)
            boats.append(left)
            display.blit(water_pic, boat)
            water.remove(left)
            water.append(boat)
        elif within(water, right) and right != (hugh_x, hugh_y):
            display.blit(boat_pic, right)
            boats.remove(boat)
            boats.append(right)
            display.blit(water_pic, boat)
            water.remove(right)
            water.append(boat)


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--map", type=str)
cmd_args = parser.parse_args()

url = cmd_args.map
with urlopen(url) as handle:
    board = handle.read().decode('utf-8')

boat_pic = pygame.image.load("boat.png")
coquina_pic = pygame.image.load("coquina.png")
grate_pic = pygame.image.load("grate.png")
hugh_pic = pygame.image.load("hugh.png")
hyacinth_pic = pygame.image.load("hyacinth.png")
injured_pic = pygame.image.load("injured.png")
openedgate_pic = pygame.image.load("open.png")
seagrass_pic = pygame.image.load("seagrass.png")
water_pic = pygame.image.load("water.png")

pygame.init()
width = 0
length = 0
for i in board:
    if i == "\n":
        width += 1

for i in board:
    if i == "\n":
        break
    length += 1

display = pygame.display.set_mode((length * 48, width * 48))
pygame.display.set_caption("Save the Manatee!")
x_loc = 0
y_loc = 0

font = pygame.font.SysFont("Serif", 25)

for i in board:
    if i == "\n":
        x_loc = -48
        y_loc += 48
    elif i == "M":
        display.blit(hugh_pic, (x_loc, y_loc))
        hugh_x = x_loc
        hugh_y = y_loc
    elif i == "W":
        display.blit(injured_pic, (x_loc, y_loc))
    elif i == "#":
        display.blit(coquina_pic, (x_loc, y_loc))
        t = (x_loc, y_loc)
        coquinas.append(t)
    elif i == "*":
        display.blit(boat_pic, (x_loc, y_loc))
        t = (x_loc, y_loc)
        boats.append(t)
    elif i == "\\":
        display.blit(hyacinth_pic, (x_loc, y_loc))
        t = (x_loc, y_loc)
        hyacinth.append(t)
    elif i == "G":
        display.blit(grate_pic, (x_loc, y_loc))
        t = (x_loc, y_loc)
        closed_gate.append(t)
    elif i == "O":
        display.blit(openedgate_pic, (x_loc, y_loc))
        t = (x_loc, y_loc)
        opened_gate.append(t)
    elif i == ".":
        display.blit(seagrass_pic, (x_loc, y_loc))
    elif i == " ":
        display.blit(water_pic, (x_loc, y_loc))
        t = (x_loc, y_loc)
        water.append(t)
    x_loc += 48

gate_loc = closed_gate[0]
total_hyacinths = len(hyacinth)
total_points = 0
points = font.render("Score: " + str(total_points), False, (10, 10, 10))
display.blit(points, (2, 0))
win = False
while True:
    for user_input in pygame.event.get():
        if user_input.type == QUIT:
            pygame.quit()
            quit()
        if len(hyacinth) == 0:
            if len(closed_gate) != 0:
                display.blit(openedgate_pic, gate_loc)
                closed_gate.remove(gate_loc)
            elif len(closed_gate) == 0 and (hugh_x, hugh_y) == gate_loc:
                total_points += total_hyacinths * 50
                display.blit(coquina_pic, (0, 0))
                display.blit(coquina_pic, (48, 0))
                display.blit(coquina_pic, (96, 0))
                points = font.render("Score: " + str(total_points), False, (10, 10, 10))
                display.blit(points, (2, 0))
                win = True
                break
        if user_input.type == KEYDOWN:
            if user_input.key == K_RIGHT:
                if within(coquinas, (hugh_x + 48, hugh_y)) or \
                        within(closed_gate, (hugh_x + 48, hugh_y)):
                    continue
                elif within(hyacinth, (hugh_x + 48, hugh_y)):
                    total_points += 25
                    display.blit(water_pic, (hugh_x, hugh_y))
                    hugh_x += 48
                    display.blit(hugh_pic, (hugh_x, hugh_y))
                    hyacinth.remove((hugh_x, hugh_y))
                    if (hugh_x, hugh_y) not in water:
                        water.append((hugh_x, hugh_y))
                elif within(boats, (hugh_x + 48, hugh_y)):
                    total_points -= 1
                    if within(water, (hugh_x + 96, hugh_y)):
                        display.blit(water_pic, (hugh_x, hugh_y))
                        hugh_x += 48
                        display.blit(hugh_pic, (hugh_x, hugh_y))
                        boats.remove((hugh_x, hugh_y))
                        boats.append((hugh_x + 48, hugh_y))
                        display.blit(boat_pic, (hugh_x + 48, hugh_y))
                    else:
                        continue
                else:
                    total_points -= 1
                    display.blit(water_pic, (hugh_x, hugh_y))
                    hugh_x += 48
                    display.blit(hugh_pic, (hugh_x, hugh_y))
                    if (hugh_x, hugh_y) not in water:
                        water.append((hugh_x, hugh_y))
            elif user_input.key == K_LEFT:
                if within(coquinas, (hugh_x - 48, hugh_y)) or \
                        within(closed_gate, (hugh_x - 48, hugh_y)):
                    continue
                elif within(hyacinth, (hugh_x - 48, hugh_y)):
                    total_points += 25
                    display.blit(water_pic, (hugh_x, hugh_y))
                    hugh_x -= 48
                    display.blit(hugh_pic, (hugh_x, hugh_y))
                    hyacinth.remove((hugh_x, hugh_y))
                    if (hugh_x, hugh_y) not in water:
                        water.append((hugh_x, hugh_y))
                elif within(boats, (hugh_x - 48, hugh_y)):
                    total_points -= 1
                    if within(water, (hugh_x - 96, hugh_y)):
                        display.blit(water_pic, (hugh_x, hugh_y))
                        hugh_x -= 48
                        display.blit(hugh_pic, (hugh_x, hugh_y))
                        boats.remove((hugh_x, hugh_y))
                        boats.append((hugh_x - 48, hugh_y))
                        display.blit(boat_pic, (hugh_x - 48, hugh_y))
                    else:
                        continue
                else:
                    total_points -= 1
                    display.blit(water_pic, (hugh_x, hugh_y))
                    hugh_x -= 48
                    display.blit(hugh_pic, (hugh_x, hugh_y))
                    if (hugh_x, hugh_y) not in water:
                        water.append((hugh_x, hugh_y))
            elif user_input.key == K_DOWN:
                if within(coquinas, (hugh_x, hugh_y + 48)) or \
                        within(closed_gate, (hugh_x, hugh_y + 48)):
                    continue
                elif within(hyacinth, (hugh_x, hugh_y + 48)):
                    total_points += 25
                    display.blit(water_pic, (hugh_x, hugh_y))
                    hugh_y += 48
                    display.blit(hugh_pic, (hugh_x, hugh_y))
                    hyacinth.remove((hugh_x, hugh_y))
                    if (hugh_x, hugh_y) not in water:
                        water.append((hugh_x, hugh_y))
                elif within(boats, (hugh_x, hugh_y + 48)):
                    total_points -= 1
                    if within(water, (hugh_x, hugh_y + 96)):
                        display.blit(water_pic, (hugh_x, hugh_y))
                        hugh_y += 48
                        display.blit(hugh_pic, (hugh_x, hugh_y))
                        boats.remove((hugh_x, hugh_y))
                        boats.append((hugh_x, hugh_y + 48))
                        display.blit(boat_pic, (hugh_x, hugh_y + 48))
                    else:
                        continue
                else:
                    total_points -= 1
                    display.blit(water_pic, (hugh_x, hugh_y))
                    hugh_y += 48
                    display.blit(hugh_pic, (hugh_x, hugh_y))
                    if (hugh_x, hugh_y) not in water:
                        water.append((hugh_x, hugh_y))
            elif user_input.key == K_UP:
                total_points -= 1
                if within(coquinas, (hugh_x, hugh_y - 48)) or \
                        within(closed_gate, (hugh_x, hugh_y - 48)):
                    continue
                elif within(hyacinth, (hugh_x, hugh_y - 48)):
                    total_points += 25
                    display.blit(water_pic, (hugh_x, hugh_y))
                    hugh_y -= 48
                    display.blit(hugh_pic, (hugh_x, hugh_y))
                    hyacinth.remove((hugh_x, hugh_y))
                    if (hugh_x, hugh_y) not in water:
                        water.append((hugh_x, hugh_y))
                elif within(boats, (hugh_x, hugh_y - 48)):
                    total_points -= 1
                    if within(water, (hugh_x, hugh_y - 48)):
                        display.blit(water_pic, (hugh_x, hugh_y))
                        hugh_y -= 48
                        display.blit(hugh_pic, (hugh_x, hugh_y))
                        boats.remove((hugh_x, hugh_y))
                        boats.append((hugh_x, hugh_y - 48))
                        display.blit(boat_pic, (hugh_x, hugh_y - 48))
                    else:
                        continue
                else:
                    total_points -= 1
                    display.blit(water_pic, (hugh_x, hugh_y))
                    hugh_y -= 48
                    display.blit(hugh_pic, (hugh_x, hugh_y))
                    if (hugh_x, hugh_y) not in water:
                        water.append((hugh_x, hugh_y))
            move_boat()
            display.blit(coquina_pic, (0, 0))
            display.blit(coquina_pic, (48, 0))
            display.blit(coquina_pic, (96, 0))
            points = font.render("Score: " + str(total_points), False, (10, 10, 10))
            display.blit(points, (2, 0))
    pygame.display.update()
    if win:
        wintext = font.render("Manatee Saved!", False, (10, 10, 10))
        wintextpos = wintext.get_rect()
        wintextpos.centerx = display.get_rect().centerx
        wintextpos.centery = display.get_rect().centery
        display.blit(wintext, wintextpos)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        quit()
