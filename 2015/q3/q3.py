f = open('inputQ3.txt', 'r')

q3_set1 = set()
q3_set2 = set()
x1 = 0
y1 = 0
x2 = 0
y2 = 0
i = 0
for line in f:
    for char in line:
        if i == 0:
            if char == '>':
                x1 += 1
            elif char == '<':
                x1 -= 1
            elif char == '^':
                y1 += 1
            elif char == 'v':
                y1 -= 1
            q3_set1.add((x1, y1))
        else:
            if char == '>':
                x2 += 1
            elif char == '<':
                x2 -= 1
            elif char == '^':
                y2 += 1
            elif char == 'v':
                y2 -= 1
            q3_set2.add((x2, y2))
        if i == 0:
            i = 1
        else:
            i = 0

q3_set3 = q3_set1.union(q3_set2)
print(len(q3_set3))
