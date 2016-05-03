import maze_utils
from random import randint

def generate(size_x, size_y, debug=0):
    def abort(message):
        print("maze generation failed :(")
        print(message)
        #quit()

    # get maze template (1 for wall, 2 for cells)
    maze = maze_utils.make_template(size_x, size_y, 0)
    
    # generate a list of all valid walls:
    walls_list = []
    for j in range(1,len(maze)-1):        # don't include borders
        for i in range(1,len(maze[j])-1):
            if j%2 and not i%2:
                walls_list.append([j,i])
            if (not j%2) and i%2:
                walls_list.append([j,i])

    # generate a set for each cell:
    x_cell_index_range = range(1, size_x*2, 2)
    y_cell_index_range = range(1, size_y*2, 2)
    cells_sets = []
    for j in y_cell_index_range:
        for i in x_cell_index_range:
            cells_sets.append([[j,i]])

    if debug:
        print("##########")
        for i in maze:
            print i
        print("walls: %s" % walls_list)
        print("cells: %s" % cells_sets)
        print("##########")

    
    # enter loop:
    for wall in range(len(walls_list)):
        # choose random wall
        random_wall = randint(0, len(walls_list)-1)
        # take it out from walls list
        current_wall = walls_list.pop(random_wall)

        if maze[current_wall[0]][current_wall[1]] == 1: # sanity check
            # decide if this is a horizontal or vertical wall
            if current_wall[0] % 2: # true if vertical wall
                # cell west of wall:
                cell_a = [current_wall[0], current_wall[1]-1]
                # cell east of wall:
                cell_b = [current_wall[0], current_wall[1]+1]
            elif current_wall[1] % 2: # true if horizontal wall:
                # cell north of wall:
                cell_a = [current_wall[0]-1, current_wall[1]]
                # cell south of wall:
                cell_b = [current_wall[0]+1, current_wall[1]]


        # get indexes of cell sets
        for i in range(len(cells_sets)):
            if cell_a in cells_sets[i]:
                cell_a_group = i
            if cell_b in cells_sets[i]:
                cell_b_group = i
        
        # check if cells belong to different sets:
        if cell_a_group != cell_b_group:
            # copy elements from 'b' set to 'a' set
            map(cells_sets[cell_a_group].append, cells_sets[cell_b_group])
            # remove b set:
            cells_sets.pop(cell_b_group)

            # remove wall:
            maze[current_wall[0]][current_wall[1]] = 0
    # end of for loop

    return maze
