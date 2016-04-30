import cardinals
class player:

    def __init__(self, start_position, start_heading):
        # heading must be a tuple or a list, and it always becomes
        # a tuple when inside the player instance.
        self.position = start_position
        self.new_position = self.position
        self.heading = tuple(start_heading)
        self.name = raw_input("what is your name?: ")

## execute() definition
    def execute(self, command):
        # command should be a list with two elements only. first should be the
        # action to be performed and the second should be the direction.

        # dictionary containing possible actions
        action = command[0]
        argument = command[-1] # protect against a single element list
        
        def walk(argument):
            try:
                num = int(argument)
            except:
                num = 1
            
            new_position = [
                    self.position[0]+(self.heading[0]*num),
                    self.position[1]+(self.heading[1]*num)
                    ]
            self.new_position = new_position
            return 0 

        def face(argument):
            if argument in cardinals.directions.keys():
                self.heading = cardinals.directions[argument]
                return 0
            else:
                return 1

        def turn(argument):
            left = cardinals.ccw_turn
            right = cardinals.cw_turn
            sides = {
                    "left":left,
                    "l":left,
                    "right":right,
                    "r":right
            }
        
            if argument in sides.keys():
                self.heading = sides[argument](self.heading)
                return 0
            else:
                return 1

        # dict of available actions
        possible_actions = {
                "walk":walk,
                "w":walk,
                "face":face,
                "f":face,
                "turn":turn,
                "t":turn,
                }

        if action in possible_actions.keys():
            return possible_actions[action](argument)

## end of execute() definition
    def request(self):
        if self.position != self.new_position:
            return 1
        else:
            return 0

    def update(self):
        self.position = self.new_position
        return self.position

