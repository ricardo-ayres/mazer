import cardinals
import depth_first, kruskal
from random import choice

class maze:
    """Maze class definition.
    this class has the purpose of keeping the maze's blueprint
    and giving out information about it as requested."""
    def __init__(self, size_x, size_y=0):
        if size_y == 0:
            size_y = size_x

        self.setup(size_x, size_y)

    def view(self, position, heading):
         
        roofline    = "\,,,,,,,,,,,,/\n"
        groundline  = "/````````````\\\n"
        wall        = "X"
        corridor    = " "
        exitwall    = "E"
        bug_wall    = "!"
        objects = [corridor, wall, exitwall, bug_wall]
        
        left_wall_direction = cardinals.ccw_turn(heading)
        left_wall_type = self.surroundings(position)[left_wall_direction]
        right_wall_direction = cardinals.cw_turn(heading)
        right_wall_type = self.surroundings(position)[right_wall_direction]
        front_view_type = self.surroundings(position)[heading]
        
        left_wall = objects[left_wall_type]
        right_wall = objects[right_wall_type]
        front_view = objects[front_view_type]

        view_line = left_wall+"|"+front_view*10+"|"+right_wall+"\n"
        view = roofline+view_line*8+groundline+cardinals.vectors[heading]
        return view

    def setup(self, size_x, size_y):
        # substitute this for a generation algorithm
        # for now keep a simple small maze hardcoded for testing purposes.
        # self.blueprint = [
        # [1, 1, 1, 1, 1, 1],
        # [1, 0, 0, 0, 1, 1],
        # [1, 1, 1, 0, 2, 1],
        # [1, 0, 0, 0, 1, 1],
        # [1, 1, 1, 0, 1, 1],
        # [1, 1, 1, 1, 1, 1],
        # ]

        # same here, define start position with the same algo that
        # generates the maze.
        # self.start_position = [1,1]
        gen = choice(("depth_first", "kruskal"))
        generators = {
                "depth_first":depth_first,
                "kruskal":kruskal,
                #2:prim,
                }
        print("Generating a %s type maze..." % gen)
        self.blueprint = generators[gen].generate(size_x, size_y)
        self.start_position = [1,1]
        self.start_heading = [0,1]
        
        # hardcode exit position for now:
        self.blueprint[size_y*2-1][size_x*2-1] = 2

        print("Maze successfully generated! Good luck!")

    def surroundings(self, position):
        y_pos = position[0]
        x_pos = position[1]

        # Don't pee the pants if array goes out of range.
        try:
            north_cell = self.blueprint[y_pos-1][x_pos]
        except:
            north_cell = -1
        try:
            east_cell = self.blueprint[y_pos][x_pos+1]
        except:
            east_cell = -1
        try:
            south_cell = self.blueprint[y_pos+1][x_pos]
        except:
            south_cell = -1
        try:
            west_cell = self.blueprint[y_pos][x_pos-1]
        except:
            west_cell = -1

        surroundings = {
                (-1, 0):north_cell,
                ( 0, 1):east_cell,
                ( 1, 0):south_cell,
                ( 0,-1):west_cell
                }
        return surroundings

    def check_move(self, position):
        if self.blueprint[position[0]][position[1]] == 1:
            return 0
        else:
            return 1
