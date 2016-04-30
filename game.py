#!/bin/env python2
import player
import maze
import cardinals

print("Commands: walk <number>, face <direction>, turn <left|right>")
print("directions can be: north, south, east, west.")
print("commands can be abbreviated as their first letter (w 3 = walk 3)")

m1 = maze.maze(1)
p1 = player.player(m1.start_position, m1.start_heading)

print(m1.view(p1.position, p1.heading))
while 1:
    # execute player commands:
    commands = raw_input("%s: " % p1.name).strip().strip(';').split(';')
    for step in commands: 
        p1.execute(step.strip().split())
    
        # check if player updated position, check move and then
        # update if valid.
        if p1.request():
            if m1.check_move(p1.new_position):
                p1.update()
            else:
                print("Can't move there!")
        
        # check winning condition
        if m1.blueprint[p1.position[0]][p1.position[1]] == 2:
            print("Congrats, %s! You won!" % p1.name)
            quit()
        
    # update view
    print(m1.view(p1.position, p1.heading))
