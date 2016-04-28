class maze:
    def __init__(self, size):
        self.size = size
        self.setup(size)

    def view(self, position, heading):
        # heading is a vector
        hline       = "------------\n"
        wall        = "|XXXXXXXXXX|\n"
        corridor    = "|          |\n"
        exitwall    = "|---EXIT---|\n"
        objects = [corridor, wall, exitwall]
        view_type = objects[self.surroundings(position)[heading]]
        view = hline+view_type*5+hline+heading+"\n"
        return view

    def setup(self, size):
        # substitute this for a generation algorithm
        # keep a simple small maze hardcoded for testing purposes.
        self.blueprint = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 2, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1],
        ]

        # same here, define start position with the same algo that
        # generates the maze.
        self.start_position = [1,1]
        self.start_heading = "east"

    def surroundings(self, position):
        y_pos = position[0]
        x_pos = position[1]
        north_cell = self.blueprint[y_pos-1][x_pos] 
        east_cell = self.blueprint[y_pos][x_pos+1]
        south_cell = self.blueprint[y_pos+1][x_pos]
        west_cell = self.blueprint[y_pos][x_pos-1]
        surroundings = {
                "north":north_cell,
                "east":east_cell,
                "south":south_cell,
                "west":west_cell
                }
        return surroundings

class player:

    players_list = []

    def __init__(self, start_position, start_heading):
        # takes a maze object as argument and uses it to set the
        # player's starting position.
        self.position = start_position
        self.heading = start_heading

    def move(self, maze, command):
        #command is a list of words.
        directions = {
                "north":[-1,0],
                "south":[1,0],
                "east":[0,1],
                "west":[0,-1]
                }

        if command[0] == "walk":
            if maze.surroundings(self.position)[self.heading] in (0,2):
                self.position[0] += directions[self.heading][0]
                self.position[1] += directions[self.heading][1]
            else:
                print("You can't go through walls, asshole!")

        if (command[0] == "face" and
            command[1] in ("north","south","east","west") and
            len(command) == 2):
            self.heading = command[1]
        
        if command[0] not in ("walk", "face"):
            print("blah blah blah, do you even type?")
            
