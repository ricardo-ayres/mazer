from random import randint
import maze_utils 

def unvisited_neighbours(maze, cell):
    unvisited = []

    #check north and south cells within range
    if cell[0] > 2:
        # check if unvisited, append to unvisited[] if true:
        if maze[cell[0]-2][cell[1]] == 2:
            unvisited.append([cell[0]-2, cell[1]]) # north
    if cell[0] < len(maze)-2:
        if maze[cell[0]+2][cell[1]] == 2:
            unvisited.append([cell[0]+2, cell[1]]) # south

    # check east and west cell within range
    if cell[1] > 2:
        if maze[cell[0]][cell[1]-2] == 2:
            unvisited.append([cell[0], cell[1]-2]) # west
    if cell[1] < len(maze[0])-2:
        if maze[cell[0]][cell[1]+2] == 2:
            unvisited.append([cell[0], cell[1]+2]) # east

    # return list of unvisited cell positions.
    return unvisited

def remove_wall(maze, p1, p2):
    y_offset = p1[0]+((p2[0]-p1[0])/2)
    x_offset = p1[1]+((p2[1]-p1[1])/2)
    if maze[y_offset][x_offset] == 1:
        return x_offset, y_offset

# implement randomized depth-first search algo
def generate(x_size, y_size, debug=0):
    cell_stack = []
    maze = maze_utils.make_template(x_size, y_size)
    
    if debug:
        for i in maze:
            print i
        
    # get the total number of cells and count them as unvisited
    unvisited_cells = x_size*y_size

    # make initial cell the current cell
    current_position = [1, 1]
    if debug:
        print (unvisited_cells, current_position, cell_stack)

    # mark it as visited (0 = path, 1 = wall, 2 = visited)
    maze[1][1] = 2 
    if debug:
        for i in maze:
            print i

    unvisited_cells -= 1 # take one from unvisited count
    
    if debug:
        print "unvisited:", unvisited_cells, "- entering loop"
    while unvisited_cells != 0:

        unvisited_around = unvisited_neighbours(maze, current_position)

        if debug:
            print(unvisited_around)

        if len(unvisited_around) != 0:
            if debug:
                print(unvisited_cells, current_position, cell_stack)
 
            # choose random unvisited neighbour
            next_position = unvisited_around[
                    randint(0, len(unvisited_around)-1)
                    ]

            # push current cell to the stack
            cell_stack.append(current_position)
            
            # remove wall between next and current cells
            wall_x, wall_y = remove_wall(maze, current_position, next_position)
            maze[wall_y][wall_x] = 0

            # make next cell the current cell and mark as visited:
            current_position = next_position
            maze[current_position[0]][current_position[1]] = 0 
            # take one from unvisited count.
            unvisited_cells -= 1

        elif len(cell_stack) != 0:
            #pop stack
            if debug:
                print("popping stack")
            current_position = cell_stack.pop()
        
        if debug:
            for i in maze:
                print i
            raw_input("loop end")
        
        # mark bottom right corner as exit
        maze[(y_size*2)-2][(x_size*2)-2] = 2
 
    return maze
