from heapq import nsmallest

f = open("inputQ2.txt", "r")

total = 0
for line in f:
    line = line.rstrip()
    split = [int(x) for x in line.split("x")]
    split.sort()
    total += split[0] + split[0] + split[1] + split[1] + (split[0]*split[1]*split[2])

print(total)
