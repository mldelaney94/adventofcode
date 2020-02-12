f = open("inputQ9.txt", 'r')

graph = {}
for line in f:
    line = line.strip()
    split = line.split(" ")
    if split[0] in graph:
        pass
    graph[split[0]] = [split[2], split[4]]

