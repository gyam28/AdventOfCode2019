file = open('puzzleInput.txt', 'r')
list = []
for line in file:
    list.append(line.rstrip('\n'))

cableAInput = list[0].split(',')
cableBInput = list[1].split(',')

cableA = []
cableB = []

startPosX = 0
startPosY = 0

for i in cableAInput:
    direction = i[0][0]
    steps = i[1:]
    if direction == "R":
        for step in range(0, int(steps)):
            startPosX += 1
            cableA.append((startPosX, startPosY))
    elif direction == "L":
        for step in range(0, int(steps)):
            startPosX -= 1
            cableA.append((startPosX, startPosY))
    elif direction == "U":
        for step in range(0, int(steps)):
            startPosY += 1
            cableA.append((startPosX, startPosY))
    elif direction == "D":
        for step in range(0, int(steps)):
            startPosY -= 1
            cableA.append((startPosX, startPosY))

startPosX = 0
startPosY = 0

for i in cableBInput:
    direction = i[0][0]
    steps = i[1:]
    if direction == "R":
        for step in range(0, int(steps)):
            startPosX += 1
            cableB.append((startPosX, startPosY))
    elif direction == "L":
        for step in range(0, int(steps)):
            startPosX -= 1
            cableB.append((startPosX, startPosY))
    elif direction == "U":
        for step in range(0, int(steps)):
            startPosY += 1
            cableB.append((startPosX, startPosY))
    elif direction == "D":
        for step in range(0, int(steps)):
            startPosY -= 1
            cableB.append((startPosX, startPosY))

setA = set(cableA)
setB = set(cableB)
unionX = setA.intersection(setB)

smallest = 0

for e in unionX:
    dist = abs(e[0] - 0) + abs(e[1] - 0)
    if smallest == 0:
        smallest = dist
    elif dist < smallest:
        smallest = dist

print(smallest)

shortest = 0
for e in unionX:
    distanceA = cableA.index(e)
    distanceB = cableB.index(e)
    result = distanceA + distanceB
    if shortest == 0:
        shortest = result
    elif shortest > result:
        shortest = result
print(shortest+2)
