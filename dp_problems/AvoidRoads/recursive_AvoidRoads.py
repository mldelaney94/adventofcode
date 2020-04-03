""" finds number of paths from bottom left corner to top right corner,
where each path is width+height distance, in a grid

As such, you can only go right or up at each square

There are squares that are inaccessible, denoted by coords in 'bad'

Algorithm goes up and to the right for each square, until it reaches either an
edge (cannot go up or right any further) or a 'bad' square. For edges, if it is
right edge, go up until destination is reached, for top, right until reached,
skip 'bad'"""

BAD = -1
END = 1

def numWays(width, height, bad):
    road = [[0]*(width+1) for i in range(height+1)]
    for item in bad:
        road[item[2]][item[3]] = BAD
    num_roads = 0
    num_roads = go(road, 0, 0)
    print(num_roads)

def go(road, x, y):
    if road[y][x] == BAD:
        return 0
    if y >= len(road)-1:
        if x >= len(road[y])-1:
            return END
        elif road[y][x] == BAD:
            return 0
        elif x + 1 < len(road):
            return go(road, x+1, y)
    elif x >= len(road[y])-1:
        if road[y][x] == BAD:
            return 0
        if y + 1 < len(road):
            return go(road, x, y+1)
    else:
        if y + 1 < len(road) and x + 1 < len(road[y]):
            return go(road, x, y+1) + go(road, x+1, y)
#current bug, its the wrong way around (change instantiation of original list)
numWays(6, 6, [])
