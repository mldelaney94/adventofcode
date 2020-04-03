""" finds number of paths from bottom left corner to top right corner,
where each path is width+height distance, in a grid

As such, you can only go right or up at each square

There are 'inaccessible' squares given in the 'bad' input.

Function sums the square below and the square to the left of the current
square, and sets squares with a value of BAD to 0 specifically """

BAD = -1
END = 1

def numWays(width, height, bad):
    road = [[0]*(width+1) for i in range(height+1)]
    road[0][0] = 1
    for item in bad:
        road[item[2]][item[3]] = BAD
    i = 0
    while i < len(road):
        j = 0
        while j < len(road[i]):
            if road[i][j] == BAD:
                road[i][j] = 0
            elif i > 0:
                if j > 0:
                    road[i][j] = road[i-1][j] + road[i][j-1]
                else:
                    road[i][j] = road[i-1][j]
            else:
                if j > 0:
                    road[i][j] = road[i][j-1]
            j += 1
        i += 1
            
            
    print(road[height][width])

numWays(2,2,[[0,0,1,0], [1,2,2,2], [1,1,2,1]])
