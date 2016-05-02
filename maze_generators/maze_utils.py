def make_template(x_size, y_size):
    
    maze = []

    # to initialize the maze array with given size we must consider
    # that mazes must be x_size cells wide and y_size cells tall
    # but every cell must have shared walls with the surrounding
    # cells:
    # 
    # 1 1 1 1 1
    # 1 0 1 0 1  example of a 2x1 initial maze array.
    # 1 1 1 1 1
    # 
    #so the maze array size must always be odd, and visitable cells
    # always have odd indexes:
    #
    # horizontally:
    # 1 (border wall) + x_size (number of cells)*2(cell+right wall):
    # [1] + [0, 1]*n  = [1, 0, 1, 0, 1, 0, 1] for n = 3.
    # vertically:
    # (1+2*x_size)*[1] + y_size*(x_cells+[1]*x_size) + [1]*x_size:
    #
    # [1, 1, 1, 1, 1, 1, 1],
    # [1, 0, 1, 0, 1, 0, 1],
    # [1, 1, 1, 1, 1, 1, 1],
    # [1, 0, 1, 0, 1, 0, 1],
    # [1, 1, 1, 1, 1, 1, 1],
    # [1, 0, 1, 0, 1, 0, 1],
    # [1, 1, 1, 1, 1, 1, 1]
    #
    # for y_size = 3.
    
    # build x_line with border walls:
    x_line = [1]
    for i in range(x_size):
        x_line.append(0)
        x_line.append(1)

    # build maze wity y_size cells + top and bottom walls:
    for i in range(y_size):
        maze.append([1]*(1+x_size*2)) #adds walls
        maze.append(x_line) # adds cells
    # close the maze with bottom wall:
    maze.append([1]*(1+x_size*2))

    return maze

def maze_position(x_position, y_position):
    # given the maze array in the format
    # defined above, return the correct index
    # for a x_position, y_position cell
    
    x_index = x_position*2+1
    y_index = y_position*2+1
    return x_index, y_index
