def main():
    direction = 0 #0 = N, 1 = E, 2 = S, 3 = S
    coords = [0, 0]
    steps_set = set()
    with open('inputQ1.txt', 'r') as f:
        instructions = []
        for line in f:
            line = line.strip()
            instructions = line.split(', ')
        for instruction in instructions:
            steps = []
            if instruction[0] == 'R':
                steps = instruction.split('R')
                direction = (direction + 1) % 4
            else:
                steps = instruction.split('L')
                direction = (direction - 1) % 4
            for i in range(int(steps[1])):
                coords = make_move(direction, i, coords)
                if tuple(coords) in steps_set:
                    print(coords)
                    sys.exit()
                steps_set.add(tuple(coords))
    return steps_set

def make_move(direction, steps, coords):
    if direction == 0:
        coords[1] += int(steps)
    elif direction == 1:
        coords[0] += int(steps)
    elif direction == 2:
        coords[1] -= int(steps)
    elif direction == 3:
        coords[0] -= int(steps)
    return coords

import sys


FACTORS = ((0, 1),   # turning right, N
           (1, 0),   # E
           (0, -1),  # S
           (-1, 0)   # W
           )
DIRF = {'R': lambda x: (x+1) % 4,
        'L': lambda x: (x-1) % 4
        }


def main2():
    current_dir = 0
    loc = (0, 0)  # (x, y)
    memo = set()  # memoize visited locations
    memo.add(loc)

    f = open('inputQ1.txt', 'r')
    for line in f:
        for turn in [x.strip() for x in line.split(',')]:
            d, c = turn[0], int(turn[1:])
            current_dir = DIRF[d](current_dir)
            for _ in range(c):
                loc = (loc[0] + FACTORS[current_dir][0],
                       loc[1] + FACTORS[current_dir][1])
         #       if loc in memo:
         #           print ('DIST: %d' % (abs(loc[0]) + abs(loc[1])))
         #           print(len(memo))
         #           sys.exit(0)
                memo.add(loc)

    #print ('SAD TROMBONE')
    f.close()
    return memo

def main3():
    current_dir = 0  # facing north
    loc = (0, 0)
    f = open('inputQ1.txt', 'r')
    for line in f:
        for turn in [x.strip() for x in line.split(',')]:
            d, c = turn[0], int(turn[1:])
            current_dir = DIRF[d](current_dir)
            loc = (loc[0] + FACTORS[current_dir][0] * c,
                   loc[1] + FACTORS[current_dir][1] * c)

            print(loc)
    #print ('DIST: %d' % (abs(loc[0]) + abs(loc[1])))
    f.close()

if __name__ == "__main__":
    #other code said 115, 2, 113
    s1 = main()
    print(len(s1))
