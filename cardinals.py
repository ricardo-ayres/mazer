def cw_turn(vector2d):
    result = (vector2d[1], -vector2d[0])
    return result

def ccw_turn(vector2d):
    result = (-vector2d[1], vector2d[0])
    return result

directions = {
    "north":(-1,0),
    "n":(-1,0),
    "south":(1,0),
    "s":(1,0),
    "east":(0,1),
    "e":(0,1),
    "west":(0,-1),
    "w":(0,-1)
    }

vectors = {
    (-1,0):"north",
    (1,0):"south",
    (0,1):"east",
    (0,-1):"west"
    }
