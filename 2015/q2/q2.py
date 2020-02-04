f = open("inputQ2.txt", "r")

total = 0
for line in f:
    line = line.rstrip()
    split = line.split("x")
    l = int(split[0])
    w = int(split[1])
    h = int(split[2])
    total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

print(total)
