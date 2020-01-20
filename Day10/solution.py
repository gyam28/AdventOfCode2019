from math import atan2
list = open('puzzleInput.txt', 'r').read().split("\n")

asteroids = []

y = 0

for row in list:
    parts = [el for el in row]
    x = 0
    for elem in parts:
        if elem == "#":
            asteroids.append([x, y])
        x += 1
    y += 1

combinations = []
for mainAster in asteroids:
    angles = set()
    for aster in asteroids:
        if aster == mainAster:
            continue
        angle = atan2(mainAster[1]-aster[1], mainAster[0]-aster[0])
        angles.add(angle)

    combinations.append(len(angles))

print(max(combinations))
