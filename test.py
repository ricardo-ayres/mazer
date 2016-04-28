#!/bin/env python2
from mazer import *

m1 = maze('')
p1 = player(m1.start_position, m1.start_heading)

print(m1.view(p1.position, p1.heading))
while 1:
    p1.move(m1, raw_input("p1: ").split())
    if m1.blueprint[p1.position[0]][ p1.position[1]] == 2:
        print("Congrats! you won!")
        quit()
    print(m1.view(p1.position, p1.heading))

