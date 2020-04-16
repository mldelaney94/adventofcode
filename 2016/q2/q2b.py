forbidden_locs = [[0, 0], [1, 0], [0, 1], [0, 3], [0, 4], [1, 4], [3, 0], [3,
    4], [4, 0], [4, 1], [4, 3], [4, 4]]

def main():
    with open("inputQ2.txt", "r") as f:
        for line in f:
            line = line.strip()
            liness = list(line)
            pos = [1, 1]
            for c in liness:
                # assume we start at 1,1
                if c == 'U':
                    if pos[0] + 1 < 5 and [pos[0] + 1, pos[1]] not in forbidden_locs:
                        pos[0] = pos[0] + 1
                elif c == 'D':
                    if pos[0] - 1 > -1 and [pos[0] - 1, pos[1]] not in forbidden_locs:
                        pos[0] = pos[0] - 1
                elif c == 'L':
                    if pos[1] - 1 > -1 and [pos[0], pos[1] - 1] not in forbidden_locs:
                        pos[1] = pos[1] - 1
                elif c == 'R':
                    if pos[1] + 1 < 5 and [pos[0], pos[1] + 1] not in forbidden_locs:
                        pos[1] = pos[1]+1
            print(pos)
            #correct numbers where manually figured out as it was faster than
            #coding

if __name__ == "__main__":
    main()
