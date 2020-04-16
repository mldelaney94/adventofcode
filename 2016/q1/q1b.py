import sys

def main():
    direction = 0 #0 = N, 1 = E, 2 = S, 3 = S
    coords = [0, 0]
    steps_set = set()
    steps_set.add(tuple(coords))
    with open('inputQ1.txt', 'r') as f:
        instructions = []
        for line in f:
            line = line.strip()
            instructions = line.split(', ')
            print(instructions)
        for instruction in instructions:
            if instruction[0] == 'R':
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4
            for i in range(int(instruction[1:])):
                coords = make_move(direction, 1, coords)
                if tuple(coords) in steps_set:
                    print(coords)
                    sys.exit()
                steps_set.add(tuple(coords))

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

if __name__ == "__main__":
    main()
