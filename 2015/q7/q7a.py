f = open ("inputQ7.txt", 'r')

# current solution idea contains having two datasets, the raw converted data,
# and the data we turn it into

for line in f:
    line = line.strip()
    line = line.split()
    if len(line) < 5:
        if len(line) < 4:
            #basic assignment, wire1 sometimes num, sometimes wire
            wire1 = line[0]
            wire2 = line[2]
            if wire1.isdigit():
                wire1 = int(wire1)

        else:
            #NOT assignment
            wire1 = line[1]
            wire2 = line[3]
    else:
        wire1 = line[0] # sometimes they're just numbers 
        wire2 = line[2]
        wire3 = line[4]
        if line[1] == 'AND':
            # if and, wire1 could be num
            if wire1.isdigit():
                wire1 = int(wire1)
                # if this is the case, this is equivalent to 1 AND wire2 -> wire3 == wire2 -> wire3
            print('AND')
        elif line[1] == 'OR':
            # wires are just wires
            print('OR')
        elif line[1] == 'RSHIFT':
            # wire2 is num
            wire2 = int(wire2)
            print('RIGHTSHIFT')
        elif line[1] == 'LSHIFT':
            # wire2 is num
            wire2 = int(wire2)
            print('LEFTSHIFT')


f.close()
