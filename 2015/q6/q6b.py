f = open ("inputQ6.txt")

import numpy as np

lightArray = np.zeros((1000, 1000), 'int32')

for line in f:
    line = line.strip()
    firstSplit = line.split(' ')
    if firstSplit[0] == 'turn':
        coordsBottomCorner = firstSplit[2].split(',')
        coordsTopCorner = firstSplit[4].split(',')
        xBot = int(coordsBottomCorner[0])
        yBot = int(coordsBottomCorner[1])
        xTop = int(coordsTopCorner[0])
        yTop = int(coordsTopCorner[1])
        if firstSplit[1] == 'on':
            lightArray[xBot:xTop+1, yBot:yTop+1] += 1
        elif firstSplit[1] == 'off':
            lightArray[xBot:xTop+1, yBot:yTop+1] -= 1
            lightArray = np.where(lightArray < 0, 0, lightArray)
    elif firstSplit[0] == 'toggle':
        coordsBottomCorner = firstSplit[1].split(',')
        coordsTopCorner = firstSplit[3].split(',')
        xBot = int(coordsBottomCorner[0])
        yBot = int(coordsBottomCorner[1])
        xTop = int(coordsTopCorner[0])
        yTop = int(coordsTopCorner[1])
        lightArray[xBot:xTop+1, yBot:yTop+1] += 2


print(np.sum(lightArray))

f.close()
